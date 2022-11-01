import cv2

img = cv2.imread("poster.jpg")

cv2.imshow("DisplayImage", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("GrayScale", gray_img)

cv2.waitKey(0)