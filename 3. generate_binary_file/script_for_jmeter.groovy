import org.apache.http.client.methods.HttpPost
import org.apache.http.entity.StringEntity
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.util.EntityUtils
import org.apache.http.HttpHeaders

def driverId = vars.get("driverId")
def routeId = vars.get("routeId")
def deliveryId = vars.get("deliveryId")
def routeIndex = vars.get("routeIndex").toInteger()
def positionIndex = vars.get("positionIndex").toInteger()

def threshold = 0.001
def sleepTime = 0.0
def maxLoopCount = 120;


def toRadians(deg) {
   return deg * (Math.PI / 180)
}
def GetDistance(lat1, lon1, lat2, lon2) {


    def R = 6371 // Radius of the earth in km
    def dLat = toRadians(lat2-lat1)
    def dLon = toRadians(lon2-lon1)
    def a = Math.sin(dLat/2) * Math.sin(dLat/2) +
             Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
             Math.sin(dLon/2) * Math.sin(dLon/2)
    def c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
    def distance = R * c // Distance in km

    return distance
}

def byteArrayFloat(byteArray) {
    def intValue = (byteArray[0] << 24) + ((byteArray[1] & 0xff) << 16) + ((byteArray[2] & 0xff) << 8) + (byteArray[3] & 0xff)
    return Float.intBitsToFloat(intValue)
}

def GetNextLocation() {
    def routeIndex = vars.get("routeIndex").toInteger()
    def positionIndex = vars.get("positionIndex").toInteger()

    def offset = routeIndex * 640 + positionIndex * 8;

    def file = new RandomAccessFile("test_route_tbl.dat", "r");
    file.seek(offset);
    def latitudeBytes = new byte[4];
    def longitudeBytes = new byte[4];
    file.read(latitudeBytes);
    file.read(longitudeBytes);
    file.close()

    def latitude = byteArrayFloat(latitudeBytes)
    def longitude = byteArrayFloat(longitudeBytes)

    if (latitude == 0.0 && longitude == 0.0) {
        return "EOL"
    } else if (positionIndex >= 120) {
            return "EOL"
    } else {
        return [latitude, longitude]
    }
}
def prevLogitude = 0;
def prevLatitude = 0;
def count = 0;
while (true) {
    if (count > maxLoopCount){
        log.info("Max Loop Count Reached.");
        break;
    }
    def coordinates = GetNextLocation()
    if (coordinates == "EOL") {
        log.info("End of File reached")
        break
    } else {
        def latitude = coordinates[0]
        def longitude = coordinates[1]
        prevLatitude = latitude;
        prevLongitude = longitude;

        def timestamp = System.currentTimeMillis()

        def client = new DefaultHttpClient()
        def request = new HttpPost("http://driver-locations-staging-amd5fgczfjcze7hk.z01.azurefd.net/inbound")
        def headers = ["Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "api_key": vars.get("Authorization"), "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"]
        headers.each { key, value -> request.setHeader(key, value) }
        def requestBody = '{"events":[{"lat":' + latitude + ',"lng":' + longitude + ',"timestamp":' + timestamp + ',"driverId":"' + driverId + '","routeId":"' + routeId + '","deliveryIds":["' +         deliveryId + '"]}]}'
        request.entity = new StringEntity(requestBody)
        def response = client.execute(request)
        def responseBody = EntityUtils.toString(response.getEntity())


        log.info("Response Body: " + responseBody)

        positionIndex++;
        log.info(Integer.toString(positionIndex));
        log.info("{${Integer.toString(routeIndex)}, ${Integer.toString(positionIndex)}}")
        
        vars.put("positionIndex", Integer.toString(positionIndex))
        def distance = GetDistance(prevLatitude, prevLongitude, latitude, longitude);
        if (distance > threshold) {
            log.info("Distance is shorter than threshold")
          sleep(sleepTime);
        }
        count++;
    }
}
