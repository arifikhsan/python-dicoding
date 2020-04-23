for letter in 'Python':
    if letter == 'h':
        pass
        print ("This is pass block")
    print('Current letter: {}'.format(letter))

for letter in 'Python':
    if letter.isupper():
        pass  # will process later
    else:
        print('Lower letter: {}'.format(letter))
