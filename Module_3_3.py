def print_params (a = 1, b = 'строка ', c = True):
    print(a, b, c)

print_params(), print_params(2, 2), print_params(3, 'Лулинэ', False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Эорлинг', True, 82.22]
values_dict = {'a': 13, 'b': "Гондор", 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'строка']

print_params(*values_list_2, 42)
