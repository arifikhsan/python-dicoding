def print_some(*arguments, **dictionaries):
    for argument in arguments: print('argumen posisi =', argument)
    for key, value in dictionaries.items(): print('argumen kata kunci {}:{}'.format(key, value))

print_some()
print_some(1, 2, 3)
print_some(i=7, j=8, k=9)
print_some(1, 2, j=8, k=9)
print_some(*(2, 3), **{'nama':'arifikhsanudin', 'umur':20})
