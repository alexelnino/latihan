import matplotlib.pyplot as plt
import numpy as np
import csv

# x, y = np.loadtxt(
#     'data.csv',
#     delimiter=',',
#     unpack=True
# )

# print(x)
# print(y)
# plt.plot(x,y)
# plt.show()

x=[]
y=[]
with open('data.csv','r') as dataku:
    data = csv.reader(dataku)
    for i in data:
        x.append(int(i[0]))
        y.append(int(i[1]))

print(x)
print(y)
plt.plot(x,y)
plt.show()