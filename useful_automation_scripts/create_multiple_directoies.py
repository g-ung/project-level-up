#! python 3
'''
Create Multiple New Diretories
Edit the block of code inside the for loop
as required
'''
import os

def main():
    # change to the diretory where you want to create your new directories
    path = '/Users/gabe_ung/Desktop/Projects/project-level-up/automate-the-boring-stuff-with-python-SOLUTIONS'
    os.chdir(path) 
   
    # dircectory name/directory prefix, change this variabl as required
    directory = 'Chapter_'
    # check with
    #print(dir(os))
    #print('Current working directory: ', os.getcwd())

    # use range to specify how many directories you need created
    count = 0
    for i in range(8, 21):
        os.mkdir(directory + str(i))
        count += 1
    
    print('Directories created, {} directories created in {}'.format(count, path))

if __name__ == '__main__':
    main()