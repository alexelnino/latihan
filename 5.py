#pip install pillow
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

# x=np.array([1,2,3,4,5])
# y=np.array([5,4,3,2,1])
# z=np.array([[2,5,4,1,3]])

# plt.figure('tes 3D plot')
# myplot = plt.subplot(111, projection = '3d')
# # myplot.plot_wireframe(x,y,z)
# myplot.scatter(x,y,z, color='green', marker='*', s=200)     #titik2
# myplot.set_xlabel('nilai X')
# myplot.set_ylabel('nilai Y')
# myplot.set_zlabel('nilai z')

# plt.show()

#membuat bar 3D
x=np.array([1,2,3,4,5])
y=np.array([5,4,3,2,1])
z1=np.zeros(5)

x1=np.ones(5)
y1=np.ones(5)
z=np.array([1,3,5,7,9])

plt.figure('tes 3D bar')
myplot = plt.subplot(111, projection = '3d')
myplot.bar3d(x,y,z1,x1,y1,z,
color=['red','blue','yellow','green','black'])
myplot.set_xlabel('nilai X')
myplot.set_ylabel('nilai Y')
myplot.set_zlabel('nilai z')
plt.show()