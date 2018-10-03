
# coding: utf-8

# In[ ]:


# from skimage.feature import match_template
# from skimage.io import imread

# sub_image = imread('resources/smaller.jpg')
# template = imread('resources/puppy.jpg')

import cv2 as cv
import matplotlib.pyplot as plt

method = cv.TM_CCOEFF_NORMED

# Read the images from the file
small_image = cv.imread('resources/smaller.png')
small_image = cv.imread('resources/boxsf.png')
large_image = cv.imread('resources/biggerimage.png')
large_image = cv.imread('resources/sf3.png')

result = cv.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
# cv.imshow('output',large_image)
cv.imwrite('output.png',large_image)
# plt.imshow(large_image)

