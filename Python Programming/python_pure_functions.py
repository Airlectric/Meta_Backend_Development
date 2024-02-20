my_list = [1,2,3,4]

def add_to_list(ls, item):
    nl = ls.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list,5)

print(my_list)
print(new_list)