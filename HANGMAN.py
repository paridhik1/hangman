
#welcoming the user
name = raw_input("What is your name? ")
 
print "Hello, " + name, "Time to play hangman!"
#explaining the rules of the game
print "The rules are simple. This is a seven-lettered word."
print "Try and guess the secret word by entering the characters one by one!"
print "You have only 10 tries!"
print "Let's begin!"
 
print "\n"
 
#setting up a secret word for the user to guess
word = "hangman"
 
#creation of a variable with an empty value
guesses = ''
 
#setting the number of turns
turns = 10
 
#Create a while loop to check if the turns are more than zero
while turns > 0:         
 
    #make a counter that starts with zero
    failed = 0             
 
    # for every character in the secret word    
    for char in word:      
 
    # see if the character is in the players guess
        if char in guesses:    
    
        # then print then out the character
            print char,    
 
        else:
    
        # if not found, print a dash 
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    
 
    # if failed is equal to zero
    if failed == 0:        
        print "\nYou won!"  
 
   
 
 
 
 
 
 #exit the script
        break              
 
    print
 
    # ask the user go guess a character
    guess = raw_input("Guess a character:") 
 
    # set the players guess to guesses
    guesses += guess                    
 
    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print "Wrong guess!\n"    
 
    # how many turns are left
        print "You have", + turns, 'more guesses.' 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print "Sorry, you lost!\n"
