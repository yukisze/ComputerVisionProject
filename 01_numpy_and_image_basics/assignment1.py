# import numpy
import numpy as np

# Create and print a 3 by 3 array where every number is a 15
arr_1 = np.full((3,3),15)
print(arr_1)
# print out what are the largest and smalled values in the array below
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
largest = arr.max()
smallest = arr.min()
print("the min value is {} and the max value is {}".format(smallest,largest))

# import pyplot lib from matplotlib and Image lib from PIL
import matplotlib.pyplot as plt
from PIL import Image

# use PIL and matplotlib to read and display the ../data/zebra.jpg image
image = Image.open(r'C:\Users\User\Documents\cv_bootcamp\data\zebra.jpg')
#image.show()
image_mat = plt.imread(r'C:\Users\User\Documents\cv_bootcamp\data\zebra.jpg')
#plt.show()
# convert the image to a numpy array and print the shape of the arrary
image_array = np.array(image)
print(image_array.shape)
image_mat_array = np.array(image_mat)
print(image_mat_array.shape)
# use slicing to set the RED and GREEN channels of the picture to 0, then use imshow() to show the isolated blue channel
image_array[:,:,0] = 0
image_array[:,:,1] = 0
print(image_array)
plt.imshow(image_array)
plt.show()
