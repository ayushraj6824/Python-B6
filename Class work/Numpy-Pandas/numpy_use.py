import numpy as np
'''x=np.linspace(1,10,100)
print(x)'''

'''np.linspace is a function in NumPy that generates an array of evenly 
spaced values over a specified interval. It’s particularly useful 
for creating sequences of numbers with a specified start and end, 
along with the number of elements you want in between.'''
#np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

start=1
end=1*60*60  #36000
noOfPoints = 3600
x=np.linspace(start,end,noOfPoints) #x axis or time
#len(x)
#print(x)

pi=22/7
omega=10


Y=2 * pi * omega * x

Y2 = np.sin(Y)
print(Y2)