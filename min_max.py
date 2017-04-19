def find_min_max(alist):
    new_list = []
    min_value = min(alist)
    max_value = max(alist)
    result = [min_value, max_value]

    if min_value == max_value:
        new_list.append(len(alist))
        return new_list
    return result
