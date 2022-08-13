#! python 3
'''
Rename File Names
Edit the block of code inside the for loop
to format file name to your requirements.
'''
import os

def main():
    os.chdir('enter file path to your files here')

    for file in os.listdir():
        # check with
        #print(file)
        #print(os.path.splitext(file))
        
        # assign variable names to each tuple
        file_name, file_ext = os.path.splitext(file)
        
        # assign variable names to each section of file name at split('_')
        file_title, file_body, file_num = file_name.split('_')

        # strip unwanted char, use zfill() to pad numnber with a zero
        file_num = file_num.strip()[1:].zfill(2) 
        
        #print("{}-{}-{}{}".format(file_num, file_title, file_body, file_ext))
        
        # new name format
        new_name = '{}-{}-{}{}'.format(file_num, file_title, file_body, file_ext)

        os.rename(file, new_name) # rename file according new_name format

if __name__ == '__main__':
    main()
