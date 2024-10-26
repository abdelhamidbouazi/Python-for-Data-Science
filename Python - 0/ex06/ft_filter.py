def ft_filter(func, iterable):
    """Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true."""
    return [item for item in iterable if func(item)]


def main():
    """main program"""
    return


if __name__ == "__main__":
    main()
