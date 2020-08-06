import sys

# first_arg = sys.argv[0]  # file name
# second_arg = sys.argv[1] # first argument
# third_arg = sys.argv[2]  # second argument
# print(first_arg, second_arg, third_arg)

def print_arguments(array):
    if len(array) == 1:
        print('Please add some arguments')
    else:
        for i in array:
            print(i)

print_arguments(sys.argv)
