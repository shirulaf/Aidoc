convert_mapper = {
    "int": lambda string: int(float(string)),
    "float": lambda string: float(string)
}


def convert_string_to_type(string_to_convert: str, new_type: str):
    if new_type == "str" or string_to_convert == "":
        return string_to_convert

    else:
        return convert_mapper[new_type](string_to_convert)
