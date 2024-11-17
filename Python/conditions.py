print("Welcome to the rollercoaster: ")
height = int(input("What is your height in cm?: "))
if height >= 160:
    print("You are eligible for a ride :)")
    age = int(input("Tell us your age: "))
    if age <= 18:
        bill = 5
        print("You'll be charged    $5 for this ride.")
    elif age >= 30:
        bill = 30
        print("Pay the $30")
    else:
        bill = 15
        print("Booyah! Pay up $15.")
    photo = input("Do you want a Photo for the memories? Y/N ").upper()
    if photo == "Y":
        bill += 3
        print("Your total bill is $", bill)
    else:
        print(f"Your total bill is ${bill}.")
else:
    print("You are not eligible for this ride shawtyy ;[ ")
    
print("Check for Prime or Non-Prime number: ")
num = int(input("Enter a number: "))
if num%2==0:
    print("Even!")
else:
    print("Odd!")