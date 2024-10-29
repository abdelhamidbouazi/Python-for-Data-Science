from load_image import ft_load
from PIL import Image
import numpy as np


def zoom():
    # print(ft_load('animal.jpeg'))
    img = Image.open('animal.jpeg').convert('L')
    arr = np.array(img)
    arr.slice(400,400)
    img.show()
    print("zomm")

def main():
    zoom()


if __name__ == "__main__":
    main()
