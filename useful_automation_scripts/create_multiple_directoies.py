#! python 3
'''
Create Multiple New Diretories
Edit the block of code inside the for loop
as required.

This script was created so I could create multple
directories in sequence in one of the folders in my
GitHub repository
'''
import os

def main():
    # change to the diretory where you want to create your new directories
    path = '' # insert your path here
    os.chdir(path) 
   
    # dircectory name/directory prefix, change this variable as required
    directory = 'Chapter_'
    # check with
    #print(dir(os))
    #print('Current working directory: ', os.getcwd())

    # use range to specify the number of directories to create
    count = 0
    for i in range(8, 21):
        os.mkdir(directory + str(i))
        count += 1
    
    print('Directories created, {} directories created in {}'.format(count, path))

if __name__ == '__main__':
    main()