def initialize_list(element: int, empty_list = []):
    '''This function creates a new list and initializes it with the given integer.'''
    empty_list.append(element)
    return empty_list

zero_list = initialize_list(0)
one_list = initialize_list(1)
one = one_list[0]
result = 5/one

print("result:", result)