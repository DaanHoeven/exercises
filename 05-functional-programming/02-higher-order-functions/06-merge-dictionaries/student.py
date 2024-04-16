def merge_dictionaries(d1, d2, merge_function):
    merged_dict = {}

    for key, value in d1.items():
        merged_dict[key] = value

    for key, value in d2.items():
        if key in merged_dict:
            merged_dict[key] = merge_function(merged_dict[key], value)
        else:
            merged_dict[key] = value

    return merged_dict
