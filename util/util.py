#utility methods
####################################
#find the centroid of vertices

def centroid(vertexes):
    _x_list = [vertex [0] for vertex in vertexes]
    _y_list = [vertex [1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return(_x, _y)

for contour in contours:
    print centroid(contour)

####################################

#find contours
from skimage import measure

# Find contours at a constant value of 0.8
contours = measure.find_contours(image, 0.8)


####################################

#add a padding of about 10 points around the imageself.
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector

image = np.pad(image, 10, pad_with, padder=1)

####################################

#division to give float instead of int.
from __future__ import division
#so how much is it scaled?

scaled_factor = template_img.shape[0]/sample_image.shape[0]
print scaled_factor


####################################
#distance between two points
#https://shapely.readthedocs.io/en/stable/manual.html
from shapely.geometry import Point

Point(0,0).distance(Point(1,1))
