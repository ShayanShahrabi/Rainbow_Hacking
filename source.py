import hashlib
import csv

from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    # Create an empty ordered dictionary to store the hashed values and their corresponding numbers.
    hashed_dict = OrderedDict()
    
    # Loop through all numbers from 1000 to 9999.
    for num in range(1000, 10000):
        # Convert the number to a string and compute its hash value using sha256 algorithm.
        hash_value = hashlib.sha256(str(num).encode()).hexdigest()
        
        # Store the hash value and the corresponding number in the ordered dictionary.
        hashed_dict[hash_value] = num
        
    # Open the input CSV file in read mode.
    with open(input_file_name, 'r') as input_file:
        # Read the data from the input file into a list of lines.
        lines = input_file.readlines()
        
    # Open the output CSV file in write mode.
    with open(output_file_name, 'w') as output_file:
        # Loop through each line in the input file.
        for line in lines:
            # Split the line into name and hash value.
            name, hash_value = line.strip().split(',')
            
            # Write the name and the corresponding number from the ordered dictionary to the output file.
            output_file.write(f"{name},{hashed_dict[hash_value]}\n")
#------------------------------------------------------------------------------------------------------------
    


