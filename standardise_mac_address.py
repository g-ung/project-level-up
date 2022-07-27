#! python 3
'''
Convert Mac Address Format
Convert current mac address format (":", "-" or ".") and capital 
(lowercase) letters to desired format.  

This script will read from from an input text file, use for 
loops to process the mac address from current format to desired
mac address format
'''
def main():
    mac_address = [] # empty list to store mac addresses from file

    # read mac addresses from input file
    input_file = "mac_addresses.txt" # enter the path to your file here
    with open(input_file, 'r') as in_f:
        for line in in_f.readlines():
            mac_address.append(line)

    # convert mac addresses to desired format e.g. MM-MM-MM-SS-SS-SS to MM:MM:MM:SS:SS:SS
    # replace "-" with ":"
    mac_no_dash = [] # empty list to store new mac addresses with dash removed
    for mac in mac_address:
        mac_colon = mac.replace('-', ':') # edit this to suit your desired mac address format
        mac_no_dash.append(mac_colon)
    
    # remove new line ("\n")
    mac_remove_newline = [] # empty list to store new mac with "\n" removed
    for mac in mac_no_dash:
        mac_no_line = mac.replace("\n", "")
        mac_remove_newline.append(mac_no_line)
    
    # convert capital to lowercase
    desired_mac_format = [] # empty list to store the desire mac address format
    for mac in mac_remove_newline:
        mac_lowercase = mac.lower() # convert to lowercase, edit this to suit your desired mac address format
        desired_mac_format.append(mac_lowercase)

    # write new mac address format to new text file
    # if output file hasn't already been created a new output file will be created
    output_file = "mac_address_standardise.txt"
    with open(output_file, 'w') as out_f:
        for i in desired_mac_format:
            out_f.write(i)
            out_f.write("\n")

if __name__ == '__main__':
    main()