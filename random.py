import random
names = input("Please enter the names: \n")
list_names = names.split(", ")
length_names = len(list_names)
random_choice = random.randint(0, length_names-1)
who_will_pay = list_names[random_choice]
print(who_will_pay +" is going to pay the Bill!")