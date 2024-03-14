import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import ft_load


def transposed_list(array: list) -> list:
    '''Transpose the array received'''
    transposed_matrix = [list(row) for row in zip(*array)]
    return transposed_matrix


def ft_rotate(array: list) -> list:
    '''Rotate the image received'''
    np_array = np.array(array)
    new_array = np_array[100:500, 450:850, :1]
    transposed_array = transposed_list(new_array)
    np_transposed_array = np.array(transposed_array)
    new_shape = np_transposed_array.shape
    print("my new shape is : " + str(new_shape))
    print(np_transposed_array)

    new_image = np_transposed_array[:, :, 0]
    final_image = Image.fromarray(new_image)
    final_image = final_image.convert("L")

    # Get image information
    size_x, size_y = final_image.size
    channels = final_image.getbands()
    pixel_array = np.array(final_image)

    # Display the image
    plt.imshow(pixel_array, cmap="gray")

    # Display the size information
    plt.text(0, -20, f"Size: {size_x} x {size_y} pixels",
             fontsize=10, color='black')

    # Display the number of channels
    plt.text(0, -40, f"Channels: {len(channels)}", fontsize=10, color='black')

    # Display the pixel content
    plt.text(size_x + 10, 10, "Pixel Content:", fontsize=10, color='black')
    for i, channel in enumerate(channels):
        plt.text(size_x + 10, 30 + i * 20,
                 f"Channel {i + 1}: {channel}", fontsize=10, color='black')

    # Display the scale on the x and y axis
    plt.xticks(np.arange(0, size_x, 50))
    plt.yticks(np.arange(0, size_y, 50))

    plt.show()


def main():
    data_img = ft_load("animal.jpeg")
    if data_img is None:
        return
    print(data_img)
    ft_rotate(data_img)


if (__name__ == "__main__"):
    main()
