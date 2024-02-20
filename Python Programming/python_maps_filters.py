menu = ['espresso', 'mocha', 'latte', 'cuppuccino','cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# map_coffee = map(find_coffee,menu)

# for type_of_coffee in map_coffee:
#     print(type_of_coffee)

filter_coffee = filter(find_coffee,menu)
for type_of_coffee in filter_coffee:
    print(type_of_coffee)