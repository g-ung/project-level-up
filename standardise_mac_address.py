#! python 3
'''
Convert Mac Address Format
Convert mac address wtih dashes ("-") and capital letters
to lower case letters and colon (":")
'''
def main():
    mac_address = [] # empty list to store mac addresses from file

    input_file = "/Users/gabe_ung/Desktop/mac_addresses.txt"
    with open(input_file, 'r') as in_f:
        for line in in_f.readlines():
            mac_address.append(line)

    # replace "-" with ":"
    mac_no_dash = [] # empty list to store new mac addresses with dash removed
    for mac in mac_address:
        mac_colon = mac.replace('-', ':') # edit this to suit your desired mac address format
        mac_no_dash.append(mac_colon)
    
    # remove new line ("\n")
    mac_remove_newline = [] # empty list to stor new mac with "\n" removed
    for mac in mac_no_dash:
        mac_no_line = mac.replace("\n", "")
        mac_remove_newline.append(mac_no_line)
    
    # convert capital to lowercase
    desired_mac_format = [] # empty list to store the desire mac address format
    for mac in mac_remove_newline:
        mac_lowercase = mac.lower() # conver to lowercase, edit this to suit your desired mac address format
        desired_mac_format.append(mac_lowercase)

    output_file = "/Users/gabe_ung/Desktop/mac_address_standardise.txt"
    with open(output_file, 'w') as out_f:
        for i in desired_mac_format:
            out_f.write(i)
            out_f.write("\n")

if __name__ == '__main__':
    main()