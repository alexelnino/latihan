import numpy as np
from matplotlib import pyplot as plt
#3x + 2y = 12

# titik potong pers dg sb y (x = 0) => 2y = 12
# |2| |y| = |12|
a = np.array ([[2]])
b=np.array ([12])
c=np.linalg.solve(a,b)

# titik potong pers dg sb y (y = 0) => 3x = 12
# |3| |y| = |12|
d=np.array([[3]])
e=np.array([12])
f=np.linalg.solve(d,e)

print(f)

titik1=np.array([0,c])
titik2=np.array([f,0])

plt.plot(titik1,titik2)
plt.show()