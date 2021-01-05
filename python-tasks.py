def list_duplicates(input_list):
    duplicates = []
    for i in input_list:
        if input_list.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates


list1 = [1, 1, 1, 2, 2, 3, 5, 6, 7, 8, '', ' ', '  ', '   ', '    ']
print(f'Duplicates in list: {list_duplicates(list1)}')


def is_empty_strings(input_list):
    for i in input_list:
        if not i:
            return True


print(f'Empty strings in list: {is_empty_strings(list1)}')


def is_list_equal(input_list1, input_list2):
    for i in input_list1[:]:
        if i in input_list2[:]:
            input_list1.remove(i)
            input_list2.remove(i)

    return sorted(input_list1) == sorted(input_list2)


list2 = [1, 1, 1, 2, 2, 3, 5, 6, 7, 8, '', ' ', '  ', '   ', '    ']
print(f'Is lists are equal: {is_list_equal(list1, list2)}')


def is_dicts_equal(input_dict1, input_dict2):
    for d in [input_dict1, input_dict2]:
        for key, value in d.items():
            if isinstance(value, (int, float, dict)):
                continue
            elif isinstance(value, list):
                d[key] = sorted(value)
            elif isinstance(value, tuple):
                d[key] = tuple(sorted(value))
            elif isinstance(value, set):
                d[key] = set(sorted(value))
            elif isinstance(value, str):
                d[key] = ''.join(sorted(value))

    return input_dict1 == input_dict2


dict1 = {1: [2, 1], 2: [1, 2, 3, 4, 5], 3: {2, 1}, 4: 1.1, 5: 2, 6: {1: 1},
         7: {1, 2, 3}, 8: 'abc'}
dict2 = {1: [1, 2], 2: [5, 4, 3, 2, 1], 3: {1, 2}, 4: 1.1, 5: 2, 6: {1: 1},
         7: {3, 2, 1}, 8: 'cba'}
print(f'Is dicts are equal: {is_dicts_equal(dict1, dict2)}')


def is_dict_values_equal(input_dict1, input_dict2):

    sorted_values_dict1 = []
    sorted_values_dict2 = []

    for value in input_dict1.values():
        if isinstance(value, (int, float)):
            sorted_values_dict1.append(value)
        else:
            sorted_values_dict1.append(sorted(value))

    for value in input_dict2.values():
        if isinstance(value, (int, float)):
            sorted_values_dict2.append(value)
        else:
            sorted_values_dict2.append(sorted(value))

    for value in sorted_values_dict1[:]:
        if value in sorted_values_dict2[:]:
            sorted_values_dict1.remove(value)
            sorted_values_dict2.remove(value)

    return sorted(sorted_values_dict1) == sorted(sorted_values_dict2)


print(f'Is dict values are equal: {is_dict_values_equal(dict1, dict2)}')
