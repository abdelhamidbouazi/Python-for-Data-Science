# %%
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


# def ft_show(array: str):
#     # img = ft_load(path, 'L')
#     # img = img[200:600, 400:800]
#     # shape_new = f"{img.shape[0], img.shape[1], 1} or {img.shape}"
#     # print(f"The shape of image is: {shape_new}")
#     # print(img)
#     # img = ft_transpose_L(img)
#     # print(f"New shape after Transpose: {img.shape}")
#     # print(img)
#     # plt.imshow(img, cmap="gray")
#     plt.imshow(array)
#     plt.axis('off')
#     plt.show()
#     return
# def ft_show(array: str):
#     plt.imshow(array)
#     plt.axis('off')
#     plt.show()
#     return

def display_original(array: str):
    plt.figure()
    plt.imshow(array)
    plt.axis('off')
    return


def ft_invert(array):
    """Ft_invert
    Display the given image with inverted colors
    Args:
        array (nparray): the image array of type numpy
    """
    display_original(array)
    plt.figure()

    new_array = np.zeros_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            new_array[i, j] = 255 - array[i, j]
    plt.imshow(new_array)
    plt.axis('off')


def ft_red(array):
    """Ft_red
    Display the red colors in the image

    Args:
        array (nparray): the image array of type numpy
    """
    plt.figure()
    new_array = np.zeros_like(array)
    heigth, width, _ = array.shape

    for i in range(heigth):
        for j in range(width):
            r, g, b = array[i, j]
            new_r = min(255, r * 1.5)
            new_array[i, j] = (new_r, 0, 0)
    plt.imshow(new_array)
    plt.axis('off')


def ft_green(array):
    """Ft_green
    Display the green colors in the image

    Args:
        array (nparray): the image array of type numpy
    """
    plt.figure()
    new_array = np.zeros_like(array)
    heigth, width, _ = array.shape

    for i in range(heigth):
        for j in range(width):
            r, g, b = array[i, j]
            new_array[i, j] = (0, g, 0)
    plt.imshow(new_array)
    plt.axis('off')


def ft_blue(array):
    """Ft_blue
    Display the blue colors in the image

    Args:
        array (nparray): the image array of type numpy
    """
    plt.figure()
    new_array = np.zeros_like(array)
    heigth, width, _ = array.shape

    for i in range(heigth):
        for j in range(width):
            r, g, b = array[i, j]
            new_array[i, j] = (0, 0, b)
    plt.imshow(new_array)
    plt.axis('off')


def ft_grey(array):
    """Ft_grey
    Display the image in a greyscale mode

    Args:
        array (nparray): the image array of type numpy
    """
    plt.figure()
    new_array = np.zeros_like(array)
    heigth, width, _ = array.shape

    for i in range(heigth):
        for j in range(width):
            r, g, b = array[i, j]
            new_r = r / 3.344
            new_g = g / 1.701
            new_b = b / 8.771
            gray = new_r + new_g + new_b
            new_array[i, j] = (gray, gray, gray)
    plt.imshow(new_array)
    plt.axis('off')


def main():
    try:
        array = ft_load("landscape.jpeg")
        assert array is not None, "please provide a valid image"
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

# %%
