#! python 3
'''
Convert Mac Address Format
This script will read mac addresses from an input text file, use 
list comprehensions to process the mac address from current format 
to desired mac address format.
'''
def main():
    mac_address = [] # empty list to store mac addresses from file

    # read mac addresses from input file
    input_file = "mac_addresses.txt" # enter the path to your file here
    with open(input_file, 'r') as in_f:
        for line in in_f.readlines():
            mac_address.append(line.strip())

    # convert mac addresses to desired format e.g. MM-MM-MM-SS-SS-SS to MM:MM:MM:SS:SS:SS
    # replace "-" with ":"
    mac_no_dash = [mac.replace('-', ':') for mac in mac_address] # edit this to suit your desired mac address format
  
    # convert capital to lowercase
    desired_mac_format = [mac.lower() for mac in mac_no_dash] # convert to lowercase, edit this to suit your desired mac address format
    
    # write new mac address format to new text file
    # if output file hasn't already been created a new output file will be created
    output_file = "mac_address_standardise.txt"
    with open(output_file, 'w') as out_f:
        for i in desired_mac_format:
            out_f.write(i)
            out_f.write("\n")

if __name__ == '__main__':
    main()
