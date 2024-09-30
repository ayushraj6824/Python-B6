import pickle

# Data to pickle
list1 = [1, 2, 3, 4, 5, 6]

# Filename to store the pickled data
fileName = "Data.pickle"

# Pickle the data and write to file
with open(fileName, "wb") as file:
    pickle.dump(list1, file)

# Now read the pickled data from the file
with open(fileName, "rb") as file:
    
    loaded_data = pickle.load(file)

print("Deserialized data:", loaded_data)
