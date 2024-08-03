import random

rock = '''
rock        
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''
       
paper = '''
paper
        /')    ./')             
      /' /.--''./'')           
 :--''  ;    ''./'')           
 :     '     ''./')            
 :           ''./'               
 :--''-..--''''   '''
 
scissors = '''
scissors
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/              '''

game = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors): "))
action = ["rock", "paper", "scissors"]
ation = ["rock", "paper", "scissors"]

if game < 0 or game > 2:
    print("Enter a valid input (0, 1, or 2).")
else:
    user_action = action[game]
    comp_action = random.choice(ation)

    print(f"You chose: {user_action}")
    print(f"Computer chose: {comp_action}")

    if user_action == "rock" and comp_action == "scissors":
        print("You", rock)
        print("Computer", scissors)
        print("You win!")
    elif user_action == "rock" and comp_action == "rock":
        print("You", rock)
        print("Computer", rock)
        print("It's a draw")
    elif user_action == "rock" and comp_action == "paper":
        print("You", rock)
        print("Computer", paper)
        print("You lose!")
    elif user_action == "paper" and comp_action == "scissors":
        print("You", paper)
        print("Computer", scissors)
        print("You lose!")
    elif user_action == "paper" and comp_action == "paper":
        print("You", paper)
        print("Computer", paper)
        print("It's a draw")
    elif user_action == "paper" and comp_action == "rock":
        print("You", paper)
        print("Computer", rock)
        print("You win!")
    elif user_action == "scissors" and comp_action == "rock":
        print("You", scissors)
        print("Computer", rock)
        print("You lose!")
    elif user_action == "scissors" and comp_action == "paper":
        print("You", scissors)
        print("Computer", paper)
        print("You win!")
    elif user_action == "scissors" and comp_action == "scissors":
        print("You", scissors)
        print("Computer", scissors)
        print("It's a draw")
