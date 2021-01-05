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
    dicts = [input_dict1, input_dict2]
    sorted_items = []
    for d in dicts:
        for item in d.items():
            sorted_item = []
            for i in item:
                if isinstance(i, int):
                    sorted_item.append(i)
                else:
                    sorted_item.append(sorted(i))
            if sorted_item in sorted_items:
                sorted_items.remove(sorted_item)
            else:
                sorted_items.append(sorted_item)
    return sorted_items == []


dict1 = {1: [2, 1], 2: [1, 2, 3, 4, 5], 3: [2, 1], 4: 2, 5: 2}
dict2 = {1: [1, 2], 2: [5, 4, 3, 2, 1], 3: [1, 2], 4: 1, 5: 1}
print(f'Is dicts are equal: {is_dicts_equal(dict1, dict2)}')


def is_dict_values_equal(input_dict1, input_dict2):

    sorted_values_dict1 = []
    sorted_values_dict2 = []

    for value in input_dict1.values():
        if isinstance(value, int):
            sorted_values_dict1.append(value)
        else:
            sorted_values_dict1.append(sorted(value))

    for value in input_dict2.values():
        if isinstance(value, int):
            sorted_values_dict2.append(value)
        else:
            sorted_values_dict2.append(sorted(value))

    for value in sorted_values_dict1[:]:
        if value in sorted_values_dict2[:]:
            sorted_values_dict1.remove(value)
            sorted_values_dict2.remove(value)

    return sorted(sorted_values_dict1) == sorted(sorted_values_dict2)


print(f'Is dict values are equal: {is_dict_values_equal(dict1, dict2)}')
