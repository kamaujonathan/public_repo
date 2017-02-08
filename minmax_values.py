def find_max_min(valuelist):
    min_value = None
    max_value = None
    list_values = []
    for value in valuelist:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
            
    for value_2 in valuelist:
        if not max_value:
            max_value = value_2
        elif value_2 > max_value:
            max_value = value_2

    if (min_value == max_value):
        equal_list = len(valuelist)
        list_values.append(equal_list)

    else:
        list_values.append(min_value)
        list_values.append(max_value)

    return list_values
