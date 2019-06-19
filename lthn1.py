import numpy as np

x=[1,2,3,4,5]
y=[5,4,3,2,1]

X=np.array(x)
print(X)
print(X[3])
print(type(X))

z=np.arange(50,100,2)
print(z)
print(z[0])
print(z[-1])
print(z[5::2])
print(z.ndim)           #ndim=untuk menunjukkan banyaknya dimensi
print(len(z))
print(z.size)           #untuk menunjukkan jumlah elemen
print(z.itemsize)       #satuan ny bytes
print(z.dtype)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()