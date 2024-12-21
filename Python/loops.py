fruits = [ "Apple", "Peach", "Mango"]
for i in fruits:
    print(i)
    print(i + " Shake")
student_scores = [22,11,34,56,76,74,23,56,13,88,43]
sum = 0
for i in student_scores:
    sum += i
print(sum)
total = 0
for i in range(1,101):
    total += i
print(total)
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)