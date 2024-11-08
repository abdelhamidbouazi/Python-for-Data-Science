from load_image import ft_load
from PIL import Image
import numpy as np


def ft_transpose(img_arr: np.array):
    assert isinstance(img_arr, np.ndarray), "Input must be a NumPy array."
    row_len, col_len, channels = img_arr.shape
    transposed = np.zeros((col_len, row_len, channels), dtype=img_arr.dtype)
    
    for i in range(row_len):
        for j in range(col_len):
            for k in range(channels):
                transposed[j, i, k] = img_arr[i, j, k]
    return transposed


def rotate():
    # print(ft_load('animal.jpeg'))
    try:
        img = Image.open('animal.jpeg').convert('L')
        arr = np.array(img)
        img_arr = ft_load('animal.jpeg')
        transposed = ft_transpose(img_arr)
        img_new = Image.fromarray(transposed).convert('L')
        
        # print(transposed is img_arr)
        # img_new.arr(400,400)
        img_new.show()
        print("zomm")
        return 
    except AssertionError as e:
        print({e})

def main():
    rotate()


if __name__ == "__main__":
    main()
