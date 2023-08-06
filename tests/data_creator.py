
def create_dictionary_array(length: int, key_count: int) -> list[dict]:
    result = []
    for itemi in range(length):
        item = {}
        for keyi in range(key_count):
            item[f"key_{keyi}"] = f"item {itemi}, key {keyi}"
        result.append(item)
    return result
