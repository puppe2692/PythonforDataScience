import numpy as np
from PIL import Image


def ft_invert(array: list) -> list:
    '''Invert the color of the image received'''
    np_array = np.array(array)
    inverted_array = 255 - np_array
    inverted_image = Image.fromarray(inverted_array)
    inverted_image.show(title=inverted_image)
    print("Inverts the color of the image received.")
    return inverted_array


def ft_red(array: list) -> list:
    '''Convert the image to red scale'''
    height = len(array)
    width = len(array[0])
    np_array = np.array([[(array[i][j][0], 0, 0) for j in range(width)]
                         for i in range(height)], dtype=np.uint8)
    # declaration d'une matricce 2D
    red_image = Image.fromarray(np_array)
    red_image.show(title=red_image)
    return red_image


def ft_green(array: list) -> list:
    '''Convert the image to green scale'''
    height = len(array)
    width = len(array[0])
    np_array = np.array([[(0, array[i][j][0], 0) for j in range(width)]
                         for i in range(height)], dtype=np.uint8)
    # declaration d'une matricce 2D
    green_image = Image.fromarray(np_array)
    green_image.show(title=green_image)
    return green_image


def ft_blue(array: list) -> list:
    '''Convert the image to blue scale'''
    height = len(array)
    width = len(array[0])
    np_array = np.array([[(0, 0, array[i][j][0]) for j in range(width)]
                        for i in range(height)], dtype=np.uint8)
    # declaration d'une matricce 2D
    blue_image = Image.fromarray(np_array)
    blue_image.show(title=blue_image)
    return blue_image


def ft_grey(array: list) -> list:
    '''Convert the image to grey scale'''
    height = len(array)
    width = len(array[0])
    np_array = np.array([[(
        int(0.2989 * array[i][j][0] + 0.5870 * array[i][j][1]
            + 0.1140 * array[i][j][2]),
        int(0.2989 * array[i][j][0] + 0.5870 * array[i][j][1]
            + 0.1140 * array[i][j][2]),
        int(0.2989 * array[i][j][0] + 0.5870 * array[i][j][1]
            + 0.1140 * array[i][j][2])
    ) for j in range(width)] for i in range(height)], dtype=np.uint8)
    grey_image = Image.fromarray(np_array)
    grey_image.show(title=grey_image)
    return grey_image
