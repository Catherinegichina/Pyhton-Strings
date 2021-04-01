import random
num_of_guesses = 0
print("Hello!,What is your name")
name = input()
number = random.randint(1,20)
print("Number i am thinking of is betwen 1 and 20" ,name)
while num_of_guesses < 6:
     print("Take a Guess. ")
     guess = input()
     guess = int(guess)
     num_of_guesses = num_of_guesses + 1
if guess < number :
    print ("Number is too low")
elif guess > number:
    print("Number is too high")
else guess == number:
             if  num_of_guesses = str(num_of_guesses)
               print("well Done " ,name,"You guessed the number in: " , num_of_guesses)
           guess != number:
                 else  number = str(number)
                 print("Wrong!Unlucky,The number was: " ,number)