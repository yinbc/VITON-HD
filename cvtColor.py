import cv2
img=cv2.imread('datasets/test/cloth-mask/888888.jpg',1)
dst=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('dst',dst)
cv2.imwrite('datasets/test/cloth-mask/88888_00.jpg',dst)
cv2.waitKey(0)