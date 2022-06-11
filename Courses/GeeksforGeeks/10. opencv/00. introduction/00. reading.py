# import open cv library
import cv2 as cv
# read image
img = cv.imread('resources/image_sanskrit_text.jpg')
# extract height and width of image
height, width = img.shape[:2]
# print height and width
print(f"height{height}, width{width}")