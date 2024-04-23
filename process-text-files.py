# Write a Python program that performs the following task:

# 1. Opens a given file for appending
# 2. Lets the user add text to the file through command line input
# 3. Saves a copy of the file with a different file name
# 4. Deletes the original file


f = open("Project2Input.txt", "a")
f.write("\nPython is widely used for system administration such as managing servers and automating tasks.")
f.close()


import os
os.rename("Project2Input.txt", "Project2Update.txt")


import os
os.remove("Project2Update.txt")
