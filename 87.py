from skimage import io
import matplotlib.pyplot as plt
import math

def posterize(image):
    rows,cols,dims=image.shape
    for i in range(0,rows):
        for j in range(0,cols):
            for k in range(0,3):
                color = image[i,j,k]
                image[i,j,k] = math.floor(color/64)*64+31
    return image
img=io.imread('scene.jpg')
io.imshow(img)
img2 = posterize(img)
plt.figure()
io.imshow(img2)
io.show()