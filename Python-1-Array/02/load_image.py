import os
import numpy as np
from PIL import Image

def ft_load(path: str) -> list:
	if not os.path.exists(path):
		print(f"Error: File not found - {path}")
		return []
	
	img = Image.open(path)
	np_img = np.array(img)
	shape_img = np_img.shape
	print("The shape of image is : " + str(shape_img))
	
	return np_img
		