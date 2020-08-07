import re

string = 'search this inside of this text please!'

try:
    match = re.search('this', string)
    print(match)
    print('Where the string occurs, between', match.span())
    print('Where the string starts, on index', match.start())
    print('Where the string ends, on index', match.end())
    print('Returns the part that was the match', match.group())
except AttributeError as error:
    print('Match not found')
    raise error

try:
    pattern = re.compile('search this inside of this')
    print(pattern.search(string))
    print('Returns a list of matches, ', pattern.findall(string))
    print('Only full match will be returned,', pattern.fullmatch(string))
    print('Returns partial match', pattern.match(string))
except AttributeError as error:
    print('Match not found')
    raise error


email = 'hi my name is roger, my email is roger@roger.com'
try:
    pattern = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z0-9]$)')
    print(pattern.search(email))
    print('Returns a list of matches, ', pattern.findall(email))
except AttributeError as error:
    print('Match not found')
    raise error

password = 'RraasZ$#@8'
try:
    pattern = re.compile(r'([a-zA-Z$%#@]{8,}\d+)')
    match = pattern.fullmatch(password)
    if match:
        print(f'Your password is {password}')
    else:
        print('Invalid password, make sure you password has at least 8 characters long. Available special characters $%#@ and has to end with a number')
except AttributeError as error:
    print('Match not found')
    raise error
