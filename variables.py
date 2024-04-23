x =10
print(x)
print(type(x))

x = .8 + 10
print(x)
print(type(x))

x = "Seattle " + "12"
print(x)
print(type(x))

y=3.5 ; print(y)

a,b,d,f,g,h = 1,2,4,"Walla Walla","Texas",1+2j
print(f)
print(g)
print(h)

print(4//5)

print(len("Texas"))

name = "IT 111 Fundamentals of Programming"
print(name)
print(len(name))
print(type(name))

a=2
if a<0:
    print("a is negative")
elif a<5 and a%2==0:
    print("a is less than 5 and a is an even number")
elif a==5:
    print("a is equal to 5")
else:
    print("a is greater than 5")

# f = open("test-file.txt", "x")

f = open("Project2Input.txt", "r")
print(f.read())

f = open("Project2Input.txt", "a")
f.write("\nPython is widely used for system administration such as managing servers and automating tasks.")
f.close()

import os
os.rename("Project2Input.txt", "Project2Update.txt")

import os
os.remove("Project2Update.txt")

# f = open("test-file.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f = open("test-file.txt", "w")
# f.write("Updating the text in the file. \nSome of the applications of Python include scripting, data analysis and automation.")
# f.close()

# import os
# os.remove("test-file.txt")

