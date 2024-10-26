import sys


def main(argv):
    """
    returns the elements that have length greater or equal
    to the length given by user
    """
    try:
        assert len(argv) == 3, "the arguments are bad"
        assert argv[2].isdigit(), "the arguments are bad"
        length = int(argv[2])
        words_list = argv[1].split()
        return print([word for word in words_list if len(word) >= length])
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv)
