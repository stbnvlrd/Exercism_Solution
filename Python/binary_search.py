def find(search_list, value):
    found = False
    place = 0
    for index in range(len(search_list)):
        if search_list[index] == value:
            found = True
            place = index
            break
    if found == True:
        return place
    else:
        raise ValueError("value not in array")

