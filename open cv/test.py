import cv2 as cv

# reading images
img=cv.imread('resources/images/shlok.jpg')
cv.imshow('shlok',img)
cv.waitKey(0)

# reading videos
vdo=cv.videoCapture('resources/videos/shlok.mp4')

