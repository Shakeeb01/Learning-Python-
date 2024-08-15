import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List all files and directories in the current directory
print(os.listdir(cwd))

# Create a new directory
os.mkdir('new_folder')
