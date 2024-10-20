import sys

def whatis(x: int) -> int:
    if x % 2 == 0:
        print("I'm Even.")
    if x % 2 != 0:
        print("I'm Odd.")
    return 0

if __name__ == "__main__":
    try:
        assert sys.argv[1].isdigit(), "The argument is not an integer"
        assert len(sys.argv) == 2, "More than one argument provided"
        x = int(sys.argv[1])
        whatis(x)
    except (AssertionError) as msg:
        print("AssertionError: " + str(msg))