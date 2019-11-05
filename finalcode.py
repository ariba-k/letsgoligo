from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.misc import imread


fig1 = plt.figure()

earthquakes_df = pd.read_csv('earthquakedata.csv')
latitude = earthquakes_df['Latitude']
longitude = earthquakes_df['Longitude']
mag = earthquakes_df['Magnitude']
depth = earthquakes_df['Focal_Depth']

plt.xlim([-180,180])
plt.ylim([-90,90])

img = imread("mapNASA.jpg")
plt.imshow(img, zorder=0, extent = [-180,180,-90,90])

sizes = []
colors = []
for i in mag:
  if i <= 5.0:
      sizes.append(10)
  elif i <= 5.5:
      sizes.append(15)
  elif i <= 6.0:
      sizes.append(20)
  elif i <= 6.5:
      sizes.append(25)
  elif i <= 7.0:
      sizes.append(30)
  elif i <= 7.5:
      sizes.append(35)
  elif i <= 8.0:
      sizes.append(40)
  elif i <= 8.5:
      sizes.append(45)    
  else:
       sizes.append(50)

for x in depth:
  if x <= 5.0:
      colors.append((0.49,0.68,1))
  elif x <= 10.0:
      colors.append((0.4,0.61,1))
  elif x <= 15.0:
      colors.append((0.3,0.55,1))
  elif x <= 20.0:
      colors.append((0.2,0.49,1))
  elif x <= 25.0:
      colors.append((0.1,0.42,1))
  else:
      colors.append((0,0.36,1))

plt.scatter(longitude,latitude,zorder=1,s = sizes,c = colors)
plt.imshow(img, zorder=0, extent = [-180,180,-90,90])

plt.show()

def on_key_press(event):
  plt_local = plt
  fig2 = plt.figure()
  if event.key == '1':
   img1 = imread('dog.jpg')
   plt_local.imshow(img1, zorder=0)
  elif event.key == '2':
   img2 = imread('dog2.jpg')
   plt_local.imshow(img2, zorder=0)
  elif event.key == '3':
   img3= imread('dog3.jpg')
   plt_local.imshow(img3, zorder=0)
  elif event.key == '4':
   img4= imread('dog4.jpg')
   plt_local.imshow(img4, zorder=0)

def quit_figure(event):
  if event.key == 'x':
    fig2.close(event.canvas.figure)
    plt.show(block=False)
    input("Hit Enter To Close")
    plt.close()


fig1.canvas.draw()
fig1.canvas.mpl_disconnect(fig1.canvas.manager.key_press_handler_id)
fig1.canvas.mpl_connect('key_press_event', on_key_press)
fig2.canvas.mpl_connect('key_press_event', quit_figure)


