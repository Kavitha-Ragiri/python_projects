import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', 
         '(', ')', '+', '|', '~','<','>','?','/','.']
numbers=['1','2','3','4','5','6','7','8','9','0']

print("Welcome to PassWord generator")

no_letters=int(input(("How many letters you want in your password? \n")))
no_symbols=int(input(("How many symbols you want in your password? \n")))
no_numbers=int(input(("How many numbers you want in your password? \n")))

password_list=[]

for i in range(1,no_letters+1):
    char=random.choice(letters)
    password_list+=char 
for i in range(1,no_symbols+1):
    char=random.choice(symbols)
    password_list+=char 
for i in range(1,no_numbers+1):
    char=random.choice(numbers)
    password_list+=char 

print(password_list)
random.shuffle(password_list)  
print(password_list)

password=""
for i in password_list:
    password+=i 

print(password)