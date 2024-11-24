#pip install matplotlib
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
'''or
import matplotlib.pyplot as plt'''
start=1
end=1*60*60  #36000
noOfPoints = 3600
x=np.linspace(start,end,noOfPoints)

pi=22/7
omega=int(input("enter frequency"))


Y = 2 * pi * omega * x

Y2 = np.sin(Y)   
print(Y2)

plt.plot(x,Y2)
plt.xlabel("time($s$)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
#plt.savefig("filename")