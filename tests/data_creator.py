from random import shuffle, seed
from math import ceil, log10

def create_dictionary_array(length: int, key_count: int) -> list[dict]:
    result = []
    for itemi in range(length):
        item = {}
        for keyi in range(key_count):
            item[f"key_{keyi}"] = f"item {itemi}, key {keyi}"
        result.append(item)
    return result

def create_dictionary(key_count: int, random_seed = None) -> dict:
    keys = list(range(key_count))
    if random_seed is not None:
        seed(random_seed)
        shuffle(keys)
    digit_count = ceil(log10(key_count+1))
    return { f"{k+1:>0{digit_count}}" : f"item {k+1}" for k in keys }
