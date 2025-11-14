Transaction_amount=int(input("Enter transaction amount"))
if Transaction_amount <= 100:
    charges = 2
    print("you would be charged 2GHS for this transaction")
elif Transaction_amount <= 500:
    charges = 5
    print("you would be charged 5GHS for this transaction")
else:
    charges = 10
    print("you would be charged 10GHS for this transaction")

receiver_amount= Transaction_amount-charges
print("Transaction Success full amount sent",receiver_amount)
print("Transaction Sumary")
print("Initial transaction amount",Transaction_amount,"Service fee was charged at",charges,"total amount sent was",receiver_amount)