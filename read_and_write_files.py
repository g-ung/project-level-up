# use open() function to access the file, specify the current working directory, the second argument 'r' opens the file in read only mode
f = open('/Users/gabe_ung/Desktop/some_text_file.txt', 'r')
file_data = f.read() #read() method takes the contents of the file and puts it into a string
f.close() #always close a file after you have opened it to free up system resources

print(file_data)

f_1 = open('another_text_file.txt', 'w') #create new file: another_text_file.txt in write mode
f_1.write("Hello World")
f_1.close()