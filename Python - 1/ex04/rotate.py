# %%
from load_image import ft_load
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
    assert isinstance(img_arr, np.ndarray), "Input must be a NumPy array."
    row_len, col_len = img_arr.shape
    transposed = np.zeros((col_len, row_len))

    for i in range(row_len):
        for j in range(col_len):
            transposed[j, i] = img_arr[i, j]
    return transposed


def ft_show(path: str):
    img = ft_load(path, 'L')
    img = img[200:600, 400:800]
    shape_new = f"{img.shape[0], img.shape[1], 1} or {img.shape}"
    print(f"The shape of image is: {shape_new}")
    print(img)
    img = ft_transpose_L(img)
    print(f"New shape after Transpose: {img.shape}")
    print(img)
    plt.imshow(img, cmap="gray")
    return


def rotate():
    try:
        ft_show('animal.jpeg')
        return
    except AssertionError as e:
        print({e})


def main():
    rotate()


if __name__ == "__main__":
    main()

# %%
