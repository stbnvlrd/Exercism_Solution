def flatten(iterable):
    new_list = []
    no_nested_array = []
    for list_element in iterable:
        if isinstance(list_element, list):
            for element in list_element:
                if isinstance(element, list):
                    for element_of_element in element:
                        if isinstance(element_of_element, list):
                            for lower_element in element_of_element:
                                if isinstance(lower_element, list):
                                    for lowest_element in lower_element:
                                        new_list.append(lowest_element)
                                else:
                                    new_list.append(lower_element)
                        else:
                                new_list.append(element_of_element)
                else:
                        new_list.append(element)
        else:
            new_list.append(list_element)
    
    for element in new_list:
        if element != None:
            no_nested_array.append(element)
    return no_nested_array
        