import random


# TODO: Decompose into functions
#global variables:
code = [0,0,0,0] # creates code
answer = '' # use to store user input answer
correct_digits_and_position = 0 # keep track of correct digits and position
correct_digits_only = 0 # keeps track of correct digits but off position
correct = False # for stating user input as being correct
turns = 0   # keeps track of the amount of turns user has left to guess code

def generate_code():
    '''
    Generates code to be guessed by the user
    
    '''
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def enter_code():
    '''
    Gets user input
    '''
    global answer 
    while True:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
        else:
            break
    
def correct_digits_pos():
    '''
    Keeps track of number of correct digits and their position 
    with respect to the code
    '''
    global correct_digits_and_position
    global correct_digits_only
    global code
    global answer
    
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))

def check_code():
    '''
    Check whether user guess is correct
    '''
    global correct
    global turns
    while not correct and turns < 12:
        enter_code()
        correct_digits_pos()
        turns += 1
        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns)) 
    print('The code was: '+str(code))

def run_game():
    '''
    Starts the game
    Calls the necessary functions
    '''
    generate_code()
    check_code()

if __name__ == "__main__":
    run_game()
