def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    converted_coor = (coordinate[0], coordinate[1])
    return converted_coor


def compare_records(azara_record, rui_record):
    azara_coor = get_coordinate(azara_record)
    azara_conv_coor = convert_coordinate(azara_coor)
    rui_coor = get_coordinate(rui_record)

    return azara_conv_coor == rui_coor


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        new_record = azara_record + rui_record
    else:
        new_record = 'not a match'

    return new_record


def clean_up(combined_record_group):
    ordered_record_list = list()
    for index in range(len(combined_record_group)):
        ind_record = combined_record_group[index]
        ordered_record = ind_record[0], ind_record[2], ind_record[3], ind_record[4]
        ordered_record_list.append(ordered_record)
    final_record = tuple(ordered_record_list)
    return final_record


print(clean_up((("Scrimshaw Whale's Tooth", '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
            ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
            ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
            ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
            ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
            ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
            ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
            ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
            ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
            ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
            ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
            ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
            ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow'))))
