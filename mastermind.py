import random

d_c_place = 0
d_inc_place = 0
turns_left = 12
list = []
u_input = ''

def generate_code(): 
    """
    Creates the random code for the game
    """
    global list
    list = [0,0,0,0]

    c = 0
    while c < 4:
        digit = random.randint(1,8)
        while digit in list:
            digit = random.randint(1,8)
        list[c] = digit
        c += 1

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def enter_code():
    """
    Prompts the user to enter a code(guess)
    Check user input for validity
        code must must be 4 characters long
    """
    global u_input
    u_input = input('Input 4 digit code: ')
    while True:
        if len(u_input) != 4:
            print('Please enter exactly 4 digits.')
            u_input = input('Input 4 digit code: ')
            continue
        break

def check_zeros():
    """
    Check the user input for zero's
    """
    global u_input
    control_var = True
    while control_var:
        for i in u_input:
            if int(i) not in range(1,9):
                print('Please enter exactly 4 digits.')
                u_input = input('Input 4 digit code: ')
                break
            else:
                control_var = False
                continue

def check_code():
    """
    Compare user input to the randomly generated code
    Updates user with each iteration on number of correct digits and their position
    Prints out 'Congratulations...' if user guesses the code
    Iterates a maximum of 12 times
    """
    global u_input
    global d_c_place
    global d_inc_place
    global turns_left

    d_c_place = 0
    d_inc_place = 0
    turns_left = 12
    while d_c_place != 4 and turns_left != 0:
        for i in u_input:
            if int(i) in list:
                if u_input.index(i) == list.index(int(i)):
                    d_c_place += 1
                else:
                    d_inc_place += 1
        print('Number of correct digits in correct place:     {}'.format(d_c_place))
        print('Number of correct digits not in correct place: {}'.format(d_inc_place))
        if d_c_place == 4:
            print('Congratulations! You are a codebreaker!')
            print('The code was: {}'.format(list))
        else:
            d_c_place = 0
            d_inc_place = 0
            turns_left -= 1
            print('Turns left: {}'.format(turns_left))
            if turns_left == 0:
                break
            u_input = input('Input 4 digit code: ')
    pass

def run_game():
    """
    Function to run the game
    """
    generate_code()
    enter_code()
    check_zeros()
    check_code()
    
if __name__ == "__main__":
    run_game()
