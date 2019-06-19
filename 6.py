#pip install seaborn
#menggunakan seaborn.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

dataku = sn.load_dataset('flights')
data = dataku.pivot('month', 'year', 'passengers')
print(dataku)

# sn.lmplot(
#     x='year',
#     y='passengers',
#     data=dataku,
#     hue='month'
#     )      #hue untuk warna
# plt.show()

plt.figure('nomor 1')
sn.heatmap(data, cmap='BuPu_r')       #_r =>warnanya di reverse

plt.figure('nomor 2')
sn.heatmap(data, cmap='BuPu')
plt.show()

# sn.swarmplot(x='year', y='passengers', data=dataku)
# plt.xtickts(rotation=90)
# plt.show()