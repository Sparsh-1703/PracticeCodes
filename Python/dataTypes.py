#Subscripting is a way to access a character or element of a string
print("Hello"[0]) #H

#String
print("123" + "456") #123456

# _ is a thousands separator and can be used to make numbers more readable
# . is a decimal point and can be used to specify a fractional part of a number
mystery = 734_529.678  # This is 734529.678
print(mystery)

#len is a function that returns the length of a string
print(len("Hello"))

#type is a function that returns the type of a variable
print(type("Hello"))

#Typecast is a function that changes the type of a variable
print("My age is: " +str(12))

print(6/2) #3.0
print(6//2) #3 (integer division) #removes after decimal
print(5//2) #2 instead of 2.5

#PEMDAS
#Parentheses, Exponents, Multiplication, Division, Addition, Subtraction (like BODMAS in math) left to right execution 

bmi = 80/1.68**2
print(bmi) #28.571428571428573
print(int(bmi)) #28
print(round(bmi, 1)) #rounds to 1 decimal (28.1)

print(f"Your BMI is {round(bmi, 1)}") #f-string is a way to insert variables into a string USE CURLY BRACKETS