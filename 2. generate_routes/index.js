const { error } = require('console');
const csv = require('csv-parser');
const fs = require('fs');
const API_KEY = 'AIzaSyBESVvRa1_DdY6ONSQLgc-_o0HB2WGqCjk'
const googleMapsClient = require('@google/maps').createClient({ key: API_KEY });
const {getCoordinatesBetweenPlaces} = require("./googleMapUtils");
let count = 0;

const numOfCoordinates = 120.0

// Read the addresses from the input file and store them in an array
const addresses = [];
fs.createReadStream('../data/test_address_pairs.csv')
    .pipe(csv(['street', 'city_state', 'code']))
    .on('data', (data) => {console.log("Loading data from csv file...");return addresses.push(data) })
    .on('end', async () => {
        // Sort the addresses by postal code
        console.log("Started sorting by postal code...")
        await addresses.sort((a, b) => {
            const postalCodeA = a.code;
            const postalCodeB = b.code;
            return postalCodeA.localeCompare(postalCodeB);
        });

        const pairs = [];
        for (let i = 0; i < addresses.length - 1; i+=2) {
            let origin = addresses[i];
            origin = `${origin.street}, ${origin.city_state}, ${origin.code}`
            let destination = addresses[i + 1];
            destination = `${destination.street}, ${destination.city_state}, ${destination.code}`

            let coordinates = await getCoordinatesBetweenPlaces(origin, destination, API_KEY, numOfCoordinates);
            // If all pairs have been processed, write the result to a CSV file
            coordinates = coordinates.join("; ");
            pairs.push({origin, destination, coordinates});
            console.log(`Got route(${count}): between ${origin} and ${destination}`);
            count++;
            if (pairs.length * 2 + 1 >= addresses.length) {
                const csvData = pairs.map(pair => [pair.origin, pair.destination, pair.coordinates].join(";"));
                // With Header 
                // const csvContent = 'origin,destination,coordinates\n' + csvData.join('\n');
                // Without Header
                const csvContent = "sep=;\n"+csvData.join('\n');

                fs.writeFile('../data/test_route_tbl.csv', csvContent, (err) => {
                    if (err) throw err;
                    console.log('Output file saved.');
                });
            }
        }
    });

