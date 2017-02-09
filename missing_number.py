def find_missing(g, h):
    if len(g) > len(h):
        first_list = g
        second_list = h
    else:
        first_list = h
        second_list = g
        
    if not first_list and not second_list:
         return 0
    elif first_list == second_list:
        return 0
    
    for entry in first_list:
        if entry not in second_list:
            return entry
        
