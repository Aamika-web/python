import random
guesstaken = 0
print("hello! What is your name?")
myname = input()
number = random.randint(1,20)


while guesstaken <6:
    print("take a guess")
    guess = input()
    guess = int(guess)
    guesstaken = guesstaken + 1

    if guess < number :
        print("your guess is too low")
    if guess > number:
        print("your guess is too high")
    if guess == number :
        break
if guess == number:
    guesstaken = str(guesstaken)
    print ('Good job, ' + myname + '! You guessed my number in ' + guesstaken + ' guesses!')

if guess!= number :
    number = str(number)
    print("nope.try again" +  number)
