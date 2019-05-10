import re
import numpy
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as im
import matplotlib.pyplot as plt
import matplotlib.cm as cm # uvozi barvne lestvice
from read_img import read_pgm, showImage
znj=40
I0= read_pgm("taxi/taxi{:02}.pgm".format(znj), byteorder='<')
I0=I0.astype('float')
print(I0.astype('uint8'))
showImage(I0)

plt.figure()

plt.imshow(I0.astype('uint8'))
