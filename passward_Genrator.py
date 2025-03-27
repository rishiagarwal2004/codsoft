import string
import random
letters=list(string.ascii_letters)
symbols=list(string.punctuation)
number=list(string.digits)

print("Welcome to the passward Genrator")
n_letter=int(input("enter number of letter for passward genration:"))
n_symbol=int(input("enter number of symbol for passward genration:"))
n_number=int(input("enter number of digits for passward genration:"))

passward_list=[]
for i in range(n_letter):
    passward_list+=random.choice(letters)    
for i in range(n_symbol):
    passward_list+=random.choice(symbols)    
for i in range(n_number):
    passward_list+=random.choice(number)
random.shuffle(passward_list)    
passward=""
for char in passward_list:
        passward+=char
print("you'r passward is genrated-",passward)        
print("Thankyou")