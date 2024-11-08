# %%
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


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
    print(ft_load(path, 'L'))
    img = ft_transpose_L(img[200:600, 400:800])
    # new_image = Image.fromarray(img)
    # trasnposed_img = ft_load(path, 'RGB')
    print(img)
    imgplot = plt.imshow(img, cmap="gray")


def rotate():
    try:
        print(ft_show('animal.jpeg'))
        
        return 
    except AssertionError as e:
        print({e})

def main():
    rotate()


if __name__ == "__main__":
    main()

# %%
