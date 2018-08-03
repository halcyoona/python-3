import numpy as np
x = np.linspace(0,10,40)
print (x)




c = np.cos(x)
print (c)


import matplotlib.pyplot as plt

#Only for jupyter notebook
#%matplotlib inline


plt.plot(x,c)


s = np.sin(x)
print(x)


plt.figure()
plt.plot(x,c)
plt.plot(x,s)



plt.figure()
plt.plot(x, c, label="cos")
plt.plot(x, s, label="sin")
plt.xlabel('x')
plt.ylabel('cos/sin')
plt.legend()
