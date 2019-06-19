import matplotlib.pyplot as plt
import numpy as np

x=np.arange(5)
y=np.array([0,1,2,3,4])
print(y)
print(type(y))
z=2*y

# plt.plot(x,y,x,z)
# plt.plot(x,y,'r-',x,z,'g--')

# plt.plot(x,y,'r-')      #=> kalau seperti ini akan memunculkan 2 grafik di dalam satu figure. sama seperti yang di atas
# plt.plot(x,z,'g--')

# # membuat 2 figure di dalam sekali run
# #fig 1
# plt.figure('nomor 1')
# plt.plot(x,y,'r-')
# plt.grid(True)
# plt.title('fig 1')
# plt.xlabel('nilai X')
# plt.ylabel('nilai Y')
# plt.legend(['hubungan XY'])


# #fig 2
# plt.figure('nomor 2')
# plt.plot(x,y,'g--')
# plt.grid(True)
# plt.title('fig 2')
# plt.xlabel('nilai X')
# plt.ylabel('nilai Z')
# plt.legend(['hubungan XZ'])
# plt.show()

# # membuat 2 plot di dalam 1 figure 
# plt.figure('ini grafik nomor 1', figsize=(10,5))
# #plot 1
# plt.subplot(1,2,1)          #atau plt.subplot(2,1,1) dicoba aj sendiri biar tau bedanya. (1,2,1 => p, l, urutan ke-n)
# plt.plot(x,y,'r-')
# plt.grid(True)
# plt.title('fig 1')
# plt.xlabel('nilai X')
# plt.ylabel('nilai Y')
# plt.legend(['hubungan XY'])


# #plot 2
# plt.subplot(1,2,2)      #plt.subplot(2,1,2)
# plt.plot(x,y,'g--')
# plt.grid(True)
# plt.title('fig 2')
# plt.xlabel('nilai X')
# plt.ylabel('nilai Z')
# plt.legend(['hubungan XZ'])
# plt.show()

# #untuk membuat titik =>(.scatter)
# # plt.scatter(x,y,color='b')
# plt.scatter(x,y, color='b', marker='*', s=1000)
# plt.plot(x,y,color='r')
# plt.show()

# # membuat diagram batang
# plt.bar(x,y)
# plt.show()

# plt.bar(x,y, color='b')
# plt.bar(x,y, color='r', bottom=y)
# plt.show()

# #membuat histogram
# plt.hist(y,x)
# plt.hist(y,x,histtype='bar',rwidth=.5)      #=>tipe histogram = bar. lebar =5
# plt.show()

#diagram lingkaran / pie chart
warna=['r','orange','y','g','b']
plt.pie(x, labels=x, startangle=180, colors=warna,
shadow=True, explode=(0 , 0.1 , 0 , 0.2 , 0),
autopct='%1.1f%%', textprops={'color':'w'}
)
plt.legend(x)
plt.show()
plt.savefig('1.png')