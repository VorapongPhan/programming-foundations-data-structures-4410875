def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None 
    sort_list = sorted(my_list)
    return sort_list[1]

print(find_second_smallest([5, 8, 3, 2, 6]))
