#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: G. Ung 
# DATE CREATED: Thursday 7 April 2022                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    '''
    use listdir() to extract contents from image_dir where image_dir specifies the path
    references:
        https://www.tutorialspoint.com/python3/os_listdir.htm
        https://www.pythonpool.com/python-listdir/
    '''
    # use listdir() to extract contents from image_dir
    image_dir = '/home/workspace/pet_images'
    image_files = listdir(image_dir)
    
    # create empty dictionary to store contents from image_dir
    results_dic = ()
    
    '''
    use os.pth.splitext() to split content from image_dir from the root and extension
        references:
        https://appdividend.com/2021/08/14/python-os-path-splitext-function/
    '''    
    # interate thru contents of image_dir start=0, stop=len(image_files), step=1
    for i in range(len(image_files)):
        # for macOS users check for files starting with ".", skip these files
        if image_files[i][0] != ".":
            # use os.pth.splitext() to split content from image_dir from the root and file extension
            f_name = os.path.splitext(image_files[i][0])
            f_name = image_files[i].split(".") # split the file at "." to seperate label and file extension
            
            # temp variable to store pet label from image_dir
            pet_breed = ""
            '''
            use isalpha() to check/split the numeric and alphabetical parts label
            references:
                https://www.tutorialspoint.com/python/string_isalpha.htm
            '''
            # iterate thru contents of image_dir, split numerical values from alphabetic values from file name
            for dog in image_files:
                if dog.isalpha(): # use isalpha() to check if all characters are alphabetic
                    pet_breed += pet_breed + "" # update pet_breed with just the alphabetic part of label w/ whitespace
            
            pet_breed = pet_breed.strip().lower()
            if image_files[i] not in results_dic: # check if word is in dictionary
                results_dic[image_files[i]] = results_dic.get(pet_breed)
            else:
                print("** Warning: Duplicate key: ", image_files[i], " exist in dictionary: results_dic with value: ", results_dic[image_files[i]])
             
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
