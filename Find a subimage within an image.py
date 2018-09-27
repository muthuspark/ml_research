
# coding: utf-8

# In[5]:


# from skimage.feature import match_template
# from skimage.io import imread

# sub_image = imread('resources/smaller.jpg')
# template = imread('resources/puppy.jpg')

import cv2
from cv2 import cv
import matplotlib.pyplot as plt

method = cv.CV_TM_SQDIFF_NORMED

# Read the images from the file
#small_image = cv2.imread('resources/smaller.jpg')
small_image = cv2.imread('resources/sub_font.png')
large_image = cv2.imread('resources/biggerimage.png')

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
plt.imshow(large_image)
plt.show()

