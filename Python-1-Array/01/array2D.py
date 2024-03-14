import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''Return a slice of the 2D array received'''
    try:
        if (not isinstance(family, list) or not isinstance(start, int)
                or not isinstance(end, int)):
            raise ValueError("ArgumentError: not the right type")

        np_family = np.array(family)
        shape = np_family.shape
        print("my shape is : " + str(shape))

        if start >= 0 and end <= shape[1]:
            new_family = np_family[start:end, :]
            new_shape = new_family.shape
            print("my new shape is : " + str(new_shape))
        else:
            raise IndexError("IndexError: indices are out of bounds on axis 1")

        return new_family

    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
