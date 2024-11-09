def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Give_bmi
    Calculate the bmi
    Args:
        height (list[int  |  float]): heigth
        weight (list[int  |  float]): weigth

    Returns:
        list[int | float]: bmis
    """
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
    """Apply_limit
    A function to check if list o bmis is bellow limit
    Args:
        bmi (list[int  |  float]): list of bmis
        limit (int): the limit as an integer

    Returns:
        list[bool]: function return list of booleans based on the checker
    """
    assert isinstance(bmi, list), "bmi must be a list"
    assert isinstance(limit, int), "limit must be an int"
    assert all(isinstance(h, (int, float))
               for h in bmi), "bmi must be int or float"

    checker = [bmi > limit for bmi in bmi]
    return checker


def main():
    """
    returns the elements that have length greater or equal
    to the length given by user
    """
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
