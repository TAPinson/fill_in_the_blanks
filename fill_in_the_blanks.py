import os

# Global lists that will be fed the correct lists after a level is selected by the user. The game_engine function will check
# responses against these lists
quiz = []
answers = []


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
    blank_one = quiz[2]
    blank_two = quiz[9]
    blank_three = quiz[13]
    blank_four = quiz[24]
    answer_one = answers[0]
    answer_two = answers[1]
    answer_three = answers[2]
    answer_four = answers[3]
    first_spot = 2
    second_spot = 9
    third_spot = 13
    fourth_spot = 24
    response = raw_input('Fill in the blank: ')
    if response == answer_one:
        quiz.remove(blank_one)
        quiz.insert(first_spot, response)
        print ' '.join(quiz)
        return game_engine(quiz,answers)
    elif response == answer_two:
        quiz.remove(blank_two)
        quiz.insert(second_spot,response)
        print ' '.join(quiz)
        return game_engine(quiz, answers)
    elif response == answer_three:
        quiz.remove(blank_three)
        quiz.insert(third_spot,response)
        print ' '.join(quiz)
        return game_engine(quiz, answers)
    elif response == answer_four:
        quiz.remove(blank_four)
        quiz.insert(fourth_spot,response)
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
        with open("easy-quiz.txt","r") as myquiz:
            loadquiz = myquiz.read().replace('\n', '')
            quiz = loadquiz.split()
            print loadquiz
            with open ("easy-answers.txt","r") as myanswers:
                loadanswers = myanswers.read().replace ('\n', '')
                answers = loadanswers.split()
                return game_engine(quiz,answers)
    else:
        return opening_prompt()


opening_prompt(quiz, answers)
# We will start the game by launching the opening_prompt function


### Travis Pinson
### travispinson@gmail.com