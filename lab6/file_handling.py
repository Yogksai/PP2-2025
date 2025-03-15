import os
f = open("file_handling.txt") #by default it is read mode
print(f.read()) #reads the whole file
print(f.read(5)) #reads the first 5 characters
print(f.readline()) #reads the first line
print(f.readline()) #reads the second line
for line in f:
    print(line)
f.close() #closes the file



f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read()) 

f = open("demofile3.txt", "x")

#deleting a file
if os.path.exists("demofile3.txt"):
  os.remove("demofile3.txt")
else:
  print("The file does not exist") 

#deleting a folder
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The folder does not exist")