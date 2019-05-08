import numpy as np
from read_img import read_pgm

I0= read_pgm("taxi/taxi01.pgm", byteorder='<')
I0=I0.astype('float')
I1 = read_pgm("taxi/taxi02.pgm", byteorder='<')
I1=I1.astype('float')

NRows,NCols=I0.shape
Ix=np.zeros(I0.shape, dtype='float')
Iy=np.zeros(I0.shape, dtype='float')
It=np.zeros(I0.shape, dtype='float')

evenU=np.zeros(I0.shape, dtype='float')
evenV=np.zeros(I0.shape, dtype='float')
oddU=np.zeros(I0.shape, dtype='float')
oddV=np.zeros(I0.shape, dtype='float')
for y in range(NRows):
  for x in range(NCols):
    #Ix
    if (y==NRows-1) and (x==NCols-1): #če gre čez rob dam ničle
      Ix[y][x]= - 1/4*(I0[y][x]+I1[y][x])
      Iy[y][x]= - 1/4*(I0[y][x]+I1[y][x])
      It[y][x]= 1/4*(I1[y][x]) - 1/4*(I0[y][x])
    elif (y==NRows-1):
      Ix[y][x]= 1/4*(I0[y][x+1] + I1[y][x+1] + 0+0) - 1/4*(I0[y][x]+I1[y][x]+0+0)
      Iy[y][x]= - 1/4*(I0[y][x]+I1[y][x]+I0[y][x+1]+I1[y][x+1])
      It[y][x]= 1/4*(I1[y][x]+I1[y][x+1]) - 1/4*(I0[y][x]+I0[y][x+1])
    elif (x==NCols-1):
      Ix[y][x]= 1/4*(0+ 0 + 0+0) - 1/4*(I0[y][x]+I1[y][x]+I0[y+1][x]+I1[y+1][x])
      Iy[y][x]= 1/4*(I0[y+1][x] + I1[y+1][x] ) - 1/4*(I0[y][x]+I1[y][x])
      It[y][x]= 1/4*(I1[y][x]+I1[y+1][x]) - 1/4*(I0[y][x]+I0[y+1][x])
    else:
      Ix[y][x]= 1/4*(I0[y][x+1] + I1[y][x+1] + I0[y+1][x+1]+I1[y+1][x+1]) - 1/4*(I0[y][x]+I1[y][x]+I0[y+1][x]+I1[y+1][x])
      Iy[y][x]= 1/4*(I0[y+1][x] + I1[y+1][x] + I0[y+1][x+1]+I1[y+1][x+1]) - 1/4*(I0[y][x]+I1[y][x]+I0[y][x+1]+I1[y][x+1])
      It[y][x]= 1/4*(I1[y][x]+I1[y+1][x]+I1[y][x+1]+I1[y+1][x+1]) - 1/4*(I0[y][x]+I0[y+1][x]+I0[y][x+1]+I0[y+1][x+1])


lamb=0.1
T=9
n=0
while n<=T:
  for y in range(NRows):
    for x in range(NCols):
      if (n%2==1): #odd- preprečim prepisovanje podatkov
        #levi desni gornji spodnji za u
        lu=0 if x==0 else evenU[y][x-1]
        du=0 if x==NCols-1 else evenU[y][x+1]
        gu=0 if y==0 else evenU[y-1][x]
        su=0 if y==NRows-1 else evenU[y+1][x]

        #levi desni gornji spodnji za v
        lv=0 if x==0 else evenV[y][x-1]
        dv=0 if x==NCols-1 else evenV[y][x+1]
        gv=0 if y==0 else evenV[y-1][x]
        sv=0 if y==NRows-1 else evenV[y+1][x]

        u_=1/4*(lu+du+su+gu) #povprečje okoliških štirih
        v_=1/4*(lv+dv+sv+gv)

        alfa=(Ix[y][x]*u_+Iy[y][x]*v_  + It[y][x])/(lamb**2+(Ix[y][x])**2+(Iy[y][x])**2)
        oddU[y][x]=u_ - Ix[y][x]*alfa
        oddV[y][x]=v_ - Iy[y][x]*alfa
      else: #even
        #levi desni gornji spodnji za u
        lu=0 if x==0 else oddU[y][x-1]
        du=0 if x==NCols-1 else oddU[y][x+1]
        gu=0 if y==0 else oddU[y-1][x]
        su=0 if y==NRows-1 else oddU[y+1][x]

        #levi desni gornji spodnji za v
        lv=0 if x==0 else oddV[y][x-1]
        dv=0 if x==NCols-1 else oddV[y][x+1]
        gv=0 if y==0 else oddV[y-1][x]
        sv=0 if y==NRows-1 else oddV[y+1][x]

        u_=1/4*(lu+du+su+gu) #povprečje okoliških štirih
        v_=1/4*(lv+dv+sv+gv)

        alfa=(Ix[y][x]*u_+Iy[y][x]*v_  + It[y][x])/(lamb**2+(Ix[y][x])**2+(Iy[y][x])**2)
        evenU[y][x]=u_ - Ix[y][x]*alfa
        evenV[y][x]=v_ - Iy[y][x]*alfa
  n=n+1
#print(Ix,Iy,It)
#print(oddU,oddV)