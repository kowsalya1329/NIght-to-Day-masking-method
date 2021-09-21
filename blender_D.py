from __future__ import print_function
import numpy as np
import cv2 as cv


def blender(src1,src2,aplha,gamma):
    beta=(1.0-aplha)
    dst=cv.addWeighted(src1,aplha,src2,beta,gamma)
    return dst


