def get_value(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return None

print(get_value([10, 20, 30], 1)) 
print(get_value([10, 20, 30], 7))  