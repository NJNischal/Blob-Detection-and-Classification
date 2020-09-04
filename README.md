# Blob-Detection-and-Classification

## Problem statement:
Refer to the q1_init.py script, the 114 images in q1/blob_set/, and the q1/query_blob.png image to create a Python script that returns the most and least similar blobs in the blob_set to the query image.

## Approach:
From the blobs found in the folder, these are the features that can be extracted: 
1) Area
2) Perimeter
3) Circularity
4) Moment
5) Convexity, 
6) Aspect ratio

Area: The area of the blob is calculated using contourArea from OpenCV, This is used to
calculate the area using the extracted contours from the image.

Perimeter: The perimeter of the blob is calculated using arcLength from OpenCV, This is used
to calculate the perimeter using the extracted contours from the image. Here, I use ‘True’ as the
parameter to signify that the blob is a closed contour.

Circularity: Circularity describes how close to a circle the observed blob is. The ‘fuller’ the circle,
the closer the value is to 1. The Circularity can be computed with :
circularity=4(pi)(area)/(perimeter)^2

Moment: Moment can be used to calculate the centroid of the blob. Moment can be used to
compute the x,y coordinates of the centroid of the blob using:

```
cx = M['m10'] / M['m00']
cy = M['m01'] / M['m00']
```
This is not useful here as most of the blobs are located in the center of the image and this can
not be used as a feature to distinguish between the blobs.
Convexity: This is used to find if the shape is convex. I found this feature not to be of much help
as it was always returning false, meaning, the shape is always non-convex. This is because at
the pixel level, it is hard to achieve convexity due to pixelation where the curves do not translate
as smooth curves in an image but as an arrangement of discrete pixels.
Aspect ratio: For aspect ratio, I fit the least possible bounding rectangle to the blob and
calculated the ratio of length to breadth. This is an important feature as it defines how symmetric
the shape of the blob is.
I have used cv2.findContours to extract contours from the blobs. Contour is a curve joining all
the continuous points along the boundary. The contours are quite useful for shape and feature
analysis.
Of the features above I have only considered Area, Circularity and Aspect Ratio as the features
used to evaluate the blobs from the blob set folder. The reason for this is, the other features are
either a product of the other features or are not varying within this dataset, thus deemed to be
not useful for the required classification task.

## Requirements/ Dependencies:

OpenCV

Numpy

## Results:

I was able to classify 42 blobs which were 'similar' to the query blob and 71 blobs which were 'dissimilar' to the query blob. 

## Command to run code:
```
$ python q1_init.py --blob_set blob_set/ --query_blob query_blob.png
```

## Known Issues/Bugs:
My method of evaluation works perfectly for the given set of blob set images. I have
removed features which are unable to differentiate the given set of blobs and used only those
features which are varying in the given dataset. Few instances where my method of evaluation
will fail is when the test images have blobs of smaller radius but still are similar to the query blob
in terms of circularity and aspect ratio. This is because I have evaluated the blobs with a range
close to the area of the query blob. To solve this problem, simply remove the ‘if’ statement which
checks and compares the area of the blob wrt the query blob. (1st if statement)
## References:
```
https://www.learnopencv.com/
```
