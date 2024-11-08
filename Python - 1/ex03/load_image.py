from PIL import Image
import numpy as np
import os

# im = Image.open("landscape.jpg")
# print(im.format, im.size, im.mode)
# im.show()

def checkPathNdFormat(path: str) -> bool:
    file_extension = os.path.splitext(path)[1].lower()
    if os.path.isfile(path) :
        if file_extension in ['.jpg', '.jpeg'] : return True
    return False

def ft_load(path: str, style: str) -> np.array:
    try:
        assert checkPathNdFormat(path), "File does not exist or unsupported file format!"
        assert isinstance(path, str), "Path must be a string !"
        im = Image.open(path)
        
        # applying the style condition
        image_array = im.convert('RGB')
        if style :
            image_array = im.convert(style)
        image_rgb = np.array(image_array)
        print(f"The shape of image is: {image_rgb.shape}")
        return image_rgb
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    
def main():
    image = "landscape.jpg"
    print(ft_load(image))

if __name__ == "__main__":
    main()
