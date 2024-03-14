import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    '''Load the image from the given path
        and return it as a list of list of list'''
    try:
        if not os.path.exists(path):
            raise ValueError("Unrecognize file path")

        img = Image.open(path)
        np_img = np.array(img)
        shape_img = np_img.shape
        print("The shape of image is : " + str(shape_img))

        return np_img

    except ValueError as ve:
        print(ve)
