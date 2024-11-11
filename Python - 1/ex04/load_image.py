from PIL import Image
import numpy as np
import os


def checkPathNdFormat(path: str) -> bool:
    """Check Path And Format
    this is a functions to check the given path and format if its a valid file
    Args:
        path (str): path to file
    Returns:
        bool: false in case of error
    """
    file_extension = os.path.splitext(path)[1].lower()
    if os.path.isfile(path):
        if file_extension in ['.jpg', '.jpeg']:
            return True
    return False


def ft_load(path: str, style: str) -> np.array:
    """ft_load
    The main function to load an image, it works with numpy array
    Args:
        path (str): path to the image
    Returns:
        np.array: returns the image as a numpy array
    """
    try:
        assert checkPathNdFormat(path), "File issue!"
        assert isinstance(path, str), "Path must be a string !"
        im = Image.open(path)
        image_array = im.convert('RGB')
        # applying the style condition
        if style:
            image_array = im.convert(style)
        image_rgb = np.array(image_array)
        # print(f"The shape of image is: {image_rgb.shape}")
        return image_rgb
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


def main():
    image = "landscape.jpg"
    print(ft_load(image))


if __name__ == "__main__":
    main()
