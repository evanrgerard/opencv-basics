import cv2
import numpy as np

# Read in an image
img = cv2.imread('../Resources/test_image2.jpg')

resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

blank = np.zeros(resized.shape, dtype='uint8')
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny Edges', canny)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('Contours Drawn', blank)


# Simple Thresholding
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY )
cv2.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV )
cv2.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)


cv2.waitKey(0)