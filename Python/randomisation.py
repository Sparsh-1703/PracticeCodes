import random
print(random.randint(1,10)) #returns a random number between 1 and 10
print(random.random()*100) #returns a random number between 0 and 100 with decimals
# randint returns an integer, uniform returns a float
print(random.uniform(1, 15))  # returns a random float between 1 and 15
print("Choose Heads or Tails: ")
num = random.randint(0,1)
if num == 0:
    print("Its Heads!!")
else:
    print("Tails..")