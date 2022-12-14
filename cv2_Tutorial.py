
import statistics
import random
import matplotlib.pyplot as plt
import datetime as datetime
import csv
import numpy as np
import cv2 as cv

############################# plotting shit ############################

data1 = [random.randrange(0, 100) for i in range(1, 10)] # 10 data points in range 1 to 100
data2 = [random.randrange(0, 100) for i in range(1, 10)] # 10 data points in range 1 to 100

plt.subplot(2, 2, 3)
plt.subplot(2, 2, 3)

plt.plot(data1, data2)
plt.plot(data2, data1, color="red")
#plt.show()

############################ actual cv2 meme time ############################


# upload an image

name = 'Anime Love.jpg'
img = cv.imread(name)
print(img.shape)

cv.imshow("Image of Anime", img)
cv.waitKey(0)
cv.destroyAllWindows()


img_new = img.copy()

# blur 

frame = cv.GaussianBlur(img_new, (3, 3), 13)
cv.imshow('frame blurred', frame)
cv.waitKey(0)
cv.destroyAllWindows()

# repeatedly sharpen image

for i in range(10):
  frame = cv.GaussianBlur(img_new, (3, 3), 13)
  img_new = cv.addWeighted(img_new, 1.5, frame, -0.5, 0)

cv.imshow('sharp', img_new)
cv.waitKey(0)
cv.destroyAllWindows()

# add red contrast

alpha = 2.2
beta = 50
b, g, r = cv.split(img_new)
r = r*alpha + beta
r = r.astype(np.uint8)
r = np.clip(r, 0, 255) # make sure all values are within this range
img_new = cv.merge((b, g, r))

cv.imshow('Deep Fried', img_new)
cv.waitKey(0)
cv.destroyAllWindows()

# edge manipulation

edges = cv.Canny(img, 50, 50)
red_edges = np.zeros(img.shape)
red_edges[:, :, 2] = edges # get only red color for edges
red_edges = red_edges.astype(np.uint8)
img = cv.addWeighted(img, 0.5, red_edges, 0.5, 0)

# make brighter

img = img * 1.5 + 50
img = img.astype(np.uint8) # cast type properly

cv.imshow('red edges', red_edges)
cv.waitKey(0)
cv.destroyAllWindows()