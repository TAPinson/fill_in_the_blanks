### LIST BANK###
# Lists to use for 'easy' level ########################################################################################
easy_quiz = ['Build strong','___1___','solving skills! Start with finding the','___2___','. Then find the','___3___','. The only thing left to do now is to','___4___','the problem.']
easy_answers = ['problem','inputs','outputs','solve']

# Lists to use for 'medium' level #####################################################################################
medium_quiz = ['Defining a','___1___','is important to coding in','___2___','. Learning that your','___3___','arent global until you call the function with its','___4___','is equally important!']
medium_answers = ['function','python','variables','parameters']

# Lists to use for 'hard' level ########################################################################################
hard_quiz = ['To change a','___1___','variable, it needs to be processed by a',' ___2___','. Otherwise, it will remain ','___3___','to the original declaration. Process the variable change by','___4___ ','it as a parameter or the function.']
hard_answers = ['global','function','equal','calling']

########################################################################################################################
# Global lists that will be fed the correct lists after a level is selected by the user. The game_engine function will check
# responses against these lists
quiz = []
answers = []



########################################################################################################################
# Inputs: User is prompted to respond if they want to play again.
# Outputs: If user elects to play again, global variables quiz and answers are emptied and user is returned to the
            # opening prompt to play again

def next_level():
    play_more = ['Y','y','Yes','YES','ok','OK','yeah']
    dont_play_more = ['N','n','No','NO','nah','NAH', 'nope']
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

########################################################################################################################
# Inputs: global variable lists: quiz and answers
# Outputs: global quiz variable printed with a .join.  After replacing the blank with the corresponding word from
    # the global answers list. Once blanks are filled, user is referred to next_level function
# quiz inserts replacement at odd numbered locations to correspond with every/other for BlahBlah,___,BlahBlah,___,etc
def game_engine(quiz,answers):
    blank_one = quiz[1]
    blank_two = quiz[3]
    blank_three = quiz[5]
    blank_four = quiz[7]
    answer_one = answers[0]
    answer_two = answers[1]
    answer_three = answers[2]
    answer_four = answers[3]
    first_spot = 1
    second_spot = 3
    third_spot = 5
    fourth_spot = 7
    response = raw_input('Fill in the blank: ')
    if response == answer_one:
        quiz.remove(blank_one)
        quiz.insert(first_spot,response)
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

########################################################################################################################
# Inputs: user is prompted for response for difficulty.
# Outputs: based on difficulty chosen, the global quiz list and answers list will be populated with the correct contents.

def opening_prompt(quiz,answers):
    response = raw_input('Choose a difficulty: ( easy | medium | hard ): ')
    while response == 'easy':
        quiz.extend(easy_quiz)
        answers.extend(easy_answers)
        print ' '.join(easy_quiz)
        return game_engine(quiz,answers)
    while response == 'medium':
        quiz.extend(medium_quiz)
        answers.extend(medium_answers)
        print ' '.join(medium_quiz)
        return game_engine(quiz,answers)
    while response == 'hard':
        quiz.extend(hard_quiz)
        answers.extend(hard_answers)
        print ' '.join(hard_quiz)
        return game_engine(quiz,answers)
    else:
        print 'incorrect, Try again.'
        return opening_prompt(quiz,answers)

########################################################################################################################
# We will start the game by launching the opening_prompt function
opening_prompt(quiz,answers)

### Travis Pinson
### for Udacity 