import os
import pandas as pd
import numpy as np


def load(path: str) -> list:
    try:
        if not os.path.exists(path):
            raise ValueError("Unrecognize file path")

        data_file = pd.read_csv(path)
        numpy_ar = np.array(data_file)
        data_shape = numpy_ar.shape
        print("Loading dataset of dimensions " + str(data_shape))

        return data_file

    except ValueError as ve:
        print(ve)
        return None
