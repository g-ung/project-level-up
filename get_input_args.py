#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: G. Ung
# DATE CREATED: 6 April 2022                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentPaser()
    args = parser.parser_args()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    '''
    argument parser for pet_images
    references:
        https://www.golinuxcloud.com/python-argparse/
        https://docs.python.org/3/howto/argparse.html#id1
    '''
    parser.add_argument('--dir', require=True, default='pet_image', help='The relative path to the pet_image directory', type=str)
    
    '''
    argument parser for CNN Model
    references:
        https://www.golinuxcloud.com/python-argparse/
        https://docs.python.org/3/howto/argparse.html#id1
    '''
    parser.add_argument('--arch', default='vgg', help='The ddesired CNN Model Architecture', type=str)
    
    '''
    argument parser for dogname.txt
    references:
        https://www.golinuxcloud.com/python-argparse/
        https://docs.python.org/3/howto/argparse.html#id1
    '''
    parser.add_argument('--dogifle', default='dognames.txt', help='The relative path to the dogdames.txt directory', type=str)
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function
    return args
