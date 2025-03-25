import random
def valid_input():
   choice=int(input("Enter your choice: Type 0 for rock,Type 1 for paper,Type 2 for scissor:"))
   while choice not in [0,1,2]:
       print("Invalid Try Again")
       choice=int(input("Enter your choice: Type 0 for rock,Type 1 for paper,Type 2 for scissor:"))
   return choice   
def game():

        user_choice=valid_input()
        print(user_choice)
        computer_choice=random.randint(0,2)
        print("Computer Choice",computer_choice)
        if(user_choice==computer_choice):
             print("Match is Drow")
        elif((user_choice==0 and computer_choice==2)):
             print("User Win")
        elif((user_choice==2 and computer_choice==0)):
             print("Computer Win")    
        elif(user_choice>computer_choice):
             print("User win")        
        else:
             print("Computer win")
#n=input("Enter:")           
#for i in range(n):
print("If you want to exit from the Game Type 'Never'")   
print("If you want to play the Game then Type any character")   
while True:
    n=input("Enter:").lower()              
    if  n=="never":
        exit() 
    else:            
       game()           
