
list_data = [2,3,4,5,6,7,9,11]

def is_even(a):
    return a % 2 == 0

my_list = list(map(lambda a: a * 2, list_data))

filtered_list = list(filter(is_even, list_data))

print(filtered_list)

print(my_list)
