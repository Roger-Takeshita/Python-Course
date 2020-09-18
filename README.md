<h1 id='summary'>Summary</h1>

- [PYTHON](#python)
  - [Environment Variables](#environment-variables)
  - [Basics](#basics)
    - [Data Types](#data-types)
      - [Binary Representation](#binary-representation)
      - [Strings](#strings)
        - [PRINT MULTIPLE LINES](#print-multiple-lines)
        - [ESCAPE SEQUENCE](#escape-sequence)
        - [STRING INTERPOLATION](#string-interpolation)
        - [STRING INDEXES](#string-indexes)
        - [IMMUTABILITY](#immutability)
      - [Built-in Functions](#built-in-functions)
    - [Lists](#lists)
      - [List Slicing](#list-slicing)
      - [List Methods](#list-methods)
      - [List Unpacking](#list-unpacking)
    - [Dictionary](#dictionary)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Ternary Operator](#ternary-operator)
    - [== vs is](#-vs-is)
    - [Iterables](#iterables)
      - [Range](#range)
      - [Enumerate](#enumerate)
    - [While/Else](#whileelse)
    - [Functions](#functions)
      - [Keyword Arguments vs Positional Arguments](#keyword-arguments-vs-positional-arguments)
      - [Default Parameters](#default-parameters)
      - [Docstrings](#docstrings)
      - [*args *kwargs](#args-kwargs)
      - [Anonymous Function](#anonymous-function)
  - [Advanced](#advanced)
    - [Classes](#classes)
      - [Attributes and Methods](#attributes-and-methods)
      - [Overriding Methods](#overriding-methods)
      - [@classmethod and @staticmethod](#classmethod-and-staticmethod)
        - [@classmethod](#classmethod)
        - [@staticmethod](#staticmethod)
      - [Private and Public Variables](#private-and-public-variables)
      - [Inheritance](#inheritance)
      - [isinstance()](#isinstance)
      - [super()](#super)
    - [Functional Programming](#functional-programming)
      - [Pure Function](#pure-function)
      - [map()](#map)
      - [filer()](#filer)
      - [zip()](#zip)
      - [reduce()](#reduce)
      - [Lambada Expressions](#lambada-expressions)
    - [List Comprehensions](#list-comprehensions)
      - [Dictionary Comprehension](#dictionary-comprehension)
    - [Decorators](#decorators)
      - [How Decorators Are Build?](#how-decorators-are-build)
      - [@classmethod](#classmethod-1)
      - [@staticmethod](#staticmethod-1)
      - [Custom Decorator](#custom-decorator)
    - [Error Handling](#error-handling)
      - [Try/Except](#tryexcept)
      - [Specific Error](#specific-error)
      - [Multiple Errors](#multiple-errors)
      - [Complete Try/Except Structure](#complete-tryexcept-structure)
      - [Raise an Error](#raise-an-error)
    - [Generators](#generators)
- [PYTHON MODULES](#python-modules)
  - [Python Package](#python-package)
      - [Different Ways To Import](#different-ways-to-import)
    - [\_\_name\_\_](#__name__)
- [DEBUGGING](#debugging)
- [WORKING WITH FILES](#working-with-files)
  - [Option 1](#option-1)
    - [Read All Lines - .read()](#read-all-lines---read)
    - [Read Single Line - .readline()](#read-single-line---readline)
    - [Read All Lines as a List - .readlines()](#read-all-lines-as-a-list---readlines)
  - [Option 2](#option-2)
    - [Read and Write Files - mode='r+'](#read-and-write-files---moder)
    - [Append Files - mode='a'](#append-files---modea)
    - [Write Files - mode='w'](#write-files---modew)
  - [Paths](#paths)
  - [Handling File Errors](#handling-file-errors)
- [REGEX](#regex)
- [TESTING](#testing)
  - [Unittest](#unittest)
  - [Run Multiple Test Files](#run-multiple-test-files)
  - [setUp(self)](#setupself)
  - [tearDown(self)](#teardownself)
- [PIL - IMAGE PROCESSING](#pil---image-processing)
  - [Install PIL](#install-pil)
  - [PIL Basics](#pil-basics)
  - [Image Converter (jpg to png)](#image-converter-jpg-to-png)
- [PyPDF2 - PDF](#pypdf2---pdf)
  - [Install PyPDF2](#install-pypdf2)
  - [PDF Basics](#pdf-basics)
  - [Merge/Combine PDFs](#mergecombine-pdfs)
  - [Watermaker PDF](#watermaker-pdf)
- [smtplib - EMAIL](#smtplib---email)
  - [SMTP Protocol](#smtp-protocol)
  - [Using smtplib](#using-smtplib)
    - [String Template](#string-template)
- [hashlib - HASH PASSWORD](#hashlib---hash-password)
  - [Password Checker](#password-checker)
- [WEB SCRAPING](#web-scraping)
  - [Check What I Can Scrape](#check-what-i-can-scrape)
  - [BeautifulSoup](#beautifulsoup)
    - [BeautifulSoup Basics](#beautifulsoup-basics)
    - [Simple Scraper](#simple-scraper)
- [FLASK](#flask)
  - [Flask Links](#flask-links)
  - [Flask vs. Django](#flask-vs-django)
  - [New Project](#new-project)
    - [Start Server](#start-server)
    - [Flask Templates](#flask-templates)
      - [Static Folder - CSS / JavaScript](#static-folder---css--javascript)
        - [favicon](#favicon)
      - [Variable Rules](#variable-rules)
    - [Request Module](#request-module)
      - [The Request Object](#the-request-object)
    - [Redirect Module](#redirect-module)
    - [Database](#database)
      - [TXT](#txt)
      - [CSV](#csv)
  - [Deploying / Saving to GitHub](#deploying--saving-to-github)
    - [requirements.txt](#requirementstxt)
    - [.gitignore](#gitignore)
- [SELENIUM](#selenium)
  - [Selenium Links](#selenium-links)
  - [Installation Selenium](#installation-selenium)
  - [Drivers](#drivers)
    - [webdriver](#webdriver)
  - [Modules](#modules)
  - [Browser Arguments](#browser-arguments)
    - [Auto Download](#auto-download)
    - [Disable Notifications in FireFox](#disable-notifications-in-firefox)
    - [Open Specific Browser Using Binary](#open-specific-browser-using-binary)
  - [Selenium Commands](#selenium-commands)
    - [Read Browser Details](#read-browser-details)
    - [Go to a Specified URL](#go-to-a-specified-url)
    - [Locating Elements](#locating-elements)
      - [Python Selenium Commands for Operation on Elements](#python-selenium-commands-for-operation-on-elements)
    - [Waits](#waits)
      - [Expected Conditions](#expected-conditions)
      - [Custom Wait Conditions](#custom-wait-conditions)
      - [Explicit Waits](#explicit-waits)
      - [Implicit Waits](#implicit-waits)

# PYTHON

## Environment Variables

[Go Back to Summary](#summary)

- Go to the root of the computer

  ```Bash
      code ~/.bash_profile
  ```

- Add a new environment variable

  ```Bash
      #= API KEYS
      export TWITTER_API_KEY=tqNGASDFASDFASDFWdGtSRd
      export TWITTER_API_SECRET_KEY=2ue9keWGASDFASDFASDFASDFWTzvaVTqDz
      export TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAANNOHwEAAAAAFFASDFASDGASDFASD37dTsDOWqcHSWQufqn2CeZFTD2rskligz22AbjB
      export TWITTER_ACCESS_TOKEN=243122725-NzG9fasdfWwsUc5of1Fg3jodfasdfNQVV5bH
      export TWITTER_ACCESS_TOKEN_SECRET=mcL2pfasdfasdfL3K7ofasdfasdffas1231fasdfdDY1
  ```

- Importing environment variables

  - In your python file, import the `environ` from `os`

    ```Python
        from os import environ

        print(environ.get('TWITTER_API_KEY'))
    ```

## Basics

### Data Types

[Go Back to Summary](#summary)

- In **Python** we have the following data types:
  - int
  - float
  - bool
  - str
  - list
  - tuple
  - set
  - dict
  - complex (imaginary numbers)

#### Binary Representation

[Go Back to Summary](#summary)

```Python
  bin(5)
```

- Gives us the binary representation of `5`, that is `0b101` -> `0b` represents in python the this is a `binary number` the actual binary is number is `101`

- to convert a `binary number` into an `integer` we can use the `int()` with the base of `2`

  ```Python
    int('0b101', 2)
  ```

#### Strings

[Go Back to Summary](#summary)

##### PRINT MULTIPLE LINES

- Use `'''` to print multiple lines

  ```Python
    multiple_lines = '''
    print
    multiple
    lines
    '''
    print(multiple_lines)
  ```

##### ESCAPE SEQUENCE

- To escape a special character we use `\` before the character

  ```Python
    weather = "It\'s \"kind of\" sunny"
    print(weather)
  ```

  - `\t` - Tab
  - `\n` - New Line
  - `\\` - Backslash
  - `\r` - Carriage Return
  - `\b` - Backspace
  - `\f` - Form Feed
  - `\ooo` - Octal value
  - `\xhh` - Hex value

##### STRING INTERPOLATION

- Using **Python 3** format

  ```Python
    name = 'Roger'
    age = 33

    print(f'Hi {name}. You are {age} years old')
  ```

- Using **Python 2** format

  - **ATTENTION** the `.format()` is right after the string. The `.format()` will evaluate the `string`

  ```Python
    name = 'Roger'
    age = 33

    print('Hi {0}. You are {1} years old'.format(name, age))
  ```

- Using `custom variables`

  - Using custom variables we have to call them between `{}`

  ```Python
    print('Hi {new_name}. You are {new_age} years old'.format(new_name="Yumi", new_age=3))
  ```

##### STRING INDEXES

- To work with string we have `[start:stop:stepover]`

  - the `start` starts at index `0`
  - `stepover`, by default the step over is `1` but we can choose any number of our choice

  ```Python
    numbers = '0123456'

    print(numbers[1:])
    # 123456
    print(numbers[:3])
    # 012
    print(numbers[::1])
    # 0123456
    print(numbers[-1])
    # 6
    print(numbers[::-1])
    # 6543210
  ```

##### IMMUTABILITY

- String are immutable, this means that once we assign a value to a string we cannot change the content (different from JavaScript), the only way to change the string content is to re-assign a complete new value to the variable

#### Built-in Functions

[Go Back to Summary](#summary)

|               |             | Built-in Functions |              |                |
| ------------- | ----------- | ------------------ | ------------ | -------------- |
| abs()         | delattr()   | hash()             | memoryview() | set()          |
| all()         | dict()      | help()             | min()        | setattr()      |
| any()         | dir()       | hex()              | next()       | slice()        |
| ascii()       | divmod()    | id()               | object()     | sorted()       |
| bin()         | enumerate() | input()            | oct()        | staticmethod() |
| bool()        | eval()      | int()              | open()       | str()          |
| breakpoint()  | exec()      | isinstance()       | ord()        | sum()          |
| bytearray()   | filter()    | issubclass()       | pow()        | super()        |
| bytes()       | float()     | iter()             | print()      | tuple()        |
| callable()    | format()    | len()              | property()   | type()         |
| chr()         | frozenset() | list()             | range()      | vars()         |
| classmethod() | getattr()   | locals()           | repr()       | zip()          |
| compile()     | globals()   | map()              | reversed()   | **import**()   |
| complex()     | hasattr()   | max()              | round()      |                |

### Lists

[Go Back to Summary](#summary)

- **Lists** are like **Arrays** in other languages, it's an ordered list

#### List Slicing

[Go Back to Summary](#summary)

- With **list slicing** we **create a new list**

  - One way to create a new list with all the values from the previous list is by adding `[:]`

  ```Python
    amazon_cart = [
      'notebook',
      'sunglass',
      'toys',
      'grapes'
    ]

    new_list = amazon_cart[:]
    print(new_list)
    # ['notebook', 'sunglass', 'toys', 'grapes']

    # another option is to use .copy();
    new_list2 = amazon_cart.copy();
    print(new_list2)
    # ['notebook', 'sunglass', 'toys', 'grapes']
  ```

#### List Methods

[Go Back to Summary](#summary)

- the `.append()` method changes the list in place, it doesn't return a new new copy of the list modified.

  ```Python
    basket = [1, 2, 3, 4, 5]

    new_list = basket.append(100)
    print(basket)
    print(new_list)
    # [1, 2, 3, 4, 5, 100]
    # None
  ```

- the `.insert()` method inserts a new item base on the index.

  - Just like `.append()`, `.insert()` modifies the list in place (it doesn't return anything)

  ```Python
    basket = [1, 2, 3, 4, 5]

    basket.insert(3, 100)
    print(basket)
    # [1, 2, 3, 100, 4, 5]
  ```

- the `.extend()` method extends the list, in other words, it concatenates two objects (lists)

  - `.extend()` modifies the list in place

  ```Python
    basket = [1, 2, 3, 4, 5]

    basket.extend([100, 101])
    print(basket)
    # [1, 2, 3, 4, 5, 100, 101]
  ```

- the `.pop()` method removes the **index** from the list and return the removed item

  ```Python
    basket = [1, 2, 3, 4, 5]

    removed_item = basket.pop(3)
    print(removed_item)
    # 4
  ```

- the `.remove()` method removes the **value** of the list, but doesn't return anything

  ```Python
    basket = [1, 2, 3, 4, 5]

    basket.remove(3)
    print(basket)
    # [1, 2, 4, 5]
  ```

- the `.clear()` method removes everything in place from the list.

  ```Python
    basket = [1, 2, 3, 4, 5]

    basket.clear()
    print(basket)
    # []
  ```

- the `.index()` method, return the index of the item that we are search on the list

  ```Python
    basket = [1, 2, 3, 4, 5]

    print(basket.index(2))
    # 1
  ```

  - We can also give a start and stop point to search for the item
  - `.index(value, start, stop)`

- the `'value' in object/list`, we can check True/False if the item exists in the list

  ```Python
    basket = ['a', 'b', 'c', 'd', 'e']

    print('a' in basket)
    # True
    print('f' in basket)
    # False
  ```

- the `.count()` method counts how many time the item occurs

  ```Python
    basket = ['a', 'b', 'c', 'd', 'e' , 'd']

    print(basket.count('d'))
    # 2
  ```

- the `.sort()` method sorts the list in place

  ```Python
    basket = ['a', 'b', 'c', 'd', 'e' , 'd']

    basket.sort()
    print(basket)
    # ['a', 'b', 'c', 'd', 'd', 'e']
  ```

- the `sorted()` function do the same thing as `.sort()` but it creates a new sorted array

  ```Python
    basket = ['a', 'b', 'c', 'd', 'e' , 'd']

    print(sorted(basket))
    print(basket)
    # ['a', 'b', 'c', 'd', 'd', 'e']
    # ['a', 'b', 'c', 'd', 'e', 'd']
  ```

- the `.reverse()` method reverts the list in place

  ```Python
    basket = ['a', 'b', 'c', 'd', 'e' , 'd']

    basket.reverse()
    print(basket)
    # ['d', 'e', 'd', 'c', 'b', 'a']
  ```

- create a list using `range()`

  ```Python
    new_list = list(range(1, 100));
    print(new_list)
  ```

- the `.join()` method iterates through the list and add join with the left part (sentence in this case)

  ```Python
    sentence = ' '
    new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'roger'])

    print(new_sentence)
    # hi my name is roger

    # alternative
    new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'roger'])

    print(new_sentence)
    # hi my name is roger
  ```

#### List Unpacking

[Go Back to Summary](#summary)

- We can assign variables to each item of the list

  ```Python
    a, b, c, *other, last_item = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(a)
    print(b)
    print(c)
    print(other)
    print(last_item)
    # 1
    # 2
    # 3
    # [4, 5, 6, 7, 8]
    # 9
  ```

### Dictionary

[Go Back to Summary](#summary)

- **Dictionary** is equal to an **object** in `JavaScript`, it's un-ordered key/value pairs

  ```Python
    dictionary = {
      'a': 1,
      'b': 2
    }

    print(dictionary['a'])
    # 1
  ```

- the `.get()` method accepts the first argument is the `key` that we are looking for, if not found we can assign a default value (second argument).

  ```Python
    user = {
        'basket': [1, 2, 3],
        'greet': 'hello',
    }

    print(user.get('age',55))
    # 55

    user2 = {
        'basket': [1, 2, 3],
        'greet': 'hello',
        'age' : 20
    }

    print(user.get('age',55))
    # 20
  ```

- `<value> in dict.key()`, loops through the dictionary and checks if the **key** exists

  ```Python
    user = {
        'basket': [1, 2, 3],
        'greet': 'hello',
        'age': 20
    }

    print('hello' in user.keys())
    # false
    print('greet' in user.keys())
    # true
  ```

- `<value> in dict.value()`, loops through the dictionary and checks if the **value** exists

  ```Python
    user = {
        'basket': [1, 2, 3],
        'greet': 'hello',
        'age': 20
    }

    print('hello' in user.values())
    # true
  ```

- `dict.items()`, returns an array of **tuples** where the fist position (`[0]`) is the **key** and the second position (`[1]`) is the **value** (the value could be anything, number, string, object...)

  ```Python
    user = {
        'basket': [1, 2, 3],
        'greet': 'hello',
        'age': 20
    }

    print(user.items())
    # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
  ```

- `.clear()`, clear the object in place, it removes all the items of the object. In the end we have and **empty** object

- `.copy()` creates a brand new copy of the object (not referencing the pointer, it creates a new object)

- `.pop()` removes the target item and returns the removed item.

- `.update()` updates an existing item or adds if not exist

  ```Python
    user = {
        'basket': [1, 2, 3],
        'greet': 'hello',
        'age': 20
    }

    user.update({'age': 55})
    print(user)

    user.update({'ages': 100})
    print(user)
    # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55}
    # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55, 'ages': 100}
  ```

### Tuples

[Go Back to Summary](#summary)

- it's just like a list but we cannot change the content

  ```Python
    days_of_the_week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    shopping_cart = ['cucumbers', 'potatoes', 'celery', 'oranges', 'avocado', 'grapes', 'banana']

    days_of_the_week[0] = 'not monday'
    print(days_of_the_week)
    # TypeError: 'tuple' object does not support item assignment

    shopping_cart[2] = 'cheese'
    print(shopping_cart)
    # ['cucumbers', 'potatoes', 'cheese', 'oranges', 'avocado', 'grapes', 'banana']
  ```

- working we tuples, we only have 2 methods available
  - `.count()` returns how many times the item appeared
  - `.index()` returns the index of the item (the first found index)

### Sets

[Go Back to Summary](#summary)

- Removes all the duplicates from an "`object`"

  ```Python
    unique_set = {1, 3, 5, 4, 3, 2, 6}
    print(unique_set)
    # {1, 2, 3, 4, 5, 6}
  ```

- `.difference()` returns the difference (who is calling)

  ```Python
    my_set = {1, 2, 3, 4, 5}
    your_set = {4, 5, 6, 7, 8, 9, 10}

    print(my_set.difference(your_set))
    # {1, 2, 3}
  ```

- `.discard()` removes an item from the set

  ```Python
    my_set = {1, 2, 3, 4, 5}

    my_set.discard(5)
    print(my_set)
    # {1, 2, 3, 4}
  ```

- `.difference_update()` returns the difference (who is calling) and modifies the original set

  ```Python
    my_set = {1, 2, 3, 4, 5}
    your_set = {4, 5, 6, 7, 8, 9, 10}

    my_set.difference_update(your_set)
    print(my_set)
    # {1, 2, 3}
  ```

- `.intersection()` or `&` returns the intersection between two sets

  ```Python
    my_set = {1, 2, 3, 4, 5}
    your_set = {4, 5, 6, 7, 8, 9, 10}

    # alternative 1
    my_set.intersection(your_set)
    print(my_set)
    # {4, 5}

    # alternative 2
    print(my_set & your_set)
    # {4, 5}
  ```

- `.isdisjoint()` returns `true/false` where `true` means that the two sets don't have items in common

  ```Python
    my_set2 = {1, 2, 3, 4, 5}
    your_set2 = {6, 7, 8, 9, 10}

    print(my_set2.isdisjoint(your_set2))
    # True
  ```

- `.union()` or `|` concatenate two sets and remove duplicates

  ```Python
    my_set = {1, 2, 3, 4, 5}
    your_set = {4, 5, 6, 7, 8, 9, 10}

    print(my_set.union(your_set))
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
  ```

- `.issubset()` checks if the left part (who is calling) is a **subset** of the other set, returns `true/false`

  ```Python
    my_set3 = {4, 5}
    your_set3 = {4, 5, 6, 7, 8, 9, 10}

    print(my_set3.issubset(your_set3))
    # True
  ```

- `.issuperset()` checks if the left part (who is calling) is a **superset** of the other set, returns `true/false`

  ```Python
    my_set3 = {4, 5}
    your_set3 = {4, 5, 6, 7, 8, 9, 10}

    print(your_set3.issuperset(my_set3))
    # True
  ```

### Ternary Operator

[Go Back to Summary](#summary)

- [Ternary Operator - Official Docs](https://book.pythontips.com/en/latest/ternary_operators.html)
- Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not. They became a part of Python in version 2.4

  ```Python
    value_if_true if condition else value_if_false
  ```

  ```Python
    is_nice = True

    state = "nice" if is_nice else "not nice"
    print(state)
    # nice
  ```

### == vs is

[Go Back to Summary](#summary)

- `==` checks for equality value
- `is` checks for memory location

  ```Python
    print(True == True)
    print('1' == '1')
    print([] == [])
    print(10 == 10)
    print([1,2,3] == [1,2,3])
    # True
    # True
    # True
    # True
    # True

    print()
    print(True is True)
    print('1' is '1')
    print([] is [])
    print(10 is 10)
    print([1,2,3] is [1,2,3])
    # True
    # True
    # False
    # True
    # False
  ```

### Iterables

[Go Back to Summary](#summary)

- We can iterate through a `list/dictionary/tuples/sets/string` and use a shorthand to get the `key/value`

  ```Python
    user = {
      'name': 'Roger',
      'age': 33,
      'can_swim': False
    }

    for key, value in user.items():
      print(key, value)
    print()
    for value in user.values():
      print(value)
    print()
    for key in user.keys():
      print(key)
  ```

#### Range

[Go Back to Summary](#summary)

- We can use `range()` that creates a special kind of object that we can iterate
- `range(start, stop, step)`

  - by default the step is not specified is `1`

  ```Python
    for number in range(0,100):
      print(number)
  ```

#### Enumerate

[Go Back to Summary](#summary)

- Using enumerate, it gives us accesses to the index for the `list/dictionary/tuples/sets/string`

```Python
  for index, value in enumerate('Helllloooooo'):
    print(index, value)
```

### While/Else

[Go Back to Summary](#summary)

- We can use `else` condition with `while`. The `else` part will be only executed if the `while` loop executed successfully

  ```Python
    i = 0
    while i < 10:
      print (i)
      i += 1;
      break
    else:
      print('This msg will never be printed')

    # 0

    j = 0
    while j < 10:
      print (j)
      j += 1;
    else:
      print('This msg will be printed after 9')
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # This msg will be printed after 9
  ```

### Functions

[Go Back to Summary](#summary)

- **Function expressions do not exist in Python**

  - Every function in Python is defined using the **def** keyword and **are never assigned to variables** as in JavaScript.

  ```Python
    msg = 'Welcome home'
    def say_greetings(name, emoji):
      print(f'{msg}, {name} {emoji}')

    say_greetings('Roger', '👍🏻')
  ```

#### Keyword Arguments vs Positional Arguments

[Go Back to Summary](#summary)

- With `keywords` we don't need to pass the parameters in order as it appears

  ```Python
    msg = 'Welcome home'
    def say_greetings(name, emoji):
      print(f'{msg}, {name} {emoji}')

    say_greetings(emoji = '👍🏻', name = 'Roger')
  ```

#### Default Parameters

[Go Back to Summary](#summary)

- We can assign default parameters if none is given

  ```Python
    msg = 'Welcome home'
    def say_greetings(name = 'Guest', emoji = '😎'):
      print(f'{msg}, {name} {emoji}')

    say_greetings()
  ```

#### Docstrings

[Go Back to Summary](#summary)

- `Docstrings` is a way to add extra info / definitions to our function

  ```Python
    def extra_info_function(a):
      '''
      Info: this function prints param a
      '''
      print(a)

    extra_info_function('!!!!')
  ```

- an alternative, we can use `help()` to know more about the function, we just need to point to the function, ot execute the function (`()`)

  ```Python
    help(extra_info_function)
  ```

- we could also use `Dunder` or `Magic Methods`

  - Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: **init**, **add**, **len**, **repr** etc.
  - Python lets our classes inherit from built-in classes. An inheriting child class of a built-in shares all the same attributes, including methods as the built-in. We can take advantage of core built-in functionality, but customize selected operations through the use of magic methods.

  ```Python
    print(extra_info_function.__doc__)
  ```

#### *args *kwargs

[Go Back to Summary](#summary)

- **Rule**: `params`, `*args`, `default parameters`, `**kwargs`

  ```Python
    def super_func(*args, **kwargs):
      total = 0
      for items in kwargs.values():
        total += items
      return sum(args) + total

    print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))
    # 30
  ```

#### Anonymous Function

[Go Back to Summary](#summary)

- [More about Anonymous Function](https://realpython.com/python-lambda/)
- Python has a different sort of anonymous functions
- Python does have a the concept of **anonymous functions** but they are called **lambda functions**.
- Think of **lambda functions** as a JavaScript arrow function that implicitly returns a single expression's result.

  ```Python
    nums = [1, 3, 2, 6, 5]
    odds = list( filter(lambda num: num % 2, nums) )

    print(odds)
    #[1, 3, 5]
  ```

  ```Python
    double = lambda x: x * 2

    print(double(5))
    # 10
  ```

## Advanced

### Classes

[Go Back to Summary](#summary)

- Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
- The convention when we are creating a class is to capitalize the first letter of each word and singular.
- The `__init__` method (constructor) is instantiated every time we instantiate a new object of our class

  - In the constructor we could also create validations before creating the object, we could give default values

  ```Python
    class PlayerCharacter:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def run(self):
            print('run')

    player1 = PlayerCharacter('Roger', 33);
    print(player1.name)
    print(player1.age)
    player1.run()
  ```

#### Attributes and Methods

[Go Back to Summary](#summary)

```Python
  class PlayerCharacter:
      #! attribute
      membership = True

      #! constructor
      def __init__(self, name, age):
          # if (self.membership): #+ we could also access like this
          if (PlayerCharacter.membership):
              self.name = name  # attribute the constructor
              self.age = age

      #! method
      def shout(self):
          print(f'My name is {self.name}')

  player1 = PlayerCharacter('Roger', 33)
  player2 = PlayerCharacter('Thaisa', 32)
  player3 = PlayerCharacter('Yumi', 3)
  print(player1.shout())
  print(player2.shout())
  print(player3.shout())
```

#### Overriding Methods

[Go Back to Summary](#summary)

- We can change this behavior by overriding the `__str__` method that the print function calls automatically to obtain the string to print out.

  ```Python
    class PlayerCharacter:
        membership = True

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f'My custom print, player: {self.name}'

        def shout(self):
            print(f'My name is {self.name}')

    player1 = PlayerCharacter('Roger', 33)
    print(player1)
  ```

#### @classmethod and @staticmethod

[Go Back to Summary](#summary)

##### @classmethod

- **@classmethod** is decorator that we add before defining the class method
- with **@classmethod** we could instantiate a new object without the need to instantiate the class
- The naming convention of the first parameter is to use `cls` instead of `self`
- the first parameter is always `cls`, `cls` stands for **class**

  ```Python
    class PlayerCharacter:
        membership = True

        #! constructor
        def __init__(self, name, age):
            if (age > 18):
                self.name = name  # attribute the constructor
                self.age = age

        #! method
        def shout(self):
            print(f'My name is {self.name}')

        #! decorator
        #+ class method
        @classmethod
        def adding_new_member(cls, num1, num2):
            return cls('Tom', num1+num2)

    player3 = PlayerCharacter.adding_new_member(10, 11)
    print(player3.name)
    print(player3.age)
    # Tom
    # 21
  ```

##### @staticmethod

- **@staticmethod** works the same way as **@classmethod** the only difference is that we don't need to define the `cls` as first parameter because **@staticmethod** doesn't have access to the class properties.
- We just want to perform a certain method

  ```Python
    class PlayerCharacter:
        membership = True

        #! constructor
        def __init__(self, name, age):
            if (age > 18):
                self.name = name  # attribute the constructor
                self.age = age

        #! method
        def shout(self):
            print(f'My name is {self.name}')

        #! decorator
        #+ class method
        @classmethod
        def adding_new_member(cls, num1, num2):
            return cls('Tom', num1 + num2)

        #+ static method
        @staticmethod
        def sum_number(num1, num2):
            return num1 + num2

    print(PlayerCharacter.sum_number(1, 1))
    # 2
  ```

#### Private and Public Variables

[Go Back to Summary](#summary)

- Python doesn't have **public** and **private** variables that will prevent the user from changing the property of our class, but it's a convention to add `_` (single underscore) before the the variable that you want to indicate that is a private variable

  ```Python
    class PlayerCharacter:
        def __init__(self, name, age):
            self._name = name
            self._age = age

        def run(self):
            print('run')

        def speak(self):
            print(f'My name is {self._name}, and I am {self._age} years old')

    player1 = PlayerCharacter('Roger', 33)
    print(player1.speak())

    player2 = PlayerCharacter('Thaisa', 32)
    player2._age = 'This is a string now'
    player2.speak = 'I can do whatever I want'
    print(player2._name)
    print(player2._age)
    print(player2.speak)
    # Thaisa
    # This is a string now
    # I can do whatever I want
  ```

#### Inheritance

[Go Back to Summary](#summary)

```Python
  class User:
      def sign_in(self):
          print('logged in')

  class Wizard(User):
      def __init__(self, name, power):
          self.name = name
          self.power = power

      def attack(self):
          print(f'attacking with power of {self.power}')

  class Archer(User):
      def __init__(self, name, num_arrows):
          self.name = name
          self.num_arrows = num_arrows

      def attack(self):
          print(f'attacking with arrows: arrows left - {self.num_arrows}')

  wizard1 = Wizard('Roger', 100)
  wizard2 = Archer('Robin', 10)
  wizard1.sign_in()
  wizard2.sign_in()
  wizard1.attack()
  wizard2.attack()
```

#### isinstance()

[Go Back to Summary](#summary)

- It's a builtin function in Python that checks if it's an instance of a class.

  ```Python
    class User:
        def sign_in(self):
            print('logged in')

    class Wizard(User):
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def attack(self):
            print(f'attacking with power of {self.power}')

    class Archer(User):
        def __init__(self, name, num_arrows):
            self.name = name
            self.num_arrows = num_arrows

        def attack(self):
            print(f'attacking with arrows: arrows left - {self.num_arrows}')

    wizard1 = Wizard('Roger', 100)
    print(isinstance(wizard1, Wizard))
    # True
  ```

#### super()

[Go Back to Summary](#summary)

- The `super()` function in Python makes class inheritance more manageable and extensible. The function returns a temporary object that allows reference to a parent class by the keyword super.
- The `super()` function has two major use cases:

  - To avoid the usage of the super (parent) class explicitly.
  - To enable multiple inheritances​.

  ```Python
    class Computer():
        def __init__(self, computer, ram, storage):
            self.computer = computer
            self.ram = ram
            self.storage = storage

    class Mobile(Computer):
        def __init__(self, computer, ram, storage, model):
            super().__init__(computer, ram, storage)
            self.model = model

    Apple = Mobile('Apple', 2, 64, 'iPhone X')
    print('The mobile is:', Apple.computer)
    print('The RAM is:', Apple.ram)
    print('The storage is:', Apple.storage)
    print('The model is:', Apple.model)
  ```

### Functional Programming

[Go Back to Summary](#summary)

- What is function programming:
  - Clear + Understandable
  - Easy to Extend
  - Easy to Maintain
  - Memory Efficient
  - Dry

#### Pure Function

[Go Back to Summary](#summary)

- Pure functions rules:
  - Given the same input, the function always return us the same output
  - The function should not produce side effects
    - For example:
      - should not have a `print()` inside this function
      - should not modify an outside variable

#### map()

[Go Back to Summary](#summary)

- Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

  ```Python
    array = [1, 2, 3]

    def multiply_by2(array):
        return array*2

    print('new list =', list(map(multiply_by2, array)))
    print('original list =', array)
    # new list = [2, 4, 6]
    # original list = [1, 2, 3]
  ```

  - In this case we had to convert into a list, otherwise, python will only print the memory location
  - Notice that we don't need to execute the function `()`, we just have to point to the function and `map()` will take care for us
  - Just like in JavaScript, `map()` creates a new list (array in JS) and doesn't affect the original list (array)

#### filer()

[Go Back to Summary](#summary)

- The filter returns a new list (array) filtered by the condition. If the condition is equal to `True` then the filter will keep the item.
- Just like in JavaScript, `filter()` creates a new list (array in JS) and doesn't effect the original list (array)

  ```Python
    array = [1, 2, 3, 4, 5]

    def check_odd(array):
        return array % 2 != 0

    print('new list =', list(filter(check_odd, array)))
    print('original list =', array)
    # new list = [1, 3, 5]
    # original list = [1, 2, 3, 4, 5]
  ```

#### zip()

[Go Back to Summary](#summary)

- The `zip()` function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
- If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

  ```Python
    my_list = [1, 2, 3]
    your_list = ["a", "b", "c", "d"]
    their_list = ["I", "II", "III", "IV"]

    print(list(zip(my_list, your_list, their_list)))
    # [(1, 'a', 'I'), (2, 'b', 'II'), (3, 'c', 'III')]
  ```

#### reduce()

[Go Back to Summary](#summary)

- Reduce doesn't come with Python by default, we have to import form `functools`
- Python’s `reduce()` is a function that implements a mathematical technique called folding or reduction. `reduce()` is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.

  ```Python
    from functools import reduce
    my_list = [1, 2, 3]

    def sum_list(accumulator, array):
        return accumulator + array

    print(reduce(sum_list, my_list, 0))
    # 6
  ```

#### Lambada Expressions

[Go Back to Summary](#summary)

- How lambda expression works

  ```Python
    lambda param: action(param)
  ```

  ```Python
    my_list = [1, 2, 3]
    def multiply_by2(item):
        return item * 2

    print(list(map(multiply_by2,my_list)))
    # [2, 4, 6]
    print(list(map(lambda item: item*2, my_list)))
    # [2, 4, 6]
  ```

  ```Python
    from functools import reduce

    my_list = [1, 2, 3]

    print(reduce(lambda acc, item: acc+item, my_list))
    # 6
  ```

### List Comprehensions

[Go Back to Summary](#summary)

- how it works
- Variable = **[** new_variable/expression **for** use_this_variable **in** string **]**

  ```Python
    my_list = [char for char in 'hello'];
    print(my_list)

    my_list2 = [num for num in range(0, 100)]
    print(my_list2)

    my_list3 = [num*2 for num in range(0, 100)]
    print(my_list3)

    my_list4 = [num*2 for num in range(0, 100) if num % 2 == 0]
    print(my_list4)
  ```

#### Dictionary Comprehension

[Go Back to Summary](#summary)

```Python
  simple_dict = {
      'a': 1,
      'b': 2
  }

  my_dict = {key: value ** 2 for key, value in simple_dict.items()}
  print(my_dict)
  # {'a': 1, 'b': 4}

  my_dict2 = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
  print(my_dict
  # {'b': 4}

  my_dict3 = {num: num*2 for num in [1, 2, 3]}
  print(my_dict3)
  # {1: 2, 2: 4, 3: 6}

  some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
  my_dict = list(set([item for item in some_list if some_list.count(item) > 1]))
  print(my_dict)
  # ['n', 'b']
```

### Decorators

[Go Back to Summary](#summary)

- Decorators super charge our functions
- It gives extra functionalities to our functions
- **Higher Order Functions**

  - It could be a function that receives another function as argument
  - Or it could be a function that returns another function

  ```Python
    def greet(func):
        func()

    def gree2():
        def func2():
            return 5
        return func2
  ```

- A decorator wraps the original function and returns the wrapped function

  ```Python
    def my_decorator(func):
        def wrap_func():
            print('do something before')
            func()
            print('do something after')
        return wrap_func

    @my_decorator
    def hello():
        print('hellooooooo')

    @my_decorator
    def bye():
        print('see you later')

    hello()
    bye()

    # this is an alternative to decorator
    # it's the same thing
    # basically the `@` it's doing this for us
    hello2 = my_decorator(hello)()
  ```

#### How Decorators Are Build?

[Go Back to Summary](#summary)

- A decorator warps the original function and enhance the functionality of that function
- We could build a decorator with pre defined arguments/parameters
- Another option is to give `*args` and `*kwargs` as arguments, this way we dont need to pre define the parameters

  - We simple pass the `*args` and `*kwargs` as arguments to our **wrapper function**
  - And then pass the `*args` and `*kwargs` to the original function

  ```Python
    def my_decorator(func):
        def wrap_func(*args, **kwargs):
            print('do something before')
            func(*args, **kwargs)
            print('do something after')
        return wrap_func

    @my_decorator
    def hello(greeting, emoji='😀'):
        print(greeting, emoji)

    hello('hi1', emoji='😅')
    hello('hi2');

    hello3 = my_decorator(hello)
    hello3('hi3', '👍🏻')
  ```

#### @classmethod

- **@classmethod** is decorator that we add before defining the class method
- with **@classmethod** we could instantiate a new object without the need to instantiate the class
- The naming convention of the first parameter is to use `cls` instead of `self`
- the first parameter is always `cls`, `cls` stands for **class**

  ```Python
    class PlayerCharacter:
        membership = True

        #! constructor
        def __init__(self, name, age):
            if (age > 18):
                self.name = name  # attribute the constructor
                self.age = age

        #! method
        def shout(self):
            print(f'My name is {self.name}')

        #! decorator
        #+ class method
        @classmethod
        def adding_new_member(cls, num1, num2):
            return cls('Tom', num1+num2)

    player3 = PlayerCharacter.adding_new_member(10, 11)
    print(player3.name)
    print(player3.age)
    # Tom
    # 21
  ```

#### @staticmethod

- **@staticmethod** works the same way as **@classmethod** the only difference is that we don't need to define the `cls` as first parameter because **@staticmethod** doesn't have access to the class properties.
- We just want to perform a certain method

  ```Python
    class PlayerCharacter:
        membership = True

        #! constructor
        def __init__(self, name, age):
            if (age > 18):
                self.name = name  # attribute the constructor
                self.age = age

        #! method
        def shout(self):
            print(f'My name is {self.name}')

        #! decorator
        #+ class method
        @classmethod
        def adding_new_member(cls, num1, num2):
            return cls('Tom', num1 + num2)

        #+ static method
        @staticmethod
        def sum_number(num1, num2):
            return num1 + num2

    print(PlayerCharacter.sum_number(1, 1))
    # 2
  ```

#### Custom Decorator

[Go Back to Summary](#summary)

- Let's build our own decorator, we are going to build our own **performance** decorator, to see how fast our function runs
- To do that we have to import the `time` module from python

  ```Python
    from time import time

    def performance(func):
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f'It took {t2-t1} ms')
            return result
        return wrap_func

    @performance
    def long_time():
        for i in range(10000000):
            i * 5

    long_time()
  ```

  ```Python
    user1 = {
        'name': 'Sorna',
        'valid': True
    }

    def authenticated(fn):
        def wrap_func(*args, **kwargs):
            if (args[0]['valid'] == True):
                return fn(*args, **kwargs)
        return wrap_func

    @authenticated
    def message_friends(user):
        name = user['name']
        print(f'message has been sent to {name}')

    message_friends(user1)
    # message has been sent to Sorna
  ```

### Error Handling

[Go Back to Summary](#summary)

- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

#### Try/Except

[Go Back to Summary](#summary)

```Python
  while True:
  try:
      age = int(input('What is your age? '))
      10/age
  except ValueError:
      print('Please enter a valid number')
  except ZeroDivisionError:
      print('Please enter a number greater than 0 (zero)')
  else:
      print('Thank you')
      break
```

#### Specific Error

[Go Back to Summary](#summary)

- We can get a specific error to do something
- Get the complete error, we can assign the type of the error to a variable

  - This variable is an object

  ```Python
    def sum(num1, num2):
        try:
            print(num1 + num2);
        except TypeError as error:
            print(f'Please enter a valid number, {error}')
    sum('1', 2)
    # Please enter a valid number, can only concatenate str (not "int") to str
  ```

#### Multiple Errors

[Go Back to Summary](#summary)

- We can handle more than one type of error

  ```Python
    def div(num1, num2):
        try:
            print(num1/num2);
        except (TypeError, ZeroDivisionError) as error:
            print(f'Something went wrong, {error}')
    div('1', 2)
    div(1, 0)
    # Something went wrong, unsupported operand type(s) for /: 'str' and 'int'
    # Something went wrong, division by zero
  ```

#### Complete Try/Except Structure

[Go Back to Summary](#summary)

- With Try/Except we have a final stage where it's executed when everything is done (`finally`) with errors or without errors

  ```Python
    try:
      # code that possible throws an error
    except:
      # catch the error
    else:
      # if no errors occur
    finally:
      # it's executed even if we get an error or not
  ```

#### Raise an Error

[Go Back to Summary](#summary)

- If we want to break out of code and print your own custom error

  ```Python
    def raiseAnError():
        print('Hello There')
        raise ValueError('This is not a number')

    raiseAnError()
    # ValueError: This is not a number
  ```

### Generators

[Go Back to Summary](#summary)

- A generator in Python is similar to JavaScript where we can **pause** and **yield** during the execution of the code
- We can run the code as many times we want until we hit the end of the range
- With generators, we use less memory, because instead of creating the whole array of numbers, we just create a single item at time and do something with it

  ```Python
    def generator_function(number):
        for i in range(number):
            yield i*2

    g = generator_function(100)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    # 0
    # 2
    # 4
    # 6
    # 8
  ```

  ```Python
    from time import time

    def performance(func):
        def wrapper(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f'It took {t2-t1} s')
            return result
        return wrapper

    # range() it's a generator that comes with Python
    @performance
    def long_time():
        print('1')
        for i in range(100000000):
            i * 5

    # list() converter the range into a list with 100000000 in it
    @performance
    def long_time2():
        print('2')
        for i in list(range(100000000)):
            i * 5

    long_time()
    long_time2()
    # 1
    # It took 5.031090974807739 ms
    # 2
    # It took 7.939239978790283 ms
  ```

- Let's create our own **for loop**

  ```Python
    def special_for(iterable):
        iterator = iter(iterable)

        while (True):
            try:
                print(iterator)
                print(next(iterator))
            except StopIteration:
                break

    special_for([1, 2, 3])

    # <list_iterator object at 0x1064df5d0>
    # 1
    # <list_iterator object at 0x1064df5d0>
    # 2
    # <list_iterator object at 0x1064df5d0>
    # 3
  ```

- Let's create our own **range()**

  ```Python
    class MyGeneratorRange():
        current = 0
        def __init__(self, first, last):
            self.first = first
            self.last = last

        def __iter__(self):
            return self

        def __next__(self):
            if MyGeneratorRange.current < self.last:
                num = MyGeneratorRange.current
                MyGeneratorRange.current += 1
                return num
            raise StopIteration

    my_range = MyGeneratorRange(0, 100)
    for i in my_range:
        print(i)
  ```

- Fibonacci Sequence

  ```Python
    def fibonacci(number):
        a = 0
        b = 1
        for i in range(number+1):
            yield a
            temp = a
            a = b
            b = temp + b

    for i in fibonacci(1000):
        print(i)

    def fibonacci2(number):
        a = 0
        b = 1
        result = []
        for i in range(number+1):
            result.append(a)
            temp = a
            a = b
            b = temp + b
        return result

    print(fibonacci2(1000))
  ```

# PYTHON MODULES

[Go Back to Summary](#summary)

- To create a Python module, we just have to create a new Python file (`.py`) and then import into the file we want to use

- in `utility.py`

  ```Python
    def multiply (num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2
  ```

- in `main.py`

  ```Python
    import utility

    print(utility.multiply(3, 3))
    # 9
  ```

## Python Package

[Go Back to Summary](#summary)

- Python packages are just folders with a special file (`__init__.py`)
- the `__init__.py` means that this is a python package
- to import a python package, we just need to `<folder_name>.<file_name>`

- in `shopping/shopping_cart.py`

  ```Python
    def buy(item):
    cart = []
    cart.append(item)
    return cart
  ```

- in `main.py`

  ```Python
    import utility
    import shopping.shopping_cart

    print(utility.multiply(3, 3))
    print(shopping.shopping_cart.buy('apple'))
    # 9
    # ['apple']
  ```

#### Different Ways To Import

[Go Back to Summary](#summary)

- The easiest way to import new packages is to chain the folder structure
  - `import shopping.shopping_cart.more_shopping.cart`
- Another way is to use `from` ... `import` ...

  - we can partial import a package to avoid name collision

  ```Python
    from utility import multiply, divide
    from shopping.shopping_cart.more_shopping.cart import shopping_cart

    print(multiply(3, 3))
    print(shopping_cart.buy('apple'))
  ```

### \_\_name\_\_

[Go Back to Summary](#summary)

- We often see something like:
  - `if __name__ == '__main__'`
  - This line checks if the file that we are running is the main file, in other words, if the file is the

# DEBUGGING

[Go Back to Summary](#summary)

- [The Python Debugger - Official Docs](https://docs.python.org/3/library/pdb.html)
- We can enhance our debugging problem by importing `pdb` from our Python libraries.

  - `pdb` is an interactive debugger that we can pause the code any time
    - `pdb.set_trace()`
  - during debugging we can also change the variables if we want to
    - `num1 = 5`
  - few useful commands:
    - `step` on the terminal, we go line by line
    - `a` returns all the available arguments
    - `w` returns the content of the current line
    - `continue` continue the code until we return something
    - `exit`

  ```Python
    import pdb

    def add(num1, num2):
        pdb.set_trace()
        return num1 + num2

    add(4, 'error')
  ```

# WORKING WITH FILES

## Option 1

[Go Back to Summary](#summary)

- We can import external files using `open()`

  ```Python
    my_file = open('my_txt.txt')
    print(my_file)
    # <_io.TextIOWrapper name='my_txt.txt' mode='r' encoding='UTF-8'>
  ```

  - This will output the file wrapper with:

    - name = `my_txt.txt`
    - mode = `r` (read)
    - encoding = `UTF-8` (encoding type)

- **IMPORTANT** after we finish using the file, we have to manually close the file using `.close()`

### Read All Lines - .read()

[Go Back to Summary](#summary)

- with `.read()`, Python reads the current line by using the cursor position
- When we open the file the cursor is in the beginning of the first line
- Once Python reads the line (`.read()`) the cursor will be in the end of the file, so if we try to run the command again, it will print nothing
- To move the cursor to the beginning of the file, we use `.seek(0)`

  ```Python
    my_file = open('my_txt.txt')
    print(my_file.read())
    print(my_file.read())
    my_file.seek(0)
    print(my_file.read())
    my_file.seek(0)
    print(my_file.read())
    my_file.close()
  ```

### Read Single Line - .readline()

[Go Back to Summary](#summary)

- with `.readline()`, Python will read line by line

  ```Python
    my_file = open('my_txt.txt')

    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())
    my_file.close()

    # Hello world

    # Second line

    # Third line

    # Forth line
  ```

### Read All Lines as a List - .readlines()

[Go Back to Summary](#summary)

- With `.readlines()` Python will return all the lines in a form of a list

  ```Python
    my_file = open('my_txt.txt')

    print(my_file.readlines())
    my_file.close()

    # ['Hello world\n', 'Second line\n', 'Third line\n', 'Fourth line']
  ```

## Option 2

[Go Back to Summary](#summary)

- A better option to work with files is to use `with`
- **Advantage:** we don't need to manually close the file

  ```Python
    with open('my_txt.txt') as my_file:
        print(my_file.readlines())
  ```

- `open()` method, has a second parameter (**mode**)
- By default `mode='r'` (read only)

### Read and Write Files - mode='r+'

[Go Back to Summary](#summary)

- `more='r+'` stands for read and write
- When we write something to a file, the new text will be written on the current location of the cursor
- **ATTENTION:** Be careful to now overwrite things

  ```Python
    with open('my_txt.txt', mode='r+') as my_file:
        text = my_file.write("Hi it's me")
        print(text)
    # 10 <- it's the number of characters that we wrote
  ```

  ```Text
    Hi it's med <----- Line overwritten
    Second line
    Third line
    Fourth line
  ```

### Append Files - mode='a'

[Go Back to Summary](#summary)

- `mode='a'` will append the new information to the end of the file
- if the file doesn't exist, Python will create one

  ```Python
    with open('my_txt.txt', mode='a') as my_file:
        text = my_file.write("Hi it's me")
        print(text)
  ```

  ```Text
    Hi it's med
    Second line
    Third line
    Fourth lineHi it's me
  ```

### Write Files - mode='w'

[Go Back to Summary](#summary)

- `mode='w'` will overwrite the whole file with the new information
- if the file doesn't exist, Python will create one

  ```Python
    with open('my_txt.txt', mode='w') as my_file:
        text = my_file.write("Hi it's me")
        print(text)
    # 10
  ```

  ```Text
    Hi it's me
  ```

## Paths

[Go Back to Summary](#summary)

- Linux/Mac:

  - We can add the relative path using `/`

  ```Python
    with open('.relative_path/../../my_txt.txt', mode='w') as my_file:
        text = my_file.write("Hi it's me")
        print(text)
  ```

- Windows

  - With windows we have to use `\`

  ```Python
    with open('.relative_path\..\..\my_txt.txt', mode='w') as my_file:
        text = my_file.write("Hi it's me")
        print(text)
  ```

- A good option is to use a library to access certain files/folder in our OS like [pathlib](https://docs.python.org/3/library/pathlib.html)

## Handling File Errors

[Go Back to Summary](#summary)

- A good way to handle errors if the file does not exist is to use a `try/except` block
- It's also good catch `IOError`, `IOError` means that something went wrong reading/writing the file

  ```Python
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
  ```

# REGEX

[Go Back to Summary](#summary)

- To use Regular Expressions we have to import a module called `re`

- Support for regular expressions (RE).
- This module provides regular expression matching operations similar to those found in Perl. It supports both 8-bit and Unicode strings; both the pattern and the strings being processed can contain null bytes and characters outside the US ASCII range.

- Regular expressions can contain both special and ordinary characters. Most ordinary characters, like "A", "a", or "0", are the simplest regular expressions; they simply match themselves. You can concatenate ordinary characters, so last matches the string 'last'.

- The special characters are:

  - `.` Matches any character except a newline.
  - `^` Matches the start of the string.
  - `\$` Matches the end of the string or just before the newline at the end of the string.
  - `\*` Matches 0 or more (greedy) repetitions of the preceding RE. Greedy means that it will match as many repetitions as possible.
  - `+` Matches 1 or more (greedy) repetitions of the preceding RE.
  - `?` Matches 0 or 1 (greedy) of the preceding RE.
  - `\*?`,`+?`,`??` Non-greedy versions of the previous three special characters.
  - `{m,n}` Matches from m to n repetitions of the preceding RE.
  - `{m,n}?` Non-greedy version of the above.
  - `\\` Either escapes special characters or signals a special sequence.
  - `[]` Indicates a set of characters. A "^" as the first character indicates a complementing set.
  - `|` A|B, creates an RE that will match either A or B.
  - `(...)` Matches the RE inside the parentheses. The contents can be retrieved or matched later in the string.
  - `(?aiLmsux)` Set the A, I, L, M, S, U, or X flag for the RE (see below).
  - `(?:...)` Non-grouping version of regular parentheses.
  - `(?P<name>...)` The substring matched by the group is accessible by name.
  - `(?P=name)` Matches the text matched earlier by the group named name.
  - `(?#...)` A comment; ignored.
  - `(?=...)` Matches if ... matches next, but doesn't consume the string.
  - `(?!...)` Matches if ... doesn't match next.
  - `(?<=...)` Matches if preceded by ... (must be fixed length).
  - `(?<!...)` Matches if not preceded by ... (must be fixed length).
  - `(?(id/name)yes|no)` Matches yes pattern if the group with id/name matched, the (optional) no pattern otherwise.

- The special sequences consist of `\\` and a character from the list below. If the ordinary character is not on the list, then the resulting RE will match the second character.

  - `\number`Matches the contents of the group of the same number.
  - `\A` Matches only at the start of the string.
  - `\Z` Matches only at the end of the string.
  - `\b` Matches the empty string, but only at the start or end of a word.
  - `\B` Matches the empty string, but not at the start or end of a word.
  - `\d` Matches any decimal digit; equivalent to the set [0-9] in bytes patterns or string patterns with the ASCII flag. In string patterns without the ASCII flag, it will match the whole range of Unicode digits.
  - `\D` Matches any non-digit character; equivalent to [^\d].
  - `\s` Matches any whitespace character; equivalent to [ \t\n\r\f\v] in bytes patterns or string patterns with the ASCII flag. In string patterns without the ASCII flag, it will match the whole range of Unicode whitespace characters.
  - `\S` Matches any non-whitespace character; equivalent to [^\s].
  - `\w` Matches any alphanumeric character; equivalent to [a-zA-Z0-9_] in bytes patterns or string patterns with the ASCII flag. In string patterns without the ASCII flag, it will match the range of Unicode alphanumeric characters (letters plus digits plus underscore). With LOCALE, it will match the set [0-9_] plus characters defined as letters for the current locale.
  - `\W` Matches the complement of \w.
  - `\\` Matches a literal backslash.

- This module exports the following functions:

  - `match` Match a regular expression pattern to the beginning of a string.
  - `fullmatch` Match a regular expression pattern to all of a string.
  - `search` Search a string for the presence of a pattern.
  - `sub` Substitute occurrences of a pattern found in a string.
  - `subn` Same as sub, but also return the number of substitutions made.
  - `split` Split a string by the occurrences of a pattern.
  - `findall` Find all occurrences of a pattern in a string.
  - `finditer` Return an iterator yielding a Match object for each match.
  - `compile` Compile a pattern into a Pattern object.
  - `purge` Clear the regular expression cache.
  - `escape` Backslash all non-alphanumerics in a string.

- Some of the functions in this module takes flags as optional parameters:

  - A ASCII For string patterns, make `\w`, `\W`, `\b`, `\B`, `\d`, `\D` match the corresponding ASCII character categories (rather than the whole Unicode categories, which is the default).
  - For bytes patterns, this flag is the only available behaviour and needn't be specified.
  - `I` IGNORECASE Perform case-insensitive matching.
  - `L` LOCALE Make \w, \W, \b, \B, dependent on the current locale.
  - `M` MULTILINE "^" matches the beginning of lines (after a newline) as well as the string.
  - `\$` matches the end of lines (before a newline) as well as the end of the string.
  - `S` DOTALL "." matches any character at all, including the newline.
  - `X` VERBOSE Ignore whitespace and comments for nicer looking RE's.
  - `U` UNICODE For compatibility only. Ignored for string patterns (it is the default), and forbidden for bytes patterns.

  ```Python
    import re

    string = 'search inside of this text please!'

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
    # <re.Match object; span=(7, 11), match='this'>
    # Where the string occurs, between (7, 11)
    # Where the string starts, on index 7
    # Where the string ends, on index 11
    # Returns the part that was the match this
  ```

  ```Python
    import re

    string = 'search this inside of this text please!'

    try:
        pattern = re.compile('search this inside of this')
        print(pattern.search(string))
        print('Returns a list of matches, ', pattern.findall(string))
        print('Only full match will be returned,', pattern.fullmatch(string))
        print('Returns partial match', pattern.match(string))
    except AttributeError as error:
        print('Match not found')
        raise error
    # <re.Match object; span=(0, 26), match='search this inside of this'>
    # Returns a list of matches,  ['search this inside of this']
    # Only full match will be returned, None
    # Returns partial match <re.Match object; span=(0, 26), match='search this inside of this'>
  ```

  ```Python
    email = 'hi my name is roger, my email is roger@roger.com'
    try:
        pattern = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z0-9]$)')
        print(pattern.search(email))
        print('Returns a list of matches, ', pattern.findall(email))
    except AttributeError as error:
        print('Match not found')
        raise error
    # <re.Match object; span=(33, 48), match='roger@roger.com'>
    # Returns a list of matches,  ['roger@roger.com']
  ```

  ```Python
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
    # Your password is RraasZ$#@8
  ```

# TESTING

[Go Back to Summary](#summary)

- Python comes with a built-in test module called `unittest`
- [unittest - Official Docs](https://docs.python.org/3/library/unittest.html)

## Unittest

[Go Back to Summary](#summary)

| Method                                                                                                             | Checks that          | New in |
| ------------------------------------------------------------------------------------------------------------------ | -------------------- | ------ |
| [assertEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)                 | a == b               |        |
| [assertNotEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)           | a != b               |        |
| [assertTrue(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)                      | bool(x) is True      |        |
| [assertFalse(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse)                    | bool(x) is False     |        |
| [assertIs(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)                       | a is b               | 3.1    |
| [assertIsNot(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)                 | a is not b           | 3.1    |
| [assertIsNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)                  | x is None            | 3.1    |
| [assertIsNotNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)            | x is not None        | 3.1    |
| [assertIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)                       | a in b               | 3.1    |
| [assertNotIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)                 | a not in b           | 3.1    |
| [assertIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)       | isinstance(a, b)     | 3.2    |
| [assertNotIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance) | not isinstance(a, b) | 3.2    |

- To use the `unittest`, we need to:

  - Import the file that we want to test
  - Create a new class
    - Then we inherit the `TestCase` from `unittest`
      - `unittest.TestCase`
    - Create a new function that describes what kind of test we are doing
    - Do all the logic
    - Then we can call `self.assertEqual` that we inherited from `unittest`
      - `.assertEqual()` checks if both parameters are equal
  - Run the `unittest`
    - `unittest.main()` that will run the entire test file

- in `main.py`

  ```Python
    def do_stuff(num):
    try:
        return int(num) +5
    except ValueError as error:
        return error
  ```

- in `test.py`

  ```Python
    import unittest
    import main

    class TestMAin(unittest.TestCase):
        def test_do_stuff(self):
            test_param = 10
            result = main.do_stuff(test_param)
            self.assertEqual(result, 15)

        def test_do_stuff2(self):
            test_param = 'string'
            result = main.do_stuff(test_param)
            self.assertIsInstance(result, ValueError)

    unittest.main()
    # ----------------------------------------------------------------------
    # Ran 2 test in 0.000s
  ```

## Run Multiple Test Files

[Go Back to Summary](#summary)

- To run multiple test files, change directory to the test folder, and run the following command

  ```Bash
    python3 -m unittest
  ```

- we can add an extra parameter `-v` (verbose)

  - This command adds more information about each test, there we can see which test passed and which one not passed

  ```Bash
    test_do_stuff_equal_to_15 (test.TestUtility) ... ok
    test_do_stuff_invalid_number (test.TestUtility) ... ok
    test_do_stuff_is_instance_of_value_error (test.TestUtility) ... ok
    test_do_stuff_number_equals_empty (test.TestUtility) ... ok
    test_do_stuff_equal_to_15 (test2.TestUtility) ... ok
    test_do_stuff_invalid_number (test2.TestUtility) ... ok
    test_do_stuff_is_instance_of_value_error (test2.TestUtility) ... ok
    test_do_stuff_number_equals_empty (test2.TestUtility) ... ok

    ----------------------------------------------------------------------
    Ran 8 tests in 0.001s
  ```

## setUp(self)

[Go Back to Summary](#summary)

- the `setUp(self)` function, runs every time before each test

  ```Python
    import unittest
    import utility

    class TestUtility(unittest.TestCase):
        def setUp(self):
            print()
            print('dropping database...')
            print('creating database...')
            print('creating new users...')

        def test_do_stuff_equal_to_15(self):
            test_param = 10
            result = utility.do_stuff(test_param)
            self.assertEqual(result, 15)

        def test_do_stuff_is_instance_of_value_error(self):
            test_param = 'string'
            result = utility.do_stuff(test_param)
            self.assertIsInstance(result, ValueError)

        def test_do_stuff_invalid_number(self):
            test_param = None
            result = utility.do_stuff(test_param)
            self.assertEqual(result, 'please enter number')

        def test_do_stuff_number_equals_empty(self):
            test_param = ''
            result = utility.do_stuff(test_param)
            self.assertEqual(result, 'please enter number')

    if __name__ == '__main__':
        unittest.main()
    # test_do_stuff_number_equals_empty (test.TestUtility) ...
    # deleting database...
    # creating new users...
    # ok
  ```

## tearDown(self)

[Go Back to Summary](#summary)

- the `tearDown(self)` function, runs every time after each test

  ```Python
    import unittest
    import utility

    class TestUtility(unittest.TestCase):
        def setUp(self):
            print()
            print('deleting database...')
            print('creating new users...')

        def test_do_stuff_equal_to_15(self):
            test_param = 10
            result = utility.do_stuff(test_param)
            self.assertEqual(result, 15)

        def test_do_stuff_is_instance_of_value_error(self):
            test_param = 'string'
            result = utility.do_stuff(test_param)
            self.assertIsInstance(result, ValueError)

        def test_do_stuff_invalid_number(self):
            test_param = None
            result = utility.do_stuff(test_param)
            self.assertEqual(result, 'please enter number')

        def test_do_stuff_number_equals_empty(self):
            test_param = ''
            result = utility.do_stuff(test_param)
            self.assertEqual(result, 'please enter number')

        def tearDown(self):
            print('cleaning up variables')
            print('closing connection with database')

    if __name__ == '__main__':
        unittest.main()
    # test_do_stuff_number_equals_empty (test.TestUtility) ...
    # deleting database...
    # creating new users...
    # closing connection with database
    # ok
  ```

# PIL - IMAGE PROCESSING

[Go Back to Summary](#summary)

- [Pillow (PIL) - Official Docs](https://pillow.readthedocs.io/en/stable/about.html#goals)

## Install PIL

[Go Back to Summary](#summary)

- install PIL

  ```Bash
    pip3 install Pillow
  ```

## PIL Basics

[Go Back to Summary](#summary)

- Working with images

  ```Python
    from PIL import Image, ImageFilter

    img = Image.open('./yumi.png')

    print(img)
    print(img.mode)
    print(img.size)
    print(img.format)

    #! Blur
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save('./images/converted/yumi_blur.png', 'png')

    #! Smooth
    filtered_img2 = img.filter(ImageFilter.SMOOTH)
    filtered_img2.save('./images/converted/yumi_smooth.png', 'png')

    #! Sharpen
    filtered_img3 = img.filter(ImageFilter.SHARPEN)
    filtered_img3.save('./images/converted/yumi_sharpen.png', 'png')

    #! Grey Scale
    filtered_img4 = img.convert('L') # 'L' = grey scale
    filtered_img4.save('./images/converted/yumi_grey_scale.png', 'png')

    #! Show Image
    # filtered_img4.show()

    #! Rotate
    rotated_img = filtered_img4.rotate(75)
    rotated_img.save('./images/converted/yumi_rotated.png', 'png')

    #! Resize
    resized_img = img.resize((300, 300))
    resized_img.save('./images/converted/yumi_300x300.png', 'png')

    #! Crop
    box = (100, 100, 400, 400)
    cropped_img = img.crop(box)
    cropped_img.save('./images/converted/yumi_cropped.png', 'png')

    #! Thumbnail
    img.thumbnail((150 ,150))
    img.save('./images/converted/yumi_thumbnail.png')
  ```

## Image Converter (jpg to png)

[Go Back to Summary](#summary)

- To use the image converter, we first need to import the `sys` module to get the input from the user
- We need to import `os` or `pathlib` (alternative)
  - [os - Official Docs](https://docs.python.org/3/library/os.html)
  - [pathlib - Official Docs](https://docs.python.org/3/library/pathlib.html)
- To use run the code we need to give the images_folder and the destination folder, like so:
- `python3 image_converter.py images/images_jpg/ images/images_png/`

  ```Python
    import sys
    import os
    from PIL import Image

    images_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    print(images_folder, destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(images_folder):
        img = Image.open(f'{images_folder}{filename}')
        clean_name = os.path.splitext(filename)
        img.save(f'{destination_folder}{clean_name[0]}.png', 'png')
  ```

# PyPDF2 - PDF

[Go Back to Summary](#summary)

- To work with PDFs we are going to use `PyPDF2`
- [PyPDF2 - Official Docs](https://pythonhosted.org/PyPDF2/)

## Install PyPDF2

[Go Back to Summary](#summary)

- Install `PyDF2`

  ```Bash
    pip3 install PyPDF2
  ```

## PDF Basics

[Go Back to Summary](#summary)

- `PdfFileReader(my_file)` - Read the PDF in binary format
  - `rb` - Ready Binary
- `.numPages`
- `.getPage(0)` - Get the first page
- `.rotateClockwise()` - Rotate a page, first we need to get page, then we can rotate
- `.rotateCounterClockwise()` - Rotate a page, first we need to get page, then we can rotate
- `.PdfFileWriter()` - Writer
- `.addPage()` - Adds a new page
- `.write()` - Save the modified file
- `.PdfFileMerger()` - Combine multiple pdfs

  ```Python
    import PyPDF2
    import os
    output_folder = './pdf/converted/'

    with open('./pdf/dummy.pdf', 'rb') as my_file:
        #! Read the binary file
        reader = PyPDF2.PdfFileReader(my_file)

        #! Select the name
        filename = os.path.splitext(os.path.basename(my_file.name))

        #! Rotate a page
        selected_page = reader.getPage(0)
        selected_page.rotateClockwise(180)

        #! Print the number of pages
        print(reader.numPages)

        #! Save (write) a new file
        #+ first we instantiate the .PdfFileWriter()
        #+ create the file in mode 'wb' (write binary)
        writer = PyPDF2.PdfFileWriter()
        #+ write to the pdf
        writer.addPage(selected_page)

        #+ check if folder exists, if not create one
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        #+ save the file
        with open(f'{output_folder}{filename[0]}_converted.pdf', 'wb') as converted_file:
            writer.write(converted_file)
  ```

## Merge/Combine PDFs

[Go Back to Summary](#summary)

- Similar to write a PDF (`.PdfFileWriter()`) we have the merger (`PdfFileMerger()`)

  ```Bash
    python3 pdf_combiner.py pdf/dummy.pdf pdf/twopage.pdf pdf/wtr.pdf
  ```

  ```Python
    import os
    import sys
    import PyPDF2

    files = sys.argv[1:]

    def pdf_combiner(files):
        output_path = './pdf/merged_pdfs/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        merger = PyPDF2.PdfFileMerger()

        for file in files:
            merger.append(file)

        merger.write(f'{output_path}combined_pdf.pdf')

    pdf_combiner(files)
  ```

## Watermaker PDF

[Go Back to Summary](#summary)

- Watermaker PDF, where the first argument is the watermark then the rest are the files

  ```Bash
    python3 pdf_watermaker.py pdf/wtr.pdf pdf/dummy.pdf pdf/twopage.pdf
  ```

  ```Python
    import os
    import sys
    import PyPDF2

    watermark = sys.argv[1]
    files = sys.argv[2:]
    output_dir = './pdf/watermarked_pdf/'

    def pdf_watermarker(watermark, files):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(watermark, 'rb') as watermark_file:
            converted_watermark_file = PyPDF2.PdfFileReader(watermark_file)
            watermark_page = converted_watermark_file.getPage(0)

            for file in files:
                with open(file, 'rb') as single_file:
                    count = 1
                    writer = PyPDF2.PdfFileWriter()
                    read_single_file = PyPDF2.PdfFileReader(single_file)
                    for page in range(read_single_file.numPages):
                        new_page = read_single_file.getPage(page)
                        new_page.mergePage(watermark_page)
                        writer.addPage(new_page)

                    while (True):
                        output_filename = f'{output_dir}merged_file_{count}.pdf'
                        if not os.path.exists(output_filename):
                            with open(output_filename, 'wb') as new_file:
                                writer.write(new_file)
                            break
                        else:
                            count += 1

    pdf_watermarker(watermark, files)
  ```

- Little refactoring:

  ```Python
    import os
    import sys
    import PyPDF2

    watermark = sys.argv[1]
    files = sys.argv[2:]
    output_dir = './pdf/watermarked_pdf/'

    def pdf_watermarker(watermark, files):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        converted_watermark_file = PyPDF2.PdfFileReader(open(watermark, 'rb'))
        watermark_page = converted_watermark_file.getPage(0)

        for file in files:
            count = 1
            writer = PyPDF2.PdfFileWriter()
            read_single_file = PyPDF2.PdfFileReader(open(file, 'rb'))
            for page in range(read_single_file.numPages):
                new_page = read_single_file.getPage(page)
                new_page.mergePage(watermark_page)
                writer.addPage(new_page)

            while (True):
                output_filename = f'{output_dir}merged_file_{count}.pdf'
                if not os.path.exists(output_filename):
                    writer.write(open(output_filename, 'wb'))
                    break
                else:
                    count += 1

    pdf_watermarker(watermark, files)
  ```

# smtplib - EMAIL

[Go Back to Summary](#summary)

- Python has a built-in email module called `smtplib`
- [smtplib - Official Docs](https://docs.python.org/3/library/email.examples.html)

## SMTP Protocol

[Go Back to Summary](#summary)

- **SMTP**, or **Simple Mail Transfer Protocol**, is a set of communication guidelines used by email servers to deliver emails to their clients. Your emails are just strings of text; **SMTP** helps servers and email clients categorize and organize the information you send. When you send an email, the sender, recipients, email body and title heading are separated into sections. **SMTP** separates the sections using code words.

- **SMTP Usage**
  **SMTP** is used to send emails, so it only works for outgoing emails. To be able to send emails, you need to provide the correct SMTP server when you set up your email client. Unlike POP3 and IMAP, SMTP can't be used to retrieve and store emails. **SMTP** is also responsible for setting up communication between servers. The first server identifies itself and transmits the type of operation it will perform. The email is sent only after the second server authorizes the operation. SMTP is simple and reliable, but not very secure. Because it is text-based, **SMTP** is vulnerable to spoofing.

## Using smtplib

[Go Back to Summary](#summary)

- Import the the library and `EmailMessage`

  ```Python
    import stmtplib
    from email.message import EmailMessage
  ```

- Then create a new email object using `EmailMessage()`

  - Add, who is this email from?
    - `email['from'] = 'Your Name'`
  - Add, who are we sending the email to
    - `email['to'] = 'user_email@gmail.com'`
  - Add the email's subject line
    - `email['subject'] = 'It\'s your lucky day Yumi'`
  - Add the content
    - `email.set_content('Hi Yumi, you just won $1.000 and 2x bones')`

- After setting up the the email object content, we need to send the email

  ```Python
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        # ehlo, this is a part of the protocol of the smtp
        smtp.ehlo()
        # starts the encryption protocol
        smtp.starttls()
        # login to gmail acc with your credentials
        stmp.login('your_email@gmail.com', 'your_password')
        # send the email that we just created
        smtp.send_message(email)
        print('message sent')
  ```

  ```Python
    import smtplib
    from email.message import EmailMessage

    email = EmailMessage()
    email['From'] = 'Your Name'
    email['To'] = 'user_email@gmail.com'
    email['Subject'] = 'It\'s your lucky day Yumi'
    email.set_content('Hi Yumi, you just won $1.000 and 2x bones')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        # ehlo, this is a part of the protocol of the smtp
        smtp.ehlo()
        # starts the encryption protocol
        smtp.starttls()
        # login to gmail acc with your credentials
        smtp.login('your_email@gmail.com', 'your_password')
        # send the email that we just created
        smtp.send_message(email)
        print('message sent')
  ```

- **ATTENTION** the name of the file has to be anything different from `email.py`

### String Template

[Go Back to Summary](#summary)

- `String Template` is a a built-in class (`class string.Template(template)`), just like template literals
  - [string.Template - Official Docs](https://docs.python.org/3/library/string.html)
- In this case we are going to read the `html` file, then we are going to substitute the variable `$name`
  - to access the `html` file, we are going to use `pathlib`, we could also use `os`
  - [pathlib vs os](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
- Then instead of sending a fixed text, we can substitute the `$name` with a dynamic name
  - `html.substitute(name='Yumi')` or `html.substitute({'name': name})`
  - the `email.set_content()` has a second parameter, that we can specify the format
    - we can set the email content to be `html`, so the email will be formatted as `html`

* in `email_send.html`

  - Let's create a base `html` file

  ```HTML
    <!DOCTYPE html>
    <html lang="en">

    <head>
    </head>

    <body>
        $name just won 1.000,00 CAD and 2x bones
    </body>

    </html>
  ```

* in `email_send.py`

  ```Python
    import smtplib
    from email.message import EmailMessage
    from string import Template
    from pathlib import Path

    name = 'Yumi'
    html = Template(Path('email_send.html').read_text())
    email = EmailMessage()
    email['From'] = 'Your Name'
    email['To'] = 'user_email@gmail.com'
    email['Subject'] = f'It\'s your lucky day {name}'
    email.set_content(html.substitute({'name': name}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('your_email@gmail.com', 'your_password')
        smtp.send_message(email)
        print('message sent')
  ```

# hashlib - HASH PASSWORD

[Go Back to Summary](#summary)

- Python has a built-in library called `hashlib` that helps us to hash our password
- [hashlib - Official Docs](https://docs.python.org/3/library/hashlib.html)

## Password Checker

[Go Back to Summary](#summary)

- Checks if our password has been leaked
- [Hash Generator](https://passwordsgenerator.net/md5-hash-generator/)
- `hashlib.sha1(password.encode('utf-8')).hexdigest().upper()`

  - basically we get our `password` and then encode as `utf-8` (we must provide an encode), then we convert into hexadecimal digits, and then covert everything to uppercase

- now we can get the first 5 character and the rest of the password (tail)
  - `first5_char, tail = sha1password[:5], sha1password[5:]`
- Then we send a quest to the api to return the of leaked passwords,
- After that we check if there is any hash equal to our hashed password

  ```Python
    import requests
    import hashlib
    import sys

    def request_api_data(query_data):
        url = 'https://api.pwnedpasswords.com/range/' + query_data
        res = requests.get(url)

        if res.status_code != 200:
            raise RuntimeError(f'Error fetching {res.status_code}. check the api again')

        return res

    def get_password_leaks_count(hashes, my_hashed_pass):
        hashes = (line.split(':') for line in hashes.text.splitlines())

        for hash, count in hashes:
            if hash == my_hashed_pass:
                return count
        return 0

    def pwned_api_check(password):
        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        response = request_api_data(first5_char)
        return get_password_leaks_count(response, tail)

    def main(passwords):
        for password in passwords:
            count = pwned_api_check(password)
            if count:
                print(f'{password} was fount {count} times... you should change your password')
            else:
                print(f'{password} was NOT found')
        return 'done!'

    main(sys.argv[1:])
  ```

# WEB SCRAPING

## Check What I Can Scrape

[Go Back to Summary](#summary)

- Most of the website has a filed called `robots.txt` that describes all the data that we "can" scrape

  ```Bash
    #                      ///////
    #                     //     //
    #                    //       //
    #                   //         //                           ///             ///                      ///
    #                  //           //                                          ///                      ///
    #                 //     ///     //               //// ///  ///  /// ////   /// ////     /// ////    /// ////
    #                //   ///   ///   //            //////////  ///  ////////// ///////////  //////////  ///////////
    #               //   //       //   //          ///     ///  ///  ///        ///      /// ///     /// ///      ///
    #              //    //       //    //        ///      ///  ///  ///        ///      /// ///     /// ///      ///
    #             //      //     //      //        ///     ///  ///  ///        ///     ///  ///     /// ///     ///
    #            //        //   //        //        //////////  ///  ///        //////////   ///     /// //////////
    #            //         /////         //
    #            //         /////         //
    #             //      ///   ///      //
    #               //////         //////
    #
    #
    #    We thought you'd never make it!
    #    We hope you feel right at home in this file...unless you're a disallowed subfolder.
    #    And since you're here, read up on our culture and team: https://www.airbnb.com/careers/departments/engineering
    #    There's even a bring your robot to work day.

    User-agent: Googlebot
    Allow: /calendar/ical/
    Allow: /.well-known/amphtml/apikey.pub
    Disallow: /account
    Disallow: /alumni
    Disallow: /associates/click
    Disallow: /api/v1/trebuchet
    Disallow: /api/v3
  ```

## BeautifulSoup

[Go Back to Summary](#summary)

- Before we start our project we need to install the following libraries

  ```Bash
    pip3 install beautifulsoup4
    pip3 install requests
  ```

  - The `requests` library allows us to download the data
  - The `beautifulsoup` library allows us to manipulate the data

- To check the available modules, we can use `pip list`

  ```Bash
    Package                       Version
    ----------------------------- ---------
    alabaster                     0.7.12
    appnope                       0.1.0
    astroid                       2.3.3
    attrs                         19.3.0
    Babel                         2.7.0
  ```

### BeautifulSoup Basics

[Go Back to Summary](#summary)

```Python
  import requests
  from bs4 import BeautifulSoup

  response = requests.get('https://news.ycombinator.com/news')
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup.body)
  print(soup.body.contents)
  print(soup.find_all('div'))
  print(soup.find_all('a'))
  print(soup.title)
  print(soup.a)
  print(soup.find('a'))
  print(soup.find(id='score_14123123'))
```

- the requests library is just like `fetch` in JavaScript, in this case we are making a `GET` request
- The we get the response of the request using `.text`, and we use beautifulsoup to to convert into an object that we can manipulate. In this case we are using the default parser (`html.parser`)
- We can select/target different elements
- `soup.body`, `soup.title`, `soup.a`, `soup.find('a')`, `soup.find(id='score_14123123')` - returns the first element body
- `soup.body.contents` - returns all the content inside `contents`
- `soup.find_all()` - returns all the elements of a specific type
- `soup.select('.score')` - returns all the elements that has `score` class. the `soup.select` uses css selectors to target the information. Just like `document.querySelector()`

- With beautifulSoup we can chain our data

```Bash
  import requests
  from bs4 import BeautifulSoup

  response = requests.get('https://news.ycombinator.com/news')
  soup = BeautifulSoup(response.text, 'html.parser')
  links = soup.select('.storylink') # Get all the links
  votes = soup.select('.score') # Get all the votes
  print(votes[0].get('id')) # Get the id of the first element
  # score_24469921
```

### Simple Scraper

[Go Back to Summary](#summary)

- with this simple exercise, we are going to use:

  - `getText()` the the content of the **tag** `<tag>value</tag>`
  - python `enumerate` to do a for loop using the **item** and **idx**
  - python `replace('value', 'new value')`
  - python `int()` convert into integer
  - python `str()` convert into string

  ```Bash
    import requests
    from bs4 import BeautifulSoup
    import pprint

    def sort_stories_by_votes(list):
        return sorted(list, key=lambda k: k['votes'], reverse = True);

    def create_custom_hn():
        hn = []

        for i in range(1, 2):
            response = requests.get('https://news.ycombinator.com/news?p=' + str(i))
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.select('.storylink')
            votes = soup.select('.score')
            subtext = soup.select('.subtext')

            for idx, item in enumerate(links):
                title = item.getText()
                href = item.get('href', '')
                vote = subtext[idx].select('.score')

                if len(vote):
                    points = int(vote[0].getText().replace(' points', ''))

                    if points > 99:
                        hn.append({'title': title, 'link': href, 'votes': points})

        return sort_stories_by_votes(hn)

    pprint.pprint(create_custom_hn())
  ```

# FLASK

## Flask Links

[Go Back to Summary](#summary)

- [Flask](https://flask.palletsprojects.com/)
- [Flask Request Data](https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data)
- [HTML5/CSS3 Free Templates](http://www.mashup-template.com/templates.html)
- [HTML5 UP](https://html5up.net/)
- [PythonAnyWhere](https://www.pythonanywhere.com/)
- [PythonAnyWhere - Deploy Tutorial](https://help.pythonanywhere.com/pages/Flask/)

## Flask vs. Django

[Go Back to Summary](#summary)

- Flask small framework. It's a small library that we can do things fast
- Django big framework

## New Project

[Go Back to Summary](#summary)

- Create a new project
- Create the following files and folders

  ```Bash
    touch css/style.css JavaScript/script.js index.html server.py
  ```

  ```Bash
    .
    ├── css
    │   └── style.css
    ├── JavaScript
    │   └── script.js
    ├── index.html
    └── server.py
  ```

- Then create a new virtual environment

  ```Bash
    python3 -m venv 9_Flask
  ```

  - **ATTENTION** do not run this command inside the folder (9_Flask) we have to run this command one lvl up (outside of the project's folder)
  - After we create our virtual environment we will have the following structure.

  ```Bash
    .
    ├── bin             <--- Created by Venv
    ├── css
    │   └── style.css
    ├── include         <--- Created by Venv
    ├── JavaScript
    │   └── script.js
    ├── lib             <--- Created by Venv
    ├── index.html
    ├── pyvenv.cfg      <--- Created by Venv
    ├── README.md
    └── server.py
  ```

- Then we have to activate the server

  ```Bash
    . 9_Flask/bin/activate
  ```

  - **ATTENTION** once again, we are running the command outside of the project's folder
  - After executing this command, on the terminal we will have something like `(9_Flask) Python-Course   master ` the `(9_Flask)` means that we are running in a virtual environment. Now e can install any kind of package for this environment.

  ```Bash
    pip install flask
  ```

### Start Server

[Go Back to Summary](#summary)

- In `server.py`

  - Let's build a basic web server
  - Create our server using the root file (app = Flask(\_\_name\_\_) -> `server`)
  - Create our routes using decorators - `@app.route('/')`

  ```Python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'hello world'
  ```

  - After that we just need to export our app and then run our server
  - Set the debug mode **on**, In debug mode, we don't need to restart our server to apply the changes, but we still need to refresh the browser to see the modifications.
  - In the project's folder

  ```Bash
    export FLASK_APP=server.py
    export FLASK_ENV=development
    flask run
  ```

### Flask Templates

[Go Back to Summary](#summary)

- We can send `html` using flask by importing the `render_template` method from `flask`
  - `from flask import Flask, render_template`
- With `render_template` flask will automatically look for a folder called `templates` on our root directory

  ```Bash
    .
    ├── bin
    ├── css
    │   └── style.css
    ├── include
    ├── JavaScript
    │   └── script.js
    ├── lib
    ├── templates        <---- new folder
    ├── index.html
    ├── pyvenv.cfg
    ├── README.md
    └── server.py
  ```

- in `server.py`

  ```Python
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')
  ```

#### Static Folder - CSS / JavaScript

[Go Back to Summary](#summary)

- To use **CSS** or **JavaScript** we need to create a static folder

  ```Bash
    .
    ├── bin
    ├── include
    ├── static        <---- new folder
    │   └── css
    │       └── style.css
    │   └──JavaScript
    │       └── script.js
    ├── lib
    ├── templates
    ├── index.html
    ├── pyvenv.cfg
    ├── README.md
    └── server.py
  ```

- then in our `html` files we just need to update the paths

  ```HTML
    <link rel="stylesheet" type="text/css" href="static/css/style.css">
    <script defer src="static/JavaScript/script.js"></script>
  ```

##### favicon

[Go Back to Summary](#summary)

- Adding a **favicon** we can simply import in our `html`
- With the help of [url_for](https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building)

  - To build a URL to a specific function, use the `url_for()` function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

  ```HTML
    <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico')}}">
  ```

#### Variable Rules

[Go Back to Summary](#summary)

- [Variable Rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)
- You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`.

  | string | \(default\) accepts any text without a slash |
  | ------ | -------------------------------------------- |
  | int    | accepts positive integers                    |
  | float  | accepts positive floating point values       |
  | path   | like string but also accepts slashes         |
  | uuid   | accepts UUID strings                         |

  ```Python
    from markupsafe import escape

    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % escape(username)

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # show the subpath after /path/
        return 'Subpath %s' % escape(subpath)
  ```

  ```Python
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    @app.route('/<username>')
    def hello_user(username=None):
        return render_template('index.html', name=username)
  ```

  ```HTML
    <body>
        <h1>Hi my name is {{name}}</h1>
        <h2>I am a web master</h2>
    </body>
  ```

### [Request Module](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request)

[Go Back to Summary](#summary)

- We can use flask to check the request type (`POST`, `GET`, ...)

#### The Request Object

[Go Back to Summary](#summary)

- The request object is documented in the API section. Here is a broad overview of some of the most common operations. First of all you have to import it from the flask module:

  ```Python
    from flask import request
  ```

  ```Bash
    # URL Example
    http://www.example.com/myapplication/%CF%80/page.html?x=y
  ```

  | Query       | Part                                                    |
  | ----------- | ------------------------------------------------------- |
  | path        | u'/π/page.html'                                         |
  | full_path   | u'/π/page.html?x=y'                                     |
  | script_root | u'/myapplication'                                       |
  | base_url    | u'http://www.example.com/myapplication/π/page.html'     |
  | url         | u'http://www.example.com/myapplication/π/page.html?x=y' |
  | url_root    | u'http://www.example.com/myapplication/'                |

- In `server.py`

  ```Python
    from flask import Flask, render_template, request
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    @app.route('/<string:html>')
    def serve_html(html):
        return render_template(html)

    @app.route('/submit_form', methods=['POST', 'GET'])
    def submit_form():
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            return data
        else:
            return 'Something went wrong'
  ```

- In `contact.html`

  - We can set our form to send the data to our backend
  - where the:
    - `action="/submit_form"` is the server endpoint
    - `method="POST"` to attach a method to this form
  - To use the form information in our backend, we need to give a name to the input fields. This way we ca use the `Request` library to get these form information

    - We can check the submitted form in the `Network Tab`, we will have a field called `Form Data`

    ```Bash
      email: test@test.com
      subject: Hello
      message: Hi,
      How are you?
    ```

  ```HTML
    <form action="/submit_form" method="POST" class="reveal-content">
      <div class="row">
        <div class="col-md-7">
          <div class="form-group">
            <input name="email" type="email" class="form-control" id="email" placeholder="Email">
          </div>
          <div class="form-group">
            <input name="subject" type="text" class="form-control" id="subject" placeholder="Subject">
          </div>
          <div class="form-group">
            <textarea name="message" class="form-control" rows="5" placeholder="Enter your message"></textarea>
          </div>
          <button type="submit" class="btn btn-default btn-lg">Send</button>
        </div>
      </div>
    </form>
  ```

  - In the `Headers` we send this form using the standard `Content-Type`
    - `Content-Type: application/x-www-form-urlencoded`
  - And we get a `Response` type `html`
    - `Content-Type: text/html; charset=utf-8`

### Redirect Module

[Go Back to Summary](#summary)

- We can redirect the user to another page using teh `redirect` module
- To use we just need to import the module

  - `from flask import redirect`

- Then we simply pass the route

  - `return redirect('/thankyou.html')`

- In `server.py`

```Python
  from flask import Flask, render_template, request, redirect
  app = Flask(__name__)

  ...

  @app.route('/submit_form', methods=['POST', 'GET'])
  def submit_form():
      if request.method == 'POST':
          data = request.form.to_dict()
          print(data)
          return redirect('/thankyou.html')
      else:
          return 'Something went wrong'
```

### Database

#### TXT

[Go Back to Summary](#summary)

- To save the incoming form, we can simply save into a TXT file

  ```Python
    from flask import Flask, render_template, request, redirect
    app = Flask(__name__)

    def write_to_database_txt(data):
        with open('./database/database.txt', mode='a') as database_txt:
            email = data['email']
            subject = data['subject']
            message = data['message']
            file = database_txt.write(f'\n{email}, {subject}, {message}')

    ...

    @app.route('/submit_form', methods=['POST', 'GET'])
    def submit_form():
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_database_txt(data)
            return redirect('/thankyou.html')
        else:
            return 'Something went wrong'

  ```

#### [CSV](https://docs.python.org/3/library/csv.html)

[Go Back to Summary](#summary)

- Another good option is to use the `CSV`, We just need to import the `CSV` module that comes builtin in Python

  - `import csv`
  - To write in the csv, we need to call the `.writer()` method
    - the `.writer(database, delimiter, quotechar, quoting)`
      - `database` is the file that we've just opened (`database_csv`)
      - `delimiter=','` is the separator
      - `quotechar='"'` the type of quotes that we want around our text
      - `quoting=csv.QUOTE_MINIMAL`, don't quote data if don't need it
  - To write a new row, we just call the `.writerow()` and pass as a list
    - `csv_writer.writerow([email, subject, message])`

- If csvfile is a file object, it should be opened with newline=''

- in `server.py`

  ```Python
    from flask import Flask, render_template, request, redirect
    import csv
    app = Flask(__name__)

    ...

    def write_to_database_csv(data):
        with open('./database/database.csv', newline='', mode='a') as database_csv:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])

    @app.route('/submit_form', methods=['POST', 'GET'])
    def submit_form():
        if request.method == 'POST':
            try:
                data = request.form.to_dict()
                write_to_database_csv(data)
                return redirect('/thankyou.html')
            except:
                return 'Something went wrong with the database'
        else:
            return 'Something went wrong'
  ```

## Deploying / Saving to GitHub

### requirements.txt

- To generate the installation package, run the following command inside our virtual environment

  - `pip3 freeze > requirements.txt`
  - This will generate a new file `requirements.txt` with all the package that we installed in our virtual environment

  ```Bash
    click==7.1.2
    Flask==1.1.2
    itsdangerous==1.1.0
    Jinja2==2.11.2
    MarkupSafe==1.1.1
    Werkzeug==1.0.1
  ```

[Go Back to Summary](#summary)

### .gitignore

[Go Back to Summary](#summary)

- in `.gitignore`

  ```Bash
    bin
    inclue
    lib
    pyvenv.cfg
  ```

# SELENIUM

## Selenium Links

[Go Back to Summary](#summary)

- [Python Selenium Commands Cheat Sheet](http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/)
- [Taking Screenshot Using Python Selenium WebDriver](http://allselenium.info/taking-screenshot-using-python-selenium-webdriver/)
- [Capture screenshot of an Element using Python Selenium WebDriver](http://allselenium.info/capture-screenshot-element-using-python-selenium-webdriver/)
- [Waits](https://selenium-python.readthedocs.io/waits.html)

## Installation Selenium

[Go Back to Summary](#summary)

- Install globally

  ```Bash
    pip3 install selenium
  ```

## Drivers

[Go Back to Summary](#summary)

- Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires **geckodriver**, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in `/usr/bin` or `/usr/local/bin`.

  | Chrome:  | https://sites.google.com/a/chromium.org/chromedriver/downloads        |
  | -------- | --------------------------------------------------------------------- |
  | Edge:    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
  | Firefox: | https://github.com/mozilla/geckodriver/releases                       |
  | Safari:  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          |

### webdriver

[Go Back to Summary](#summary)

- Import `webdriver` module from `selenium`
- `webdriver` allow us to interact with the browser using code - `from selenium import webdriver`
- **Driver setup**

```Python
  # Chrome
  chromedriver = webdriver.Chrome(executable_path=”Path to Chrome driver”)

  # Internet Explorer:
  iedriver = webdriver.IE(executable_path=”­Pat­h To­ IEDriverServer.exe”)

  # Edge:
  edgedriver = webdriver.Edge(executable_path=”­Pat­h To­ MicrosoftWebDriver.exe”)

  # Opera:
  operadriver = webdriver.Opera(executable_path=”­Pat­h To­ operadriver”)

  # Safari:
  # SafariDriver now requires manual installation of the extension prior to automation
```

## Modules

[Go Back to Summary](#summary)

- Important modules to import

  ```Python
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.ui import Select

    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains

    from selenium.common.exceptions import NoSuchElementException

    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.firefox.options import Options
  ```

## Browser Arguments

[Go Back to Summary](#summary)

- `–headless`: To open browser in headless mode. Works in both Chrome and Firefox browser
- `–start-maximized`: To start browser maximized to screen. Requires only for Chrome browser. Firefox by default starts maximized
- `–incognito`: To open private chrome browser
- `–disable-notifications`: To disable notifications, works Only in Chrome browser

  ```Python
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")

    # OR

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--incognito","--start-maximized","--headless")
    driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")
  ```

### Auto Download

[Go Back to Summary](#summary)

- Chrome

  ```Python
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.add_argument("download.default_directory=")

    driver = webdriver.Chrome(chrome_options=options, executable_path="Path to chrome driver")
  ```

- Firefox

  ```Python
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options

    firefoxOptions = Options()
    firefoxOptions.set_preference("browser.download.folderList",2)
    firefoxOptions.set_preference("browser.download.manager.showWhenStarting", False)
    firefoxOptions.set_preference("browser.download.dir","/data")
    firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

    firefoxdriver = webdriver.Firefox(firefox_options=firefoxOptions, executable_path="Path to firefox driver")
  ```

- We can add any MIME types in the list. MIME for few types of files are given below.

  1. Text File (.txt) – `text/plain`
  2. PDF File (.pdf) – `application/pdf`
  3. CSV File (.csv) – `text/csv` or `application/csv`
  4. MS Excel File (.xlsx) – `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` or `application/vnd.ms-excel`
  5. MS word File (.docx) – `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
  6. Zip file (.zip) – `application/zip`

- **Note:** The value of `browser.download.folderList` can be set to either `0`, `1`, or 2`.
  - `0` – Files will be downloaded on the user’s desktop.
  - `1` – Files will be downloaded in the Downloads folder.
  - `2` – Files will be stored on the location specified for the most recent download

### Disable Notifications in FireFox

[Go Back to Summary](#summary)

```Python
  firefoxOptions.set_preference(“dom.webnotifications.serviceworker.enabled”, false);
  firefoxOptions.set_preference(“dom.webnotifications.enabled”, false);
```

### Open Specific Browser Using Binary

[Go Back to Summary](#summary)

- Firefox

  ```Python
    from selenium import webdriver
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

    binary = FirefoxBinary('path/to/binary')
    driver = webdriver.Firefox(firefox_binary=binary)
  ```

- Chrome

  ```Python
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.binary_location = “”
    driver = webdriver.Chrome(chrome_options=options, executable_path=””)
    driver.get(‘http://google.com/’)
  ```

## Selenium Commands

### Read Browser Details

[Go Back to Summary](#summary)

```Python
  driver.title
  driver.window_handles
  driver.current_window_handles
  driver.current_url
  driver.page_source
```

### Go to a Specified URL

[Go Back to Summary](#summary)

```Python
  driver.get(“http://google.com”)
  driver.back()
  driver.forward()
  driver.refresh()
```

### Locating Elements

[Go Back to Summary](#summary)

- `driver.find_element_by_<property>` – To find the first element matching the given locator argument. Returns a WebElement
- `driver.find_elements_by_<property>` – To find all elements matching the given locator argument. Returns a list of WebElement

- **By ID**

  ```Python
    <input id=”q” type=”text” />

    element = driver.find_element_by_id(“q”)
  ```

- **By Name**

  ```Python
    <input id=”q” name=”search” type=”text” />

    element = driver.find_element_by_name(“search”)
  ```

- **By Class Name**

  ```Python
    <div class=”username” style=”display: block;”>…</div>

    element = driver.find_element_by_class_name(“username”)
  ```

- **By Tag Name**

  ```Python
    <div class=”username” style=”display: block;”>…</div>

    element = driver.find_element_by_tag_name(“div”)
  ```

- **By Link Text**

  ```Python
    <a href=”#”>Refresh</a>

    element = driver.find_element_by_link_text(“Refresh”)
  ```

- **By Partial Link Text**

  ```Python
    <a href=”#”>Refresh Here</a>

    element = driver.find_element_by_partial_link_text(“Refresh”)
  ```

- **By XPath**

  ```Python
    <form id=”testform” action=”submit” method=”get”>

    Username: <input type=”text” />
    Password: <input type=”password” />

    </form>

    element = driver.find_element_by_xpath(“//form[@id=’testform’]/input[1]”)
  ```

- **By CSS Selector**

  ```Python
    <form id=”testform” action=”submit” method=”get”>

    <input class=”username” type=”text” />
    <input class=”password” type=”password” />

    </form>

    element = driver.find_element_by_css_selector(“form#testform>input.username”)
  ```

#### Python Selenium Commands for Operation on Elements

[Go Back to Summary](#summary)

- **button/link/image:**

      ```Python
        click()
        get_attribute()
        is_displayed()
        is_enabled()
      ```

- **Text field:**

      ```Python
        send_keys()
        clear()
      ```

- **Checkbox/Radio:**

  ```Python
    is_selected()
    click()
  ```

- **Select:**

  - Find out the select element using any element locating strategies and then select options from list using index, visible text or option value.

  ```Python
    select = Select(driver.find_element_by_id(""))

    select.select_by_index(1)
    select.select_by_value("") # pass value
    select.select_by_visible_text("") # pass visible text
  ```

- **Element properties:**

  - These methods return either `true` or `false`.

  ```Python
    is_displayed()
    is_selected()
    is_enabled()
  ```

- **Read Attribute:**

  ```Python
    get_attribute(“”)
  ```

- **Get attribute from a disabled text box**

  ```Python
    driver.find_element_by_id(“id”).get_attribute(“value”);
  ```

- **Screenshot:**

  - **Note:** An important note to store screenshots is that `save_screenshot(‘filename’)` and `get_screenshot_as_file(‘filename’)` will work only when extension of file is **.png**. Otherwise content of the screenshot can’t be viewed.
  - Read articles for more details about taking [screenshot](http://allselenium.info/taking-screenshot-using-python-selenium-webdriver/) and element [screenshot](http://allselenium.info/capture-screenshot-element-using-python-selenium-webdriver/)

  ```Python
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path='[Browser Driver Path]')
    driver.get('[URL to Open]')

    driver.get_screenshot_as_file('sample_screenshot_2.png')
    driver.save_screenshot('sample_screenshot_1.png')
  ```

### Waits

[Go Back to Summary](#summary)

- [Waits](https://selenium-python.readthedocs.io/waits.html)
- Selenium Webdriver provides two types of waits - implicit & explicit. An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution. An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

#### Expected Conditions

[Go Back to Summary](#summary)

- There are some common conditions that are frequently of use when automating web browsers. Listed below are the names of each. Selenium Python binding provides some [convenience methods](http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions) so you don’t have to code an `expected_condition` class yourself or create your own utility package for them.

  ```Python
    title_is
    title_contains
    presence_of_element_located
    visibility_of_element_located
    visibility_of
    presence_of_all_elements_located
    text_to_be_present_in_element
    text_to_be_present_in_element_value
    frame_to_be_available_and_switch_to_it
    invisibility_of_element_located
    element_to_be_clickable
    staleness_of
    element_to_be_selected
    element_located_to_be_selected
    element_selection_state_to_be
    element_located_selection_state_to_be
    alert_is_present
  ```

  ```Python
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
  ```

#### Custom Wait Conditions

[Go Back to Summary](#summary)

- You can also create custom wait conditions when none of the previous convenience methods fit your requirements. A custom wait condition can be created using a class with `__call__` method which returns `False` when the condition doesn’t match.

  ```Python
    class element_has_css_class(object):
      """An expectation for checking that an element has a particular css class.

        locator - used to find the element
        returns the WebElement once it has the particular css class
        """
        def __init__(self, locator, css_class):
          self.locator = locator
          self.css_class = css_class

        def __call__(self, driver):
          element = driver.find_element(*self.locator)   # Finding the referenced element
          if self.css_class in element.get_attribute("class"):
              return element
          else:
              return False

      # Wait until an element with id='myNewInput' has class 'myCSSClass'
      wait = WebDriverWait(driver, 10)
      element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
  ```

#### Explicit Waits

[Go Back to Summary](#summary)

- An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.

  ```Python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Firefox()
    driver.get("http://somedomain/url_that_delays_loading")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()
  ```

  - In the code above, Selenium will wait for a maximum of `10 seconds` for an element matching the given criteria to be found. If no element is found in that time, a TimeoutException is thrown. By default, WebDriverWait calls the ExpectedCondition every **500 milliseconds** until it returns success. ExpectedCondition will return true (Boolean) in case of success or not null if it fails to locate an element.

#### Implicit Waits

[Go Back to Summary](#summary)

- An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.

  ```Python
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.implicitly_wait(10) # seconds
    driver.get("http://somedomain/url_that_delays_loading")
    myDynamicElement = driver.find_element_by_id("myDynamicElement")
  ```
