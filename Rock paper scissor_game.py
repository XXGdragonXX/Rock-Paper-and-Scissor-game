#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
while True:
    user_choice=input("Enter your choice (Rock, Paper or Scissor)")
    choices=['Rock','Paper','Scissor']
    computer_choice=random.choice(choices)
    print(f"\nYour choice:{user_choice}   Computer choice :{computer_choice}.\n")



    
    if user_choice == computer_choice:
        print("Its a tie")
    elif user_choice == 'Rock':
        if computer_choice == "Paper":
            print("You lose suckaaaaaaaaa!!!")
          
        else:
            print("You win suckaaaaaaaa!!!!")
           
    elif user_choice == 'Paper':
        if computer_choice =='Scissor':
            print("you lose suckaaaaaaaaa!!!")
           
        else:
            print("you win suckaaaaaaaaa!!!!")
           
    elif user_choice == 'Scissor':
        if computer_choice == "Rock":
            print("You lose suckaaaaaaaaa!!!")
        
            
        else:
            print("You win suckaaaaaaaa!!!!")
    play_again = input("Play again ? press 1 to continue . Press any other key to stop: ")
    if play_again.lower() != "1":
        break
            
  


# In[ ]:




