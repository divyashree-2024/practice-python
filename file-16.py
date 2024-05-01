#modules

#from msg import *
#hello()
#bye()
#help('modules')


#basic game

import random
while True:
     choices=["rock","paper","scissors"]
     computer=random.choice(choices)
     player=None
#print(computer)
     while player not in choices:
         player=input("rock,paper or scissors?:").lower()
     if player==computer:
         print("computer:",computer)
         print("player:",player)
         print("tie")
     elif player=="rock":
         if computer=="paper":
             print("computer:",computer)
             print("player:",player)
             print("player won")
         if computer=="scissors":
             print("computer:",computer)
             print("player:",player)
             print("player lose")
     elif player=="scissors":
         if computer=="scirrors":
             print("computer:",computer)
             print("player:",player)
             print("player lose")
         if computer=="rock":
             print("computer:",computer)
             print("player:",player)
             print("player win")
     elif player=="paper":
         if computer=="scissors":
             print("computer:",computer)
             print("player:",player)
             print("player lose")
         if computer=="rock":
             print("computer:",computer)
             print("player:",player)
             print("player win")
         play_again=input("play again?:")
         if play_again!="yes":
             break
print("bye")
