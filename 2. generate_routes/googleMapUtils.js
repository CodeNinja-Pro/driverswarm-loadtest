const axios = require('axios');
var polyline = require( "google-polyline" );
async function getCoordinatesBetweenPlaces(origin, destination, apiKey, numOfPoints) {
  try {
    // Get route between origin and destination using Directions API
    const response = await axios.get('https://maps.googleapis.com/maps/api/directions/json', {
      params: {
        origin,
        destination,
        key: apiKey,
      },
    });

    // Extract polyline from response
    const polyline = response.data.routes[0].overview_polyline.points;

    // Decode polyline to get coordinates
    const decodedPolyline = decodePolyline(polyline);

    // // Calculate step size for interpolation
    const stepSize = decodedPolyline.length / numOfPoints;

    // Interpolate coordinates along the route
    let coordinates = [];
    for (let i = 0; i < decodedPolyline.length; i += stepSize) {
      if (coordinates.length === numOfPoints - 1) {
        coordinates.push(decodedPolyline[decodePolyline.length -1]);
        break;
      }
      coordinates.push(decodedPolyline[Math.floor(i)]);
    }

    console.log(coordinates[0].length);

    coordinates = coordinates.map(coordinate => `${coordinate[0]}, ${coordinate[1]}`);
    return coordinates;
  } catch (error) {
    console.error('Error:', error.message);
    throw error;
  }
}

// Decode Google Maps polyline encoding
function decodePolyline(polyline) {
  // const polylineChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
  const polylineLength = polyline.length;
  let index = 0;
  let lat = 0;
  let lng = 0;
  const coordinates = [];

  while (index < polylineLength) {
    let b;
    let shift = 0;
    let result = 0;

    do {
      b = polyline.charCodeAt(index++) - 63;
      result |= (b & 0x1f) << shift;
      shift += 5;
    } while (b >= 0x20);

    const deltaLat = (result & 1) ? ~(result >> 1) : (result >> 1);
    lat += deltaLat;

    shift = 0;
    result = 0;

    do {
      b = polyline.charCodeAt(index++) - 63;
      result |= (b & 0x1f) << shift;
      shift += 5;
    } while (b >= 0x20);

    const deltaLng = (result & 1) ? ~(result >> 1) : (result >> 1);
    lng += deltaLng;

    coordinates.push([lat * 1e-5, lng * 1e-5]);
  }

  return coordinates;
}


const origin = 'New York, NY';
const destination = 'Los Angeles, CA';
const API_KEY = 'AIzaSyBESVvRa1_DdY6ONSQLgc-_o0HB2WGqCjk'

// getCoordinatesBetweenPlaces(origin, destination, API_KEY)
//   .then(coordinates => {
//     // console.log(coordinates);
//   })
//   .catch(error => {
//     console.error('Error:', error.message);
//   });

  module.exports = {
    getCoordinatesBetweenPlaces,
  };