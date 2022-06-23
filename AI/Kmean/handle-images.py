import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

img = plt.imread("tree.jpg") #Read image or import cv -> cv.imread()
print("img")
print(img)
#img.shape -> (h,w,k)
height = img.shape[0]
width  = img.shape[1]

img = img.reshape(width*height, 3)
print("img reshape")
print(img)
kmeans = KMeans(n_clusters=20).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_
print("label")
print(labels)
print("cluster")
print(clusters)

img2 = numpy.zeros_like(img)
print("img2")
print(img2)
for i in range(len(img2)):
	img2[i] = clusters[labels[i]]

img2 = img2.reshape(height,width,3)

plt.imshow(img2)
plt.show()