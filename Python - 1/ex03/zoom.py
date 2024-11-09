# %%
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_show(path: str):
    img = ft_load(path, 'RGB')
    print(f"The shape of image is: {img.shape}")
    print(img)
    img = ft_load(path, 'L')
    new_img = img[200:600, 400:800]
    shape_new = f"{new_img.shape[0], new_img.shape[1], 1} or {new_img.shape}"
    print(f"The shape of image is: {shape_new}")
    print(new_img)
    result = plt.imshow(new_img, cmap="gray")
    return result


def zoom():
    ft_show('animal.jpeg')
    return


def main():
    zoom()


if __name__ == "__main__":
    main()

# %%
