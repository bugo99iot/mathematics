import random  

# set the initial values from 1 to 50
the_number = random.randrange(50) + 1
guess = int(raw_input("Take a guess: "))
tries = 1

# guessing loop
while (guess != the_number):
    if (guess > the_number):
        print "Lower..."
    else:
        print "Higher..."
            
    guess = int(raw_input("Take a guess: "))
    tries += 1

print "You guessed it!  The number was %d" % (the_number)
print "And it only took you", tries, "tries!\n"
