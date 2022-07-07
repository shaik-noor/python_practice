import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

images = [rock,paper,scissors]

user_choice = int(input("Please choose a number? 0 is for rock, 1 for paper and 2 for scessors: \n"))
if user_choice >= 3 or user_choice < 0:
  print("You have entered a invalid number.")
else:
  print(f"user choice: \n" + images[user_choice])
  
  computer_choice = random.randint(0,2)
  print(f"computer choice: \n"+images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("your win!")
  elif user_choice == 2 and computer_choice == 1:
    print("your win!")
  elif user_choice == 1 and computer_choice == 0:
    print("You win!")
  else:
    print("you lose!")
 


