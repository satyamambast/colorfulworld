import numpy as np
import cv2
from random import randint
import PIL
lower_blue = np.array([randint(50,70), randint(100,255), randint(100,255)])

lower_blue.astype('uint8')
print(lower_blue.dtype)
a=np.full((400,400,3),(30, randint(200,255), randint(200,255)))
# b=cv2.cvtColor(lower_blue,cv2.COLOR_HSV2BGR)
# print(b)
#cv2.imshow('before',a)
cv2.imwrite("test.png",a)
img=cv2.imread('test.png')
img=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imwrite('test2.png',img)

cv2.imshow('after',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# import numpy as np
# import cv2

# green = np.uint8([[[0, 255, 0]]]) #here insert the bgr values which you want to convert to hsv
# hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print(hsvGreen)

# lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
# upperLimit = hsvGreen[0][0][0] + 10, 255, 255

# print(upperLimit)
# print(lowerLimit)
