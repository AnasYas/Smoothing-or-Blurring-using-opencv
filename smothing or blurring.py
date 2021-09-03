import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('lena.jpg')
averaging=cv2.blur(img,(11,11))
gblue=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bilateralfilter=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('img',img)
cv2.imshow('averaging',averaging)
cv2.imshow('gblue',gblue)
cv2.imshow('median',median)
cv2.imshow('bilateralfilter',bilateralfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
