# %%
from load_image import ft_load
from load_image import checkPathNdFormat
import matplotlib.pyplot as plt
import numpy as np


# def ft_transpose(img_arr: np.array):
#     assert isinstance(img_arr, np.ndarray), "Input must be a NumPy array."
#     row_len, col_len, channels = img_arr.shape
#     transposed = np.zeros((col_len, row_len, channels), dtype=img_arr.dtype)
#     for i in range(row_len):
#         for j in range(col_len):
#             for k in range(channels):
#                 transposed[j, i, k] = img_arr[i, j, k]
#     return transposed


def ft_transpose_L(img_arr: np.array):
    """Ft_transpose
    a function to transpose an array
    Args:
        img_arr (np.array): the array u want to transpose

    Returns:
        transposed (np.array): the transposed array
    """
    assert isinstance(img_arr, np.ndarray), "Input must be a NumPy array."
    row_len, col_len = img_arr.shape
    transposed = np.zeros((col_len, row_len))

    for i in range(row_len):
        for j in range(col_len):
            transposed[j, i] = img_arr[i, j]
    return transposed


def rotate(path: str):
    """Rotate
    This function rotate an imageand displays it
    Args:
        path (str): path to the image
    """
    assert checkPathNdFormat(path), "File issue!"
    img = ft_load(path, 'L')
    img = img[200:600, 400:800]
    shape_new = f"{img.shape[0], img.shape[1], 1} or {img.shape}"
    print(f"The shape of image is: {shape_new}")
    print(img)
    img = ft_transpose_L(img)
    print(f"New shape after Transpose: {img.shape}")
    print(img)
    plt.imshow(img, cmap="gray")


def main():
    try:
        rotate('/goinfre/abouazi/P-01/animal.jpeg')
        return
    except AssertionError as e:
        print({e})


if __name__ == "__main__":
    main()

# %%
