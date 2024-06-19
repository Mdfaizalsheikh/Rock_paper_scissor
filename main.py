import random

def user_input():
  choice = input ("Enter a choice(Rock, Paper, Scissor)  ").lower()
  while choice not in ["rock","paper","scissor"]:
    choice= input("Choose between (Rock, Paper, Scissor) ")
  return choice

def computer_choice():
  return random.choice([" rock","paper","scissor"])

def winner(user,computer):
  if user==computer:
    print("Tie")
  elif (user== "rock" and computer=="scissor")or (user== "paper" and computer=="rock")or(user== "scissor" and computer=="paper"):
    print ("You win!! ")

  else:
    print(" you lose ")

def main():
  user = user_input() 
  computer= computer_choice()
  print(f" Your choice is {user}")
  print(f"computer choice is {computer}")
  result = winner(user, computer)

  print(result)

if __name__ == "__main__":
  main()

  
    
  
