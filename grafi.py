import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3])
y=np.array([1,2,4])
y2=np.array([4,5,6])
plt.figure(1)
plt.plot(x,y)
plt.savefig('1.png')
plt.figure(2)
plt.plot(x,y2)
plt.savefig('2.png')
print('done')

from read_img import read_pgm, showImage
znj=40
I0= read_pgm("taxi/taxi{:02}.pgm".format(znj), byteorder='<')
I0=I0.astype('float')
showImage(I0)