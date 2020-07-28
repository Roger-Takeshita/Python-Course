<h1 id='summary'>Summary</h1>

-   [Basics](#basics)
    -   [Data Types](#datatypes)
    -   [Binary Representation](#binary)
    -   [Strings](#strings)
        -   [Print Multiple Lines](#printmultistring)
        -   [Escape Sequence](#escape)
        -   [String Interpolation](#stringinter)
        -   [String Indexes](#stringindexes)
        -   [Immutability](#immutability)
    -   [Built-in Functions](#bultinfunctions)
    -   [Lists](#lists)
        -   [List Slicing](#listslicing)
        -   [List Methods](#listmethods)
        -   [List Unpacking](#listunpacking)
    -   [Dictionary](#dictionary)
    -   [Tuples](#tuples)
    -   [Sets](#sets)
    -   [Ternary Operator](#ternaryoperator)
    -   [== vs is](#equalis)
    -   [Iterables](#iterables)
    -   [Enumerate](#enumerate)
    -   [While/Else](#whileelse)
    -   [xxxxxxx](#xxxxxxxx)

<h1 id='basics'>Basics</h1>

<h2 id='datatypes'>Data Types</h2>

[Go Back to Summary](#summary)

-   In **Python** we have the following data types:
    -   int
    -   float
    -   bool
    -   str
    -   list
    -   tuple
    -   set
    -   dict
    -   complex (imaginary numbers)

<h3 id='binary'>Binary Representation</h3>

[Go Back to Summary](#summary)

```Python
  bin(5)
```

-   Gives us the binary representation of `5`, that is `0b101` -> `0b` represents in python the this is a `binary number` the actual binary is number is `101`

-   to convert a `binary number` into an `integer` we can use the `int()` with the base of `2`

```Python
  int('0b101', 2)
```

<h3 id='strings'>Strings</h3>

[Go Back to Summary](#summary)

<h4 id='printmultistring'>Print Multiple Lines</h4>

-   Use `'''` to print multiple lines

    ```Python
      multiple_lines = '''
      print
      multiple
      lines
      '''
      print(multiple_lines)
    ```

<h4 id='escape'>Escape Sequence</h4>

-   To escape a special character we use `\` before the character

    ```Python
      weather = "It\'s \"kind of\" sunny"
      print(weather)
    ```

    -   `\t` - Tab
    -   `\n` - New Line
    -   `\\` - Backslash
    -   `\r` - Carriage Return
    -   `\b` - Backspace
    -   `\f` - Form Feed
    -   `\ooo` - Octal value
    -   `\xhh` - Hex value

<h4 id='stringinter'>String Interpolation</h4>

-   Using **Python 3** format

    ```Python
      name = 'Roger'
      age = 33

      print(f'Hi {name}. You are {age} years old')
    ```

-   Using **Python 2** format

    -   **ATTENTION** the `.format()` is right after the string. The `.format()` will evaluate the `string`

    ```Python
      name = 'Roger'
      age = 33

      print('Hi {0}. You are {1} years old'.format(name, age))
    ```

-   Using `custom variables`

    -   Using custom variables we have to call them between `{}`

    ```Python
      print('Hi {new_name}. You are {new_age} years old'.format(new_name="Yumi", new_age=3))
    ```

<h4 id='stringindexes'>String Indexes</h4>

-   To work with string we have `[start:stop:stepover]`

    -   the `start` starts at index `0`
    -   `stepover`, by default the step over is `1` but we can choose any number of our choice

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

<h4 id='immutability'>Immutability</h4>

-   String are immutable, this means that once we assign a value to a string we cannot change the content (different from JavaScript), the only way to change the string content is to re-assign a complete new value to the variable

<h3 id='bultinfunctions'>Built-in Functions</h3>

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

<h2 id='lists'>Lists</h2>

[Go Back to Summary](#summary)

-   **Lists** are like **Arrays** in other languages, it's an ordered list

<h3 id='listslicing'>List Slicing</h3>

[Go Back to Summary](#summary)

-   With **list slicing** we **create a new list**

    -   One way to create a new list with all the values from the previous list is by adding `[:]`

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

<h3 id='listmethods'>List Methods</h3>

[Go Back to Summary](#summary)

-   the `.append()` method changes the list in place, it doesn't return a new new copy of the list modified.

    ```Python
      basket = [1, 2, 3, 4, 5]

      new_list = basket.append(100)
      print(basket)
      print(new_list)
      # [1, 2, 3, 4, 5, 100]
      # None
    ```

-   the `.insert()` method inserts a new item base on the index.

    -   Just like `.append()`, `.insert()` modifies the list in place (it doesn't return anything)

    ```Python
      basket = [1, 2, 3, 4, 5]

      basket.insert(3, 100)
      print(basket)
      # [1, 2, 3, 100, 4, 5]
    ```

-   the `.extend()` method extends the list, in other words, it concatenates two objects (lists)

    -   `.extend()` modifies the list in place

    ```Python
      basket = [1, 2, 3, 4, 5]

      basket.extend([100, 101])
      print(basket)
      # [1, 2, 3, 4, 5, 100, 101]
    ```

-   the `.pop()` method removes the **index** from the list and return the removed item

    ```Python
      basket = [1, 2, 3, 4, 5]

      removed_item = basket.pop(3)
      print(removed_item)
      # 4
    ```

-   the `.remove()` method removes the **value** of the list, but doesn't return anything

    ```Python
      basket = [1, 2, 3, 4, 5]

      basket.remove(3)
      print(basket)
      # [1, 2, 4, 5]
    ```

-   the `.clear()` method removes everything in place from the list.

    ```Python
      basket = [1, 2, 3, 4, 5]

      basket.clear()
      print(basket)
      # []
    ```

-   the `.index()` method, return the index of the item that we are search on the list

    ```Python
      basket = [1, 2, 3, 4, 5]

      print(basket.index(2))
      # 1
    ```

    -   We can also give a start and stop point to search for the item
    -   `.index(value, start, stop)`

-   the `'value' in object/list`, we can check True/False if the item exists in the list

    ```Python
      basket = ['a', 'b', 'c', 'd', 'e']

      print('a' in basket)
      # True
      print('f' in basket)
      # False
    ```

-   the `.count()` method counts how many time the item occurs

    ```Python
      basket = ['a', 'b', 'c', 'd', 'e' , 'd']

      print(basket.count('d'))
      # 2
    ```

-   the `.sort()` method sorts the list in place

    ```Python
      basket = ['a', 'b', 'c', 'd', 'e' , 'd']

      basket.sort()
      print(basket)
      # ['a', 'b', 'c', 'd', 'd', 'e']
    ```

-   the `sorted()` function do the same thing as `.sort()` but it creates a new sorted array

    ```Python
      basket = ['a', 'b', 'c', 'd', 'e' , 'd']

      print(sorted(basket))
      print(basket)
      # ['a', 'b', 'c', 'd', 'd', 'e']
      # ['a', 'b', 'c', 'd', 'e', 'd']
    ```

-   the `.reverse()` method reverts the list in place

    ```Python
      basket = ['a', 'b', 'c', 'd', 'e' , 'd']

      basket.reverse()
      print(basket)
      # ['d', 'e', 'd', 'c', 'b', 'a']
    ```

-   create a list using `range()`

    ```Python
      new_list = list(range(1, 100));
      print(new_list)
    ```

-   the `.join()` method iterates through the list and add join with the left part (sentence in this case)

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

<h3 id='listunpacking'>List Unpacking</h3>

[Go Back to Summary](#summary)

-   We can assign variables to each item of the list

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

<h2 id='dictionary'>Dictionary</h2>

[Go Back to Summary](#summary)

-   **Dictionary** is equal to an **object** in `JavaScript`, it's un-ordered key/value pairs

    ```Python
      dictionary = {
        'a': 1,
        'b': 2
      }

      print(dictionary['a'])
      # 1
    ```

-   the `.get()` method accepts the first argument is the `key` that we are looking for, if not found we can assign a default value (second argument).

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

-   `<value> in dict.key()`, loops through the dictionary and checks if the **key** exists

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

-   `<value> in dict.value()`, loops through the dictionary and checks if the **value** exists

    ```Python
      user = {
          'basket': [1, 2, 3],
          'greet': 'hello',
          'age': 20
      }

      print('hello' in user.values())
      # true
    ```

-   `dict.items()`, returns an array of **tuples** where the fist position (`[0]`) is the **key** and the second position (`[1]`) is the **value** (the value could be anything, number, string, object...)

    ```Python
      user = {
          'basket': [1, 2, 3],
          'greet': 'hello',
          'age': 20
      }

      print(user.items())
      # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
    ```

-   `.clear()`, clear the object in place, it removes all the items of the object. In the end we have and **empty** object

-   `.copy()` creates a brand new copy of the object (not referencing the pointer, it creates a new object)

-   `.pop()` removes the target item and returns the removed item.

-   `.update()` updates an existing item or adds if not exist

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

<h2 id='tuples'>Tuples</h2>

[Go Back to Summary](#summary)

-   it's just like a list but we cannot change the content

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

-   working we tuples, we only have 2 methods available
    -   `.count()` returns how many times the item appeared
    -   `.index()` returns the index of the item (the first found index)

<h2 id='sets'>Sets</h2>

[Go Back to Summary](#summary)

-   Removes all the duplicates from an "`object`"

    ```Python
      unique_set = {1, 3, 5, 4, 3, 2, 6}
      print(unique_set)
      # {1, 2, 3, 4, 5, 6}
    ```

-   `.difference()` returns the difference (who is calling)

    ```Python
      my_set = {1, 2, 3, 4, 5}
      your_set = {4, 5, 6, 7, 8, 9, 10}

      print(my_set.difference(your_set))
      # {1, 2, 3}
    ```

-   `.discard()` removes an item from the set

    ```Python
      my_set = {1, 2, 3, 4, 5}

      my_set.discard(5)
      print(my_set)
      # {1, 2, 3, 4}
    ```

-   `.difference_update()` returns the difference (who is calling) and modifies the original set

    ```Python
      my_set = {1, 2, 3, 4, 5}
      your_set = {4, 5, 6, 7, 8, 9, 10}

      my_set.difference_update(your_set)
      print(my_set)
      # {1, 2, 3}
    ```

-   `.intersection()` or `&` returns the intersection between two sets

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

-   `.isdisjoint()` returns `true/false` where `true` means that the two sets don't have items in common

    ```Python
      my_set2 = {1, 2, 3, 4, 5}
      your_set2 = {6, 7, 8, 9, 10}

      print(my_set2.isdisjoint(your_set2))
      # True
    ```

-   `.union()` or `|` concatenate two sets and remove duplicates

    ```Python
      my_set = {1, 2, 3, 4, 5}
      your_set = {4, 5, 6, 7, 8, 9, 10}

      print(my_set.union(your_set))
      # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    ```

-   `.issubset()` checks if the left part (who is calling) is a **subset** of the other set, returns `true/false`

    ```Python
      my_set3 = {4, 5}
      your_set3 = {4, 5, 6, 7, 8, 9, 10}

      print(my_set3.issubset(your_set3))
      # True
    ```

-   `.issuperset()` checks if the left part (who is calling) is a **superset** of the other set, returns `true/false`

    ```Python
      my_set3 = {4, 5}
      your_set3 = {4, 5, 6, 7, 8, 9, 10}

      print(your_set3.issuperset(my_set3))
      # True
    ```

<h2 id='ternaryoperator'>Ternary Operator</h2>

[Go Back to Summary](#summary)

-   [Ternary Operator - Official Docs](https://book.pythontips.com/en/latest/ternary_operators.html)
-   Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not. They became a part of Python in version 2.4

    ```Python
      value_if_true if condition else value_if_false
    ```

    ```Python
      is_nice = True

      state = "nice" if is_nice else "not nice"
      print(state)
      # nice
    ```

<h2 id='equalis'>== vs is</h2>

[Go Back to Summary](#summary)

-   `==` checks for equality value
-   `is` checks for memory location

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

<h2 id='iterables'>Iterables</h2>

[Go Back to Summary](#summary)

-   We can iterate through a `list/dictionary/tuples/sets/string` and use a shorthand to get the `key/value`

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

<h3 id='range'>Range</h3>

[Go Back to Summary](#summary)

-   We can use `range()` that creates a special kind of object that we can iterate
-   `range(start, stop, step)`

    -   by default the step is not specified is `1`

    ```Python
      for number in range(0,100):
        print(number)
    ```

<h3 id='enumerate'>Enumerate</h3>

[Go Back to Summary](#summary)

-   Using enumerate, it gives us accesses to the index for the `list/dictionary/tuples/sets/string`

```Python
  for index, value in enumerate('Helllloooooo'):
    print(index, value)
```

<h2 id='whileelse'>While/Else</h2>

[Go Back to Summary](#summary)

-   We can use `else` condition with `while`. The `else` part will be only executed if the `while` loop executed successfully

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
