# #memunculkan gambar
# import matplotlib.pyplot as plt
# import matplotlib.image as mimg

# gambar = mimg.imread('1.jpg')
# print(gambar)

# gbrplot=plt.imshow(gambar)
# plt.show()

# pip install pillow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#black/white = 'L' / 'RGBA' / 'CMYK'
gambar = Image.open('1.jpg').convert('L')
gambar = np.array(gambar)
print(gambar)

# plt.imshow(gambar,cmap='gray')
# plt.show()
gbr=Image.fromarray(gambar, 'L')
gbr.show()

plt.savefig('1.png')