from turtle import width
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

img = plt.imread("tree.jpg")
 
height = img.shape[0]
width = img.shape[1]

print(img.shape)
img = img.reshape(width*height,3)


kmeans = KMeans(n_clusters=3).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

print(labels)
print(clusters)

img2 = numpy.zeros((height,width,3), dtype=numpy.uint8)

index = 0
for i in range(height):
	for j in range(width):
		label_of_pixel = labels[index]
		img2[i][j] = clusters[label_of_pixel]
		index += 1

print(img2)
# plt.imshow(img2)
# plt.show()

