#
#= Open file - Option 1
# my_file = open('my_txt.txt')

#_ Read all lines
# print(my_file.read())
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

#_ Read line by line
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

#_ Read all lines and return as a list
# print(my_file.readlines())
# my_file.close()

#= Open file - Option 2
try:
    with open('my_txt2.txt', mode='r') as my_file:
        text = my_file.readline()
        print(text)
except FileNotFoundError as err:
    print("FileNotFoundError - File does not exist")
    raise err
except IOError as err:
    print("IOError - Something went wrong")
    raise err