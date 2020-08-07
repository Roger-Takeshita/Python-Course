import sys
from random import randint

def run_guess(guessed_number, rand_number):
    if (guessed_number == rand_number):
        print(f'You found the right number {rand_number}')
        return True
    elif guessed_number > rand_number:
        print('You guessed to high')
        return False
    else:
        print('You guessed to low')
        return False

if __name__ == '__main__':    
    try:
        num_start = int(sys.argv[1])
        num_end = int(sys.argv[2])
    except ValueError:
        print('Please enter a valid number')
    else:
        if num_start <= 0:
            print('Start number should be greater than 0 ')
        elif num_end > 100:
            print('End number should be less or equal to 100')
        elif num_start >= num_end:
            print('Start number should be less than end number')
        else:
            rand_number = randint(num_start, num_end)
            print(f'Please guess a number between {num_start} and {num_end}')
            
            while (True):
                try:
                    guessed_number = int(input('Your guess = '))
                except ValueError:
                    print('Please enter a valid number')
                    continue
                else:
                    if (run_guess(guessed_number, rand_number)):
                        break
