passengers = int(input("How many passengers are going? "))
for i in range(passengers):
    route = input("Enter your route for the trip: ")
if route == "Accra-Madina":
 fare=5 
 print ("fare=5")
elif route=="Accra-Kasoa":
 fare=10
 print("fare=10")
elif route == "Accra-Tema":
   fare=8
   print ("fare = 8")
else:
    fare = 0
    print("Unknown route")
total_fare=fare*passengers
print("total fare is ",total_fare)
    

