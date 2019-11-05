import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from struct import unpack
%matplotlib inline

bod_num=[]
mass=[]
time=[]
ax=[]
ex=[]
inc=[]
x=[]
y=[]
z=[]

#Set Up Data
f = open("/Users/aribakhan/Documents/BH_nbody/OutputData/May22/bout.bin", "rb")
num=17 #number of columns
vals=[1,2,3,4,5]
while len(vals)>0:
    vals = f.read(4*num)
    if len(vals)>0:
        bod_num.append(unpack('f'*num,vals)[1])
        mass.append(unpack('f'*num,vals)[2])
        time.append(unpack('f'*num,vals)[3]/365.2)
        ax.append(unpack('f'*num,vals)[4])
        ex.append(unpack('f'*num,vals)[5])
        inc.append(unpack('f'*num,vals)[6])
        x.append(unpack('f'*num,vals)[10])
        y.append(unpack('f'*num,vals)[11])
        z.append(unpack('f'*num,vals)[12])
    if unpack('f'*num,vals)[3]>1e7:
        break  
f.close()

#Set Up Variables
x=np.array(x)
y=np.array(y)
z=np.array(z)
bod_num=np.array(bod_num)
mass=np.array(mass)
time=np.array(time)
ax=np.array(ax)
ex=np.array(ex)
r=np.sqrt(x**2+y**2+z**2) #calculating radial hill

lsize=26

fig=plt.figure(figsize = (30,4))#initiates a figure

colors = [(1, 0, 0), (1, 0.749, 0), (1, 1, 0), (0.749, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1),(0.749, 0, 1), (1, 0, 0.749),(0.525, 0.475, 0.475)]
colors = np.array(colors)
m = 665

#----------------------------------------------------------------------------------------------------------------------
#First Subplot
plt.subplot(1,5,1)
plt.plot()
plt.title("$40M_{\odot}$ at 0 Years",fontsize=lsize)
plt.ylim(-0.06,0.12)
plt.xlim(400,1000)
plt.ylabel('Eccentricity',fontsize=lsize)
plt.gca().tick_params(labelsize=lsize)
for i in range(25): #range is a list of numbers from 0 to 24 (so 25 numbers total)
    axvline(m, color = 'k', linewidth=1, dashes = (3,3))
    axhline(0, color = 'k', linewidth=1, dashes = (3,3))
    obj=bod_num==i#boolean indexing
    time0 = time[obj]>0
    if sum(time0)!=0:
        plt.plot(ax[obj][time0][0],ex[obj][time0][0], ".",ms=mass[obj][time0][0],alpha=0.3,c=colors[i])
    else: 
        plt.plot(2000,1.20)
#----------------------------------------------------------------------------------------------------------------------
#Second Subplot
plt.subplot(1,5,2)
plt.plot()
plt.title("$40M_{\odot}$ at 1000 Years", fontsize=lsize)
plt.gca().tick_params(labelsize=lsize)
plt.ylim(-0.06,0.12)
plt.xlim(400,1000)
for i in range(25): #range is a list of numbers from 0 to 24 (so 25 numbers total)
    axvline(m, color = 'k', linewidth=1, dashes = (3,3))
    axhline(0, color = 'k', linewidth=1, dashes = (3,3))
    obj=bod_num==i#boolean indexing
    time0 = time[obj]>10**3
    if sum(time0)!=0:
        plt.plot(ax[obj][time0][0],ex[obj][time0][0], ".",ms=mass[obj][time0][0],label="%d"%i,alpha=0.3,c=colors[i])
    else: 
        plt.plot(2000,1.20)
#----------------------------------------------------------------------------------------------------------------------
#Third Subplot
plt.subplot(1,5,3)
plt.plot()
plt.title("$40M_{\odot}$ at 2500 Years",fontsize=lsize)
plt.gca().tick_params(labelsize=lsize)
plt.ylim(-0.06,0.12)
plt.xlim(400,1000)
for i in range(25): #range is a list of numbers from 0 to 24 (so 25 numbers total)
    axvline(m, color = 'k', linewidth=1, dashes = (3,3))
    axhline(0, color = 'k', linewidth=1, dashes = (3,3))
    obj=bod_num==i#boolean indexing
    time0 = time[obj]>2511.88
    if sum(time0)!=0:
        plt.plot(ax[obj][time0][0],ex[obj][time0][0], ".",ms=mass[obj][time0][0],label="%d"%i,alpha=0.3,c=colors[i])
    else: 
        plt.plot(2000,1.20)
#----------------------------------------------------------------------------------------------------------------------
#Fourth Subplot
plt.subplot(1,5,4)
plt.plot()
plt.title("$40M_{\odot}$ at 10000 Years",fontsize=lsize)
plt.gca().tick_params(labelsize=lsize)
plt.ylim(-0.06,0.12)
plt.xlim(400,1000)
for i in range(25): #range is a list of numbers from 0 to 24 (so 25 numbers total)
    axvline(m, color = 'k', linewidth=1, dashes = (3,3))
    axhline(0, color = 'k', linewidth=1, dashes = (3,3))
    obj=bod_num==i#boolean indexing
    time0 = time[obj]>6309.57
    if sum(time0)!=0:
        plt.plot(ax[obj][time0][0],ex[obj][time0][0], ".",ms=mass[obj][time0][0],label="%d"%i,alpha=0.3,c=colors[i])
    else: 
        plt.plot(2000,1.20)
#----------------------------------------------------------------------------------------------------------------------        
#Fifth Subplot
plt.subplot(1,5,5)
plt.plot()
plt.title("$40M_{\odot}$ at 16000 Years",fontsize=lsize)
plt.gca().tick_params(labelsize=lsize)
plt.ylim(-0.06,0.12)
plt.xlim(400,1000)
for i in range(25): #range is a list of numbers from 0 to 24 (so 25 numbers total)
    axvline(m, color = 'k', linewidth=1, dashes = (3,3))
    axhline(0, color = 'k', linewidth=1, dashes = (3,3))
    obj=bod_num==i#boolean indexing
    time0 = time[obj]>15848.93
    if sum(time0)!=0:
        plt.plot(ax[obj][time0][0],ex[obj][time0][0], ".",ms=mass[obj][time0][0],label="%d"%i,alpha=0.3,c=colors[i])
    else: 
        plt.plot(2000,1.20)


plt.tight_layout()
plt.savefig('May22_Plots/10body_may22growth.png')

