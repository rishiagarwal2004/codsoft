import random
def valid_input():#for the valid input enter by the user
   choice=int(input("Enter your choice: Type 0 for rock,Type 1 for paper,Type 2 for scissor:"))
   while choice not in [0,1,2]:
       print("Invalid Try Again")
       choice=int(input("Enter your choice: Type 0 for rock,Type 1 for paper,Type 2 for scissor:"))
   return choice   
def game():

        user_choice=valid_input()
        print(user_choice)
        computer_choice=random.randint(0,2) #randint() function takes only 0,1,2 int number from the random() function
        print("Computer Choice",computer_choice)
        if(user_choice==computer_choice):
             print("it's a Tie")
        elif((user_choice==0 and computer_choice==2)):
             print("You Win")
        elif((user_choice==2 and computer_choice==0)):
             print("You Loses")    
        elif(user_choice>computer_choice):
             print("You Win")        
        else:
             print("You Loses")
print("If you want to play the Game Type 'yes'")   
print("If you want to exit from the game type 'no'")   
while True:
    n=input("Enter:").lower()#if user want to play game then type "yes" otherwise "no"
    if  n=="yes":
        game() 
    elif n=="no":
         exit()
            #exit() function take user exit from the game