def check_args(args, kwargs):
    keys = ["toto", "tutu", "tata"]
    operations = ["mean", "median","quartile"]
    for i in args:
        if not isinstance(i, int):
            return 0
    for key in kwargs:
        if not key in keys or not kwargs[key] in operations:
            print(kwargs[key])
            return 0
    return 1


def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        assert len(args) > 0, "ERROR"
        assert check_args(args, kwargs), "ERROR"
        # check_args(args, kwargs)
        print(f"passed, args : {type(args)}, {type(kwargs)}")
    except :
        print("ERROR")
        return
ft_statistics(2, 5, 8, 5, 7, toto="mean", tutu="median", tata="quartile")