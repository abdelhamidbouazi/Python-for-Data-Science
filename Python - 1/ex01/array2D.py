import numpy as np


def checkLenght(list: list):
    """function ot check if the list given has same size in all elements"""
    firstElementSize = len(list[0])
    for l in list:
        if len(l) is not firstElementSize:
            return False
    return True

def slice_me(family: list, start: int, end: int) -> list:
    """
    slice function, require the list, the start and the end of slice
    """
    assert isinstance(family, list), "family must be a list"
    assert checkLenght(family), "lenghts arn't the same in your list"
    assert isinstance(start, int), "start is not int"
    assert isinstance(end, int), "end is not int"
    checkLenght(family)
    
    familyArray = np.array(family)
    familyShape = familyArray.shape
    newArray = familyArray[start:end]
    return f"My shape is : {familyShape}\nMy new shape is : {newArray.shape}\n{newArray.tolist()}"


def main():
    """
    returns the elements that have length greater or equal
    to the length given by user
    """
    try:
        family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
