# %%
from load_image import ft_load
from load_image import checkPathNdFormat
import matplotlib.pyplot as plt


def zoom(path: str):
    """Ft_show
    a function to display the image zommed
    Args:
        path (str): path to the image
    """
    try:
        assert checkPathNdFormat(path), "File issue!"
        img = ft_load(path, 'L')
        print(f"The shape of image is: {img.shape}")
        print(img)
        img = ft_load(path, 'L')
        new_img = img[200:600, 400:800]
        shape_new = f"{new_img.shape[0], new_img.shape[1], 1} "
        shape_new += f"or {new_img.shape}"
        print(f"The shape of image is: {shape_new}")
        print(new_img)
        result = plt.imshow(new_img, cmap="gray")
        return result
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    try:
        zoom("/goinfre/abouazi/P-01/anismal.jpeg")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

# %%
