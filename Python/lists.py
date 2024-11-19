import random
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Conneticut"]
states_of_india = ["Delhi", "Mumbai", "Pune", "Chennai", "Kolkata"]
states = [states_of_america, states_of_india]
# This line prints the third character of the second state in the 'states_of_india' list.
# 'states' is a list containing two lists: 'states_of_america' and 'states_of_india'.
# 'states[1]' accesses the 'states_of_india' list.
# 'states[1][1]' accesses the second element in 'states_of_india', which is "Mumbai".
# 'states[1][1][2]' accesses the third character in "Mumbai", which is 'm'.
print(states[1][1][2])
states_of_america[0]= "Pencil"
print(states_of_america[0])
states_of_america.extend(["wow", "wowie","wowzers"])
print(states_of_america)
print(random.choice(states_of_america))
print(len(states_of_america))