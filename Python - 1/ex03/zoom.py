# %%
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_show(path: str):
    img = ft_load(path, 'L')
    print(img[200:600, 400:800])
    imgplot = plt.imshow(img[200:600, 400:800], cmap="gray")

def zoom():
    ft_show('animal.jpeg')
    return


def main():
    zoom()


if __name__ == "__main__":
    main()

# %%
