#! python 3
'''
Create Multiple New Diretories
Insert the directory name, source file path, and path 
(where the new directories are to be created) in the
variables provided in main() as required.
'''
import os

def new_dir_seq(dir_path, dir_name):
    '''
    Funtion to create multiple directories with sequencial names
    e.g. dir_1, dir_2, dir_3 ... dir_n

    Args:
        dir_path (string): the directory path where you want your new directories created
        dir_name (string): name of your directory: name, prefix or suffix

    Returns:
        print statment: status with number of directories created and where they have been created
    '''
    # change diretory where you want to create your new directories
    os.chdir(dir_path) 
   
    # create new directories in sequence
    # use range to specify the number of sequencial directories to create
    count = 0
    for i in range(1, 4): # add code to the for loop as required to build your directory name
        os.mkdir(dir_name + str(i)) # edit direcotry name sequence here
        count += 1
    
    print('Directories created, {} directories created in {}'.format(count, dir_path))

def new_dir_multiple(folder_path, file_path):
    '''
    Funtion to create multiple directories where name of directories are from a source file

    Args:
        folder_path (string): the directory path where you want your new directories created
        file_path (string): file path of your source file

    Returns:
        print statment: status with number of directories created and where they have been created
    '''
    # change to the diretory where you want to create your new directories
    os.chdir(folder_path) 

    # create multiple directories where name of directories are from a source file
    # input_file = ''# insert location of your input file here
    count = 0
    with open(file_path, 'r') as f:
        for dir in f.readlines():
            dir = dir.strip()
            os.mkdir(dir)
            count += 1
    
    print('Directories created, {} directories created in {}'.format(count, file_path))

def main():
    # dircectory name/prefix/suffix, change this variable as required
    directory = 'Chapter_'
    
    # directory path where you want the new directories to be created
    path = ''

    # path of your source file
    input_file = ''

    # create multple new directories with sequencial names
    new_dir_seq(path, directory)

    # create multple new directories with different names from source file
    new_dir_multiple(path, input_file)

if __name__ == '__main__':
    main()
