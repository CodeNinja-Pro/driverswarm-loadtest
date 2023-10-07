import os
import datetime

# Create an empty list to store unique addresses
unique_addresses = []
duplication_count = 0

# Iterate through all the files in the "dataset" directory
for file_name in os.listdir("data/random_addresses"):
    if file_name.endswith(".txt"):
        with open(os.path.join("dataset", file_name), 'r') as file:
            # Read the contents of the file line by line
            lines = file.readlines()
            
            # Remove empty lines and add unique addresses to the list
            for line in lines:
                line = line.strip()
                if line != '':
                    if line not in unique_addresses:
                        unique_addresses.append(line)
                    else:
                        # Get the current timestamp
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log_message = f"\033[93m[{timestamp}] WARNING: Duplication detected ({duplication_count}): {line} in \"{file_name}\"\033[0m"
                        duplication_count += 1
                        print(log_message)
                        # print("Duplication detected"+str(duplication_count)+"\n" + line + " in" + file_name + "file")

# Write the unique addresses to a new file
with open("merged_addresses.txt", 'w') as merged_file:
    for address in unique_addresses:
        address_parts = address.split(' ')
        part1 = " ".join(address_parts[:-1]).strip()
        postal_code = address_parts[-1].strip()
        merged_file.write(f"{part1}, {postal_code}\n")
