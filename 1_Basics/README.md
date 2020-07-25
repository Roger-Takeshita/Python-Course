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

-   `Lists` are like `Arrays` in other languages

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
