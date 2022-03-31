# use open() function to access the file, specify the current working directory, the second argument 'r' opens the file in read only mode
'''
f = open('/Users/gabe_ung/Desktop/some_text_file.txt', 'r')
file_data = f.read() #read() method takes the contents of the file and puts it into a string
f.close() #always close a file after you have opened it to free up system resources

print(file_data)
'''

'''
f_1 = open('another_text_file.txt', 'w') #create new file: another_text_file.txt in write mode
f_1.write("Hello World") #write to the file that was just created
f_1.close()
'''
# use with key word to open a file, do operations on it, and automatically close it after the intented code is executed 
# in this case reading from the file. now we don't have to call f.close(). you can only access the file object, f, within this indented block
with open('/Users/gabe_ung/Desktop/some_text_file.txt', 'r') as f: 
    file_data = f.read()
print(file_data)
