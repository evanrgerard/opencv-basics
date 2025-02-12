import cv2
import numpy as np

# Read in an image
img = cv2.imread('Resources/test_image1.jpg')
cv2.imshow('Original', img)


# Rotate image
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotate Image', rot)


# Resize image
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

#Flip
flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

#Cropped
crop = img[100:300, 100:300]
cv2.imshow('Crop', crop)

#Translation
blank = np.zeros(img.shape, dtype='uint8')

height, width = img.shape[:2]
quarter_height, quarter_width = height / 4, width / 4

t = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
t2 = cv2.warpAffine(img, t, (600, 600))
cv2.imshow('Translation', t2)


cv2.waitKey(0)