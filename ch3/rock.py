import random

random_choice = random.randint (0,2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
elif random_choice==2: 
    computer_choice = 'scissors'   
user_choice = input (' rock, paper or scissors?')
print (' You chose', user_choice , 'and the computer chose' , computer_choice )


     
