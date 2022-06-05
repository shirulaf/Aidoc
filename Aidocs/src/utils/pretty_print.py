import tabulate


def pp_list(list_data):
    headers = list_data[0].keys()
    rows = [item.values() for item in list_data]
    print(tabulate.tabulate(rows, headers, showindex=list(range(1, len(list_data) + 1))))


def pp_value(value, function_name: str):
    print(f"{function_name.title().replace('_', ' ')} : {value}")


def pretty_print_list(func):
    def decorated_func(*args, **kwargs):
        result = func(*args, **kwargs)
        pp_list(result)

        return result

    return decorated_func


def pretty_print_value(func):
    def decorated_func(*args, **kwargs):
        result = func(*args, **kwargs)
        pp_value(result, func.__name__)

        return result

    return decorated_func
