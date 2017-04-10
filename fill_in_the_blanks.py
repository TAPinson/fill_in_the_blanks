import os

# Global lists that will be fed the correct lists after a level is selected by the user. The game_engine function will check
# responses against these lists
quiz = []
answers = []

blank_one = "___1___"
blank_two = "___2___"
blank_three = "___3___"
blank_four = "___4___"
blank_five = "___5___"

# Inputs: User is prompted to play again. # Outputs: If user elects to play again, global variables quiz and
# answers are emptied and user is returned to the opening prompt
def next_level():
    play_more = ['Y','y','Yes','YES','ok','OK','yeah','yes']
    dont_play_more = ['N','n','No','NO','nah','NAH', 'nope','no']
    response = raw_input('Would you like to play again?')
    if response in play_more:
        quiz = []
        answers = []
        opening_prompt(quiz,answers)
    elif response in dont_play_more:
        print 'goodbye'
    else:
        print "Invalid selection. Try again."
        return next_level()


# Outputs: global quiz variable printed with a .join. after replacing the blank with the corresponding word from
# the global answers list. Once blanks are filled, user is referred to next_level function
def game_engine(quiz,answers):
    response = raw_input("Fill in the Blank:")
    if response == answers[0]:
        quiz = [blank.replace(blank_one, response) for blank in quiz]
        print ' '.join(quiz)
        return game_engine(quiz,answers)
    elif response== answers[1]:
        quiz = [blank.replace(blank_two, response) for blank in quiz]
        print ' '.join(quiz)
        return game_engine(quiz, answers)
    elif response == answers[2]:
        quiz = [blank.replace(blank_three, response) for blank in quiz]
        print ' '.join(quiz)
        return game_engine(quiz, answers)
    elif response == answers[3]:
        quiz = [blank.replace(blank_three, response) for blank in quiz]
        print ' '.join(quiz)
        return next_level()
    else:
        print 'incorrect. Try again.'
        return game_engine(quiz,answers)


# Inputs: user is prompted for response for difficulty.
# Outputs: based on difficulty chosen, the global quiz list and answers list will be populated with the correct contents.
def opening_prompt(quiz,answers):
    response = raw_input('Would you like to play?(yes/no): ')
    if response == 'yes':
            with open ("easy-quiz.txt", "r") as quiz:
                quiz = quiz.read().replace('\n', '')
                quiz = quiz.split()
                print ' '.join(quiz)
            with open ("easy-answers.txt","r") as answers:
                answers = answers.read().replace ('\n', '')
                answers = answers.split()

                return game_engine(quiz,answers)
    else:
        return opening_prompt(quiz,answers)
        #return opening_prompt(quiz,answers)

opening_prompt(quiz, answers)
# We will start the game by launching the opening_prompt function


### Travis Pinson
### travispinson@gmail.com
