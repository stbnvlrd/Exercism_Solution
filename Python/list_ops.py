def append(list1, list2):

    return list1 + list2

def concat(lists):
    final_list = []
    for list in lists:
        final_list.extend(list)
    return final_list


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    return len(list)


def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    result = initial
    for element in list:
        result = function(result, element)
    return result


def foldr(function, list, initial):
    result = initial
    for element in reverse(list):
        result = function(element, result)
    return result


def reverse(list):
    final_list = []
    for element in list:
        final_list.insert(0, element)
    return list[::-1]
