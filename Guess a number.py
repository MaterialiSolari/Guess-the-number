import random
import math

lower = int(input("Enter Lower bound:- "))
 
upper = int(input("Enter Upper bound:- "))

target_number = random.randint(lower,upper)
print("\n\tYou've only ", 
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
count = 0
max_attempts = math.log(upper - lower + 1,2)
while count < max_attempts :
     
    guess = int(input("Guess a number:"))
        
    if guess == target_number:
        print(f'You win!\n You did it in {count} tries')
        break
    
    elif (guess < lower) or (guess > upper):
        print(f'Guess number can not be lower than {lower} or higher than {upper}')
    
    elif guess < target_number:
        print('Too small')
    else:
        print('Too large')
    count += 1
           
if count >= max_attempts:
    print(f'The number is {target_number}')
    print('Try your luck another day')