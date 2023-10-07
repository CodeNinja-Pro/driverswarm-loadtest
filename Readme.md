# Driver Swarm Load Test

### 1. Prepare Random Address Data

#### Prerequisite

To proceed with this step, make sure you have Python installed on your system.

1. Go to [Random Address Generater Site](https://codebeautify.org/random-street-address).
2. Enter the number of random addresses you need.
3. Click the "Download" button.
4. Run the following command to process downloaded txt files, remove duplicate addresses, and merge them into one txt file:
    ```
    cd "1. get_random_addresses" && python address_merge.py
    ```
    This will generate a file named "merged_addresses.txt" in the "data" directory.
5. Convert "merged_addresses.txt" file to CSV format 
    Please ensure that the delimiter is set to ';' instead of ',' since the addresses contain ','.
    This will generate a file named "address_paris.csv" in "data" directory.

### 2. Generate Route Table

#### Prerequisite

To proceed with this step, you need to have the Node.js runtime environment installed.

1. Navigate to the "2. generate_routes" directory.
2. Run the following command to install the necessary dependencies:
    ```
    npm install
    ```
3. Run the following command to generate the route table:
    ```
    npm start
    ```
   This will generate a file named "route_tbl_120.csv" in "data" directory.

### 3. Generate Binary Route Table 

#### Prerequisite

To proceed with this step, you need to have the Java runtime environment installed.

1. Navigate to the "3. generate_binary_file" directory.
2. Run the following command to generate the route table with binary format:
    ```
    groovy csv2bin.groovy
    ```
    This will two files: "generate route_tbl_120.dat" and "route_tbl_120_regernated".
    You can use "route_tbl_120_regenerated.csv" to comfirm if the conversion was successful.

### 4. Groovy Script for Load Test in JMeter

"3. generate_binary_file/script_for_jmeter_groovy":
This file is used in JMeter for your load testing purpose

### 5. Locust
1. Navigate to "4. locust" directory

2. Run the following command to install "locust" package:
    ```
    pip install locust
    ```
3. Run the following command to install "har2locust" package:
    ```
    pip install har2locust
    ```
4. Convert har file to locust file using "har2locust" package:
    ```
    har2locust mspetshop.net.har > locustfile.py
    ```
5. Run the following command to perform load test using locust:
    ```
    locust -f locustfile.py
    ```
6. You can check the address of the server on console.

### Important Note

Consider using a big dataset only after fully testing it with a small test dataset since the Google Maps Directions API charges you according to the number of you API requests.