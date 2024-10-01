#1. Write a program to read - list and dictionary using the pickle module. 

import pickle


list1 = [1, 2, 3, 4, 5, 6]

# Filename to store the pickled data
fileName = "Data.pickle"

# Pickle the data and write to file
with open(fileName, "wb") as file:
    pickle.dump(list1, file)

#  Read the pickled data from the file
with open(fileName, "rb") as file:
    
    loaded_data = pickle.load(file)

print("Deserialized data:", loaded_data)


# fileHandle = open(fileName, "wb")
# pickle.dump(list1, fileHandle)
# fileHandle.close()
# try: 
#     with open(fileName,"wb") as fileHandle:
#         pickle.dump(list1, fileHandle)
#     print("Object Save Successfully")
# except:
#     print("Error Occured Saving Object")