name = input("Enter your name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower(), 
if age >= 18 and nationality == "ghanaian":
    print(f"{name}, you are Eligible to vote.")
else:
    print(f"{name}, you are Not Eligible to vote.")
    print("provide your voters cards for maual verification on polling station")
    poll_no=int(input("enter polling station number"))
    if poll_no == 1963:
       print("you can vote here")
    else:
       print ("find your polling station this isnot it")