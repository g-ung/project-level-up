#! python 3
'''
Reformat and Rename File Name
This script rename file name: Title_File_#1
'''
import os

def main():
    os.chdir('/Users/gabe_ung/Desktop/Test_folder')

    for file in os.listdir():
        
        file_name, file_ext = os.path.splitext(file)
        file_title, file_body, file_num = file_name.split('_')
        file_num = file_num.strip()[1:].zfill(2) # strip unwanted char, use zfill() to pad numnber with a zero
        
        #print("{}-{}-{}{}".format(file_num, file_title, file_body, file_ext))
        new_name = '{}-{}-{}{}'.format(file_num, file_title, file_body, file_ext)

        os.rename(file, new_name)


if __name__ == '__main__':
    main()