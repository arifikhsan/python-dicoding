amount = int(input("Enter amount: "))

if amount < 1000:
   discount = amount * 0.05
   print("Discount", discount)
else:
   discount = amount * 0.10
   print("Discount", discount)

print ("Net payable:",amount-discount)

a = 8
if a % 2 == 0:
    print('bilangan {} adalah genap'.format(a))
else:
    print('bilangan {} adalah ganjil'.format(a))
