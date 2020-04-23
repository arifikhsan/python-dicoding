for letter in 'python':
    if letter == 'h': continue
    print(letter)

for a in [0, 1, -1, 2, -2, 3, -3]:
    if a <= 0: continue
    print(a)

var = 10
while var > 0:
    var -= 1
    if var == 5: continue
    print('Current variable value: {}'.format(var))
