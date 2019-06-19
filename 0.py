# matplotlib.org
# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

# x=[0,1,2,3,4,5,6,7,8,9]
# y=[1,4,6,7,4,3,6,2,1,5]

# plt.plot(x,y)
# plt.title('tes Matplotlib')     #memberikan title
# plt.xlabel('nilai x')           #memberikan nama di x
# plt.ylabel('nilai y')           #memberikan nama di y
# plt.grid(True)                  #memberikan grid
# plt.legend(['dataku'])          #memberikan nama di garis grafik nya

# plt.show()

x=np.arange(10)
y=np.array([1,4,6,7,4,3,6,2,1,5])

# plt.plot(x,y,'r--',linewidth=3)               
plt.plot(x,y*2,color='green',linestyle='-')
plt.plot(x,y*3,'b')
# plt.xticks(rotation=90)     #merotasi angka di grafik nya
plt.yticks(rotation=90)
# plt.plot(x,y,'g--',x,y*2,'b^',x,y*3,'r.')
#=>'r' / 'g' / 'b' / 'y' = warna garis
# untuk warna garis, bisa juga plt.plot(x,y,color='red) atau color='#7ffd4
#  '--' untuk garis putus-putus
# - = line
# -- = dash
# o = point
# s = square
# ^ = segitiga
# * = Star
# . = dot

for titik in x:
    plt.text(titik-.1,y[titik]-.2,y[titik])

# plt.plot(x,y,'r*')

#memberikan background style pada grafik
print (plt.style.available)     #melihat background yang ada
# plt.style.use('seaborn')

plt.annotate(
    'Nilai tertinggi', xy=(3,21), xytext=(4,20),
    arrowprops=dict(facecolor='blue',shrink=.2)
)


# save grafik
# plt.savefig('inigrafikku.jpg)

# adjust letak garis
plt.subplots_adjust(
    left=.14, bottom=.14, right=.95, top=.88, wspace=.2, hspace=.2
)

plt.plot(x,y,
    color='pink',linestyle='-',linewidth=3)
plt.fill_between(x,y[3],0,facecolor='y',alpha=.3)

plt.title('tes Matplotlib')     #memberikan title
plt.xlabel('nilai x')           #memberikan nama di x
plt.ylabel('nilai y')           #memberikan nama di y
plt.grid(True)                  #memberikan grid
plt.legend(['x-y','x-y*2','x-y*3'], loc=2)          #memberikan nama di garis grafik nya. loc= lokasi nama garis nya(0-10). kalau 0 defaultnya pojok kanan atas 

plt.show()