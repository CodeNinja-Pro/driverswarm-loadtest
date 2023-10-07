import java.nio.file.Files
import java.nio.file.Paths
import java.nio.ByteBuffer


// Colored Console logs in Groovy
def printlnWithColor(color, str) {
    // Map of ANSI Escape color codes
    final colorsMap = [black  : 30, red: 31, green: 32, yellow: 33,
                       blue   : 34, magenta: 35, cyan: 36, white: 37,
                       default: 39]
    // Create the escape sequence so string is color formatted                   
    final style = "${(char) 27}[${colorsMap[color]}" + "m"
    // Apply the escape sequence to the string by prepending it
    final styledStr = style + str
    // finally use println to print this escaped string
    println(styledStr)
}

def byteArrayFloat(byteArray) {
    def intValue = (byteArray[0] << 24) + ((byteArray[1] & 0xff) << 16) + ((byteArray[2] & 0xff) << 8) + (byteArray[3] & 0xff)
    return Float.intBitsToFloat(intValue)
}

def csvFileInput = "data/test_route_tbl_120.csv"                     // Test CSV File Input Path
def regeneratedCSVFile = "data/test_regenerated_route_tbl_120.csv"   // Regenerated CSV File Path === csv -> bin -> csv === (For Confirmation Of Functions)
def binFileOutput = "data/test_route_tbl_120.dat"                    // Bin File Output Path
def coordinatesPerRoute = 120;

def csv2bin(csvFileInput, binFileOutput, coordinatesPerRoute) {
    printlnWithColor("magenta", "\nConverting (csv -> bin): ${csvFileInput} to ${binFileOutput}");
    def data = new ByteArrayOutputStream()
    def lineNumber = 0;

    new File(csvFileInput).withReader { reader ->
        reader.eachLine { line ->
            lineNumber ++;
            if (line.startsWith("sep=")) {
                return // Skip the header row
            }

            def parts = line.split(";")
            printlnWithColor("blue", "\nRoute(" + (lineNumber - 1)+"): " + parts[0] + " -------- "+ parts[1]) 
            for (int j = 2; j < coordinatesPerRoute + 2; j++) {
                def lat = parts[j].split(",")[0].trim().toFloat()
                def lon = parts[j].split(",")[1].trim().toFloat()
                if(j == 2 || j == coordinatesPerRoute + 1){
                    printlnWithColor("green", "{${lineNumber-1}, ${j - 1}}: ${lat}, ${lon}")
                }
                def latBytes = ByteBuffer.allocate(4).putFloat(lat).array()
                def lonBytes = ByteBuffer.allocate(4).putFloat(lon).array()

                data.write(latBytes)
                data.write(lonBytes)
            }
        }
        Files.write(Paths.get(binFileOutput), data.toByteArray())
        printlnWithColor("cyan", "\nSaved binary route table at \"" + Paths.get(binFileOutput) +"\"") 
    }
}

def bin2csv(binFileOutput, csvFileInput, delimiter, coordinatesPerRoute) {
    printlnWithColor("magenta", "\nConverting (bin -> csv): ${binFileOutput} to ${csvFileInput}");

    def data = Files.readAllBytes(Paths.get(binFileOutput))
    def lines = []
    lines << "sep=" + delimiter;
    printlnWithColor("magenta", "\nTotal Bytes: ${data.length}");

    for (int i = 0; i < data.length / (coordinatesPerRoute * 8); i++) {
        def latitudes = []
        def longitudes = []
        def line = "";
        for (int j = 0; j < coordinatesPerRoute; j++) {
            def latBytes = data[(i * coordinatesPerRoute + j) * 8..(i * coordinatesPerRoute + j) * 8 + 3]
            def lonBytes = data[(i * coordinatesPerRoute + j) * 8 + 4..(i * coordinatesPerRoute + j) * 8 + 7]

            def lat = byteArrayFloat(latBytes);
            def lon = byteArrayFloat(lonBytes);

            line += lat + "," + lon;
            if (j != coordinatesPerRoute -1) {
                line += delimiter
            }        
        }
        lines << line
    }

    Files.write(Paths.get(csvFileInput), lines.join("\n").getBytes())
    printlnWithColor("cyan", "\nSaved CSV route table at \"" + Paths.get(csvFileInput) +"\"") 
}


def GetNextLocation(routeIndex, positionIndex, coordinatesPerRoute) {
    // def routeIndex = vars.get("routeIndex").toInteger()
    // def positionIndex = vars.get("positionIndex").toInteger()

    def offset = routeIndex * coordinatesPerRoute * 8 + positionIndex * 8;

    def file = new RandomAccessFile("data/test_route_tbl.dat", "r");
    file.seek(offset);
    def latitudeBytes = new byte[4];
    def longitudeBytes = new byte[4];
    file.read(latitudeBytes);
    file.read(longitudeBytes);
    file.close()

    def latitude = byteArrayFloat(latitudeBytes)
    def longitude = byteArrayFloat(longitudeBytes)

    if (latitude == 0.0 && longitude == 0.0) {
        return "EOF"
    } else {
        return [latitude, longitude].toString()
    }

    // return [latitude, longitude];
}

csv2bin(csvFileInput, binFileOutput, coordinatesPerRoute);
bin2csv(binFileOutput, regeneratedCSVFile, ";", coordinatesPerRoute)

println(GetNextLocation(0, 0, coordinatesPerRoute));