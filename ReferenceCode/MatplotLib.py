import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Lena.png',0)
print(img.shape)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
