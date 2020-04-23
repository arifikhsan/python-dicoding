def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print('dalam fungsi', mylist)

mylist = [10, 20, 30]
changeme(mylist)
print('luar fungsi', mylist)
