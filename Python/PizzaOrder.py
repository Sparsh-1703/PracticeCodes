print("Welcome to Python Pizza Delhivery!!")
size = input("What size pizza would you prefer? S, M , L: ").upper()
jalapenos = input("Do you want Jalapenos on your Pizza? Y/N: ").upper()
extra_cheese = input("Do you wanna go NEXT LEVEL on Cheese?: Y/N: ").upper()
#how much do they need to pay according to their Size preference
#how much to add to their bill according to their Jalapenos
#how much extra for the extra cheese, then the final bill
bill = 0
if size == "S":
    bill = 10
elif size == "M":
    bill+=20
elif size == "L":
    bill+=30
else:
    print("Invalid size selected. Please restart the order.")
    exit()
if (jalapenos and extra_cheese) == "N":
    print(f"Your final bill is ${bill}.")
elif jalapenos == "Y" and extra_cheese == "N":
    bill += 5
    print(f"Your final bill with Pizze of size {size} and Jalapenos is ${bill}.")
elif jalapenos == "N" and extra_cheese == "Y":
    bill += 10
    print(f"Your final bill with Pizza of size {size} and NEXT LEVEL CHEESE is ${bill}.")
else: 
    bill += 15
    print(f"Your final bill with Pizza of size {size}, Jalapenos and NEXT LEVEL CHEESE is ${bill}.")