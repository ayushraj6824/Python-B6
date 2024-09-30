# wAP save a list object into a file and read that same file and recover as a list without using pickle module

filePath = "listData.txt"
data=[1,2,3,4]

with open(filePath,"w") as fileHandle:
    fileHandle.write(str(data))



# read the same file and recover data as list 
with open(filePath,"r") as fileHandle:
    readData = fileHandle.read()
    print()