total = 0

def sum(numone, numtwo):
    global total
    total = numone + numtwo
    print('inside function', total)
    return total

sum(2, 3) # 5
print('outside function', total) # 5
