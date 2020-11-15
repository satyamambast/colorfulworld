import numpy as np
import cv2
from random import randint
a=np.full((400,400,3),(0,0,randint(110,130)))
cv2.imwrite("maroon.png",a)