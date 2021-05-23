def sum(num1, num2):
    my_sum = num1 + num2
    return my_sum


def last_item_in_list1 (arg_list):
    for entry in arg_list:
        return_value = entry
    return return_value

def last_item_in_list2(arg_list):
    for entry in arg_list:
        pass
    return entry

def last_item_in_list3(arg_list):
    return list(reversed(arg_list))[0]

def last_item_in_list4(arg_list):
    return arg_list[-1]


dict1 =['a', 'b', 'c', 'd']
dict2 = ['b', 'g', 'a']

print(last_item_in_list1(dict1))
print(last_item_in_list2(dict1))
print(last_item_in_list3(dict1))
print(last_item_in_list4(dict1))


def even(arg):
    if arg % 2 == 0:
        return True
    else:
        return False


def filter_odd_elements(input_list):
    output_list = []
    for element in input_list:
        if even(element):
            output_list.append(element)
    return output_list

l = list(range(99))
print(l)


print(filter_odd_elements(l))


def return_four_letter_strings(input_list):
    output_list = []
    for element in input_list:
        if len(element) == 4:
            output_list.append(element)
    return output_list


print(set(dict1) - set(dict2))
print(set(dict1) & set(dict2))