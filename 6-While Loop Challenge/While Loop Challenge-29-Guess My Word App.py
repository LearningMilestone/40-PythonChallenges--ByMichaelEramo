#Reference : The Art of Doing Computer Science Through Python Application udemy course by Michael P. Eramo
#While Loops Challenge 29: Guess the Word App
import random

print("Welcome to the Guess My Word App")

#Create the dict to hold our words
game_dict = {
    "sports":['basketball', 'baseball', 'soccer', 'football', 'tennis',
                'curling'],
"colors":['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
"fruits":['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
"classes":['english', 'history', 'science', 'mathematics', 'art', 'health'],
}

#create a blank list
game_keys=[]
for key in game_dict:
    game_keys.append(key)

#flag variable to control while loop running
running=2
while running<=5:
    game_category=random.choice(game_keys)
    game_word=random.choice(game_dict[game_category])

    running+=1
    #create another empty list
    blank_word=[]
    for letter in game_word:
        blank_word.append('-')
    #print(game_category,game_word,blank_word)
    print("Guess a " + str(len(game_word)) + " letter word from the following category: " + game_category.title())

    #let's keep track of user guesses

    guess=''
    guess_count=0
    while guess!=game_word:
        print("".join(blank_word))
        guess = input("\nEnter your guess: ").lower()
        guess_count+=1
        #Guess is correct, user won the game
        if guess == game_word:
            print("\nCorrect! You guessed the word in " + str(guess_count) + " guesses.")
            break
        else:
            print("That is not correct. let us reveal a letter to help you!")
            #Loop to replace "-" in blank_word to reveal a letter to help user
            swapping = True
        while swapping:
                letter_index = random.randint(0, len(game_word)-1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    swapping = False
    #Ask the user to play again
    choice = input("\nWould you like to play again (y/n): ").lower()
    if choice != 'y':
        playing = False
        print("Thank you for playing the game.")