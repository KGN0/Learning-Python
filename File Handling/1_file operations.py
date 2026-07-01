# Files
'''
- A file is a named location on disk to store related information. It is used to permanently store data in a non - volatile memory.
  Since RAM is volatile which loses data when computer is turns off, then we use files for future use of the data.

- When we want to read from a file or write to a file we need to open it first, when our work is completed we need to close the files'''

# File operations
# Opening a File
'''
Python has built-in function open() to open a file in current directory. This function creates a file object, which will be used to involve
methods associated with it
Syntax   :    file_object = open(file_name [, access_mode][,buffering])
file_name: The file_name argument is a string value that contians the name of the file that you want to access
           access_mode: The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc
buffering: If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file.
'''

# Example 

file_obj1 = open(r'.\File Handling\file1.txt', 'r')  # different ways to open file
file_obj2 = open('File Handling\\file1.txt', 'r')
file_obj3 = open('File Handling/file1.txt', 'r')
print(file_obj1)
print(file_obj2)
print(file_obj3)

# file opeing modes
'''
"r" = This mode is used to read data from the file
"w" = This mode is used to write data into file
"a" = This mode is used to append data to the existing file
"r+" = This mode is used to read and write data into a file
"w+" = This mode is used to write and read data of a file
"a+" = This mode is used to append and read data of a file
"x" = This mode is used to open the file in exclusive mode. It returns error if the file already exist
'''

# file objects attributes
'''Once a file is successfully opened, a file object is returned. Using this file object, 
you can easily acess different types of information related to that file
- fileobj.closed : bool indicating the current state of the file object
- fileobj.encoding : the encoding that file uses
- fileobj.mode : the I/O mode for the file
- fileobj.name : if the file object was created using open(), the name of the file. Otherwise some string that indicates the source of the file object'''

# Example
fileObj = open('File Handling/file1.txt', 'r')
print('\nName of file:', fileObj.name)
print('File closed:', fileObj.closed)
print('File is opened in:', fileObj.mode)
print('File encoding:', fileObj.encoding)

# Reading  and Writing files
# read([count])
'''The read method is used to read a string from an already opened file. The read method can read alphabets, numbers, characters, other symbols
Syntax: fileObj.read([count])  - count is optional and it specifies how many bytes or lines to be read from file'''
# Example
f1 = open('File Handling\\file1.txt', 'r')
content = f1.read()
print("\n",content, sep="")

# write(string)
'''The write method is used to write a string to an already opened file. This may include numbers, special characters or other symbols
Syntax: fileObject.write(string)'''
# Example
f2 = open('File Handling/file1.txt', "w")
line = '\nThis line is written by python program'
f2.write(line)


# closing a file
'''A opened file must be closed by using close() method'''
f2.close()


# Program showing writing / reading data to / from a file
f = open('File Handling/file1.txt', 'w')
line = input("Enter text: \n")
f.write(line)
f.close()

f = open('File Handling/file1.txt', 'r')
content = f.read()
print(content)