file_path = "/root/hey_im_learning_python/practice/file.txt"   #specify the file path 

try:

    file = open(file_path, "r")     #open the file and read (r stands for read)
    
    content = file.read()       # read the entire file at once

    print (f"The file contains: {content}")

    file.close()        #close the file

except FileNotFoundError:
    print(f"The file {file_path} doesn't exist!")
except PermissionError:
    print(f"You don't have permission to access {file_path}!")



