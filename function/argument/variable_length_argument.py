def print_number(number, *numbers):
    print('first argument', number)
    for n in numbers: print(n)

print_number(10)
print_number(1, 2, 3, 4, 5)
