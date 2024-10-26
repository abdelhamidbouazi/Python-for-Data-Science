import numpy as np

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    assert isinstance(height, list), "height must be a list"
    assert isinstance(weight, list), "weigth must be a list"
    assert all(isinstance(h, (int, float))
               for h in height), "height must be int or float"
    assert all(isinstance(w, (int, float))
               for w in weight), "weight must be int or float"
    assert len(height) == len(weight), "length error, given\
            lists must be same size"

    bmi = [w / (h ** 2) for w, h in zip(weight, height)]
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert isinstance(bmi, list), "bmi must be a list"
    assert isinstance(limit, int), "limit must be an int"
    assert all(isinstance(h, (int, float))
               for h in bmi), "bmi must be int or float"

    checker = [bmi > limit for bmi in bmi]
    return checker

def checkLenght(list: list):
    clist = np.array(list)
    firstElementSize = clist[0].shape
    for l in clist:
        assert l.shape != firstElementSize, "error"
    return True
        # if l.shape != firstElementSize

def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list), "family must be a list"
    assert checkLenght(family), "lenghts arn't the same in your list"
    assert isinstance(start, int), "start is not int"
    assert isinstance(end, int), "end is not int"
    newResult = np.array(family)
    checkLenght(newResult)
    
    
    
    # assert (lenght >= end), "end out of range"
    # print(lenght)
    # return newResult.tolist()


def main():
    """
    returns the elements that have length greater or equal
    to the length given by user
    """
    try:
        # height = [2.71, 1.15]
        # weight = [165.3, 38.4]
        # bmi = give_bmi(height, weight)
        # print(bmi, type(bmi))
        # print(apply_limit(bmi, 26))
        slice_me([[2, 3], [4, 5, 6]], 1, 2)
        # slice_me(arr, 1, 6)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
