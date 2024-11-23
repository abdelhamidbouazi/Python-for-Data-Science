def format_num(num):
    """format numbers that has .0"""
    if num == int(num):
        return int(num)
    return num


def check_args(args, kwargs):
    """handling errors and checking args"""
    # operations = ["mean", "median","quartile", "std", "var"]
    err = 0
    for i in args:
        if not isinstance(i, int):
            return 0
    for key in kwargs:
        if kwargs[key] and len(args) == 0:
            err += 1
    if err == 0:
        return 0
    for e in range(err):
        print("ERROR")
    return 1


def cal_mean(args) -> int:
    """calculate the Mean"""
    length = len(args)
    result = 0
    for i in args:
        result += i
    result = result / length
    return result


def cal_median(args) -> int:
    """calculate the Median"""
    if len(args) == 1:
        return args[0], 0
    result = 0
    sorted_numbers = sorted(args)
    middle = 0
    if len(sorted_numbers) % 2 == 0:
        middle = int(len(sorted_numbers) / 2)
        result = (sorted_numbers[middle] + sorted_numbers[middle - 1]) / 2
    else:
        middle = int((len(sorted_numbers) - 1) / 2)
        result = sorted_numbers[middle]
    return format_num(result), middle


def cal_quartile(args):
    """calculate the Quartile 25% and 75%"""
    if len(args) == 1:
        return args[0]
    median, median_index = cal_median(args)
    lower_half = sorted(args)[0:median_index]
    upper_half = sorted(args)[median_index + 1:]
    print(upper_half)
    q1 = cal_median(lower_half)
    q3 = cal_median(upper_half)
    return list((q1[0], q3[0]))


def cal_var(args):
    """calculate the Variance"""
    mean = cal_mean(args)
    len_data = len(args)
    sigma = 0
    for i in range(len_data):
        sigma += (args[i] - mean) ** 2
    result = sigma / len_data
    return result


def ft_statistics(*args: any, **kwargs: any) -> None:
    """function to calculate the Mean, Median, Quartile
    (25% and 75%), Variance and Standard Deviation
    Returns:
        None
    """
    if check_args(args, kwargs):
        return None
    for key in kwargs:
        if kwargs[key] == 'mean':
            print(f"mean : {cal_mean(args)}")
        elif kwargs[key] == 'median':
            print(f"median : {cal_median(args)[0]}")
        elif kwargs[key] == 'quartile':
            print(f"quartile : {cal_quartile(args)}")
        elif kwargs[key] == 'std':
            print(f"std : {cal_var(args) ** 0.5}")
        elif kwargs[key] == 'var':
            print(f"var : {cal_var(args)}")
