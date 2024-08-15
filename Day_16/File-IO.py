f = open('myfile.txt',"a")

# text = f.read() # this is to read
text = f.write(" Good working")  # this is to write.

print(text)
f.close()


# Using with Statement

# The with statement is a better way to handle file operations because it ensures that the file is properly closed after its suite finishes, even if an exception is raised.

# with open('example.txt', 'r') as file:
#     content = file.read()



# Reading from a File
# You can read from a file using methods like read(), readline(), or readlines().


# read(size): Reads up to size bytes from the file. If no size is provided, it reads the entire file.
# readline(): Reads one line at a time.
# readlines(): Reads all lines and returns them as a list.