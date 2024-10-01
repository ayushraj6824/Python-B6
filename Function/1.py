def counter():

    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter()

print(counter1())  
print(counter1())  

counter2 = counter()
print(counter2())  
