import random
winner = " "
# nesse jogo, o computador escolhe entre pedra, papel e tesoura
# em seguida, o usuario faz sua escolha

random_choice = random.randint (0,2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
elif random_choice==2: 
    computer_choice = 'scissors'   
user_choice = input (' rock, paper or scissors?')
if computer_choice == user_choice:
    winner = "Tie"
elif computer_choice == "paper" and user_choice == "rock":
    winner = "computer"
elif computer_choice == "rock" and user_choice == "scissors":
    winner = "computer"
elif computer_choice == "scissors" and user_choice == "paper":
    winner = "computer"
#existem tres possibilidades de vitoria do  computador, se não resultara em vitoria do usuario
#caso haja empate, ira jogar novamente
else: 
    winner = "user "
if winner == "tie" :
    print ("We both chose", computer_choice + ", play again!")
else:
    print (winner, "won. The computer chose ", computer_choice + " ")