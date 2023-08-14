
def determine_dict_or_array(json) -> str:
    if type(json) == dict:
        return "dict"
    elif type(json) == list:
        return "array"
    else:
        return None
