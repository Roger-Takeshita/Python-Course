<h1 id='summary'>Summary</h1>

-   [Advanced](#advanced)
    -   [Classes](#classes)
        -   [Attributes and Methods](#attributesandmethods)
        -   [Overriding Methods](#overridingmethods)
        -   [@classmethod and @staticmethod](#classmethodsandstaticmethods)
            -   [@classmethod](#classmethods)
            -   [@staticmethod](#staticmethod)
        -   [Private and Public Variables](#privateandpublic)
        -   [Inheritance](#inheritance)
        -   [isinstance()](#isinstance)
        -   [super()](#super)
    -   [Functional Programming](#functionalprogramming)
        -   [Pure Function](#purefunction)
        -   [map()](#map)
        -   [reduce()](#reduce)
        -   [Lambada Expressions](#lambdaexpression)
    -   [List Comprehensions](#listcomprehensions)
        -   [Dictionary Comprehension](#dictionarycomprehension)
    -   [xxxxxxxx](#xxxxxxxxxxx)

<h1 id='advanced'>Advanced</h1>

<h2 id='classes'>Classes</h2>

[Go Back to Summary](#summary)

-   Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
-   The convention when we are creating a class is to capitalize the first letter of each word and singular.
-   The `__init__` method (constructor) is instantiated every time we instantiate a new object of our class

    -   In the constructor we could also create validations before creating the object, we could give default values

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

<h3 id='attributesandmethods'>Attributes and Methods</h3>

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

<h3 id='overridingmethods'>Overriding Methods</h3>

[Go Back to Summary](#summary)

-   We can change this behavior by overriding the `__str__` method that the print function calls automatically to obtain the string to print out.

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

<h3 id='classmethodsandstaticmethods'>@classmethod and @staticmethod</h3>

[Go Back to Summary](#summary)

<h4 id='classmethods'>@classmethod</h4>

-   **@classmethod** is decorator that we add before defining the class method
-   with **@classmethod** we could instantiate a new object without the need to instantiate the class
-   The naming convention of the first parameter is to use `cls` instead of `self`
-   the first parameter is always `cls`, `cls` stands for **class**

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

<h4 id='staticmethod'>@staticmethod</h4>

-   **@staticmethod** works the same way as **@classmethod** the only difference is that we don't need to define the `cls` as first parameter because **@staticmethod** doesn't have access to the class properties.
-   We just want to perform a certain method

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

<h3 id='privateandpublic'>Private and Public Variables</h3>

[Go Back to Summary](#summary)

-   Python doesn't have **public** and **private** variables that will prevent the user from changing the property of our class, but it's a convention to add `_` (single underscore) before the the variable that you want to indicate that is a private variable

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

<h3 id='inheritance'>Inheritance</h3>

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

<h3 id='isinstance'>isinstance()</h3>

[Go Back to Summary](#summary)

-   It's a builtin function in Python that checks if it's an instance of a class.

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

<h3 id='super'>super()</h3>

[Go Back to Summary](#summary)

-   The `super()` function in Python makes class inheritance more manageable and extensible. The function returns a temporary object that allows reference to a parent class by the keyword super.
-   The `super()` function has two major use cases:

    -   To avoid the usage of the super (parent) class explicitly.
    -   To enable multiple inheritances​.

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

<h2 id='functionalprogramming'>Functional Programming</h2>

[Go Back to Summary](#summary)

-   What is function programming:
    -   Clear + Understandable
    -   Easy to Extend
    -   Easy to Maintain
    -   Memory Efficient
    -   Dry

<h3 id='purefunction'>Pure Function</h3>

[Go Back to Summary](#summary)

-   Pure functions rules:
    -   Given the same input, the function always return us the same output
    -   The function should not produce side effects
        -   For example:
            -   should not have a `print()` inside this function
            -   should not modify an outside variable

<h3 id='map'>map()</h3>

[Go Back to Summary](#summary)

-   Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

    ```Python
      array = [1, 2, 3]

      def multiply_by2(array):
          return array*2

      print('new list =', list(map(multiply_by2, array)))
      print('original list =', array)
      # new list = [2, 4, 6]
      # original list = [1, 2, 3]
    ```

    -   In this case we had to convert into a list, otherwise, python will only print the memory location
    -   Notice that we don't need to execute the function `()`, we just have to point to the function and `map()` will take care for us
    -   Just like in JavaScript, `map()` creates a new list (array in JS) and doesn't affect the original list (array)

<h3 id='filter'>filer()</h3>

[Go Back to Summary](#summary)

-   The filter returns a new list (array) filtered by the condition. If the condition is equal to `True` then the filter will keep the item.
-   Just like in JavaScript, `filter()` creates a new list (array in JS) and doesn't effect the original list (array)

    ```Python
      array = [1, 2, 3, 4, 5]

      def check_odd(array):
          return array % 2 != 0

      print('new list =', list(filter(check_odd, array)))
      print('original list =', array)
      # new list = [1, 3, 5]
      # original list = [1, 2, 3, 4, 5]
    ```

<h3 id='zip'>zip()</h3>

[Go Back to Summary](#summary)

-   The `zip()` function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
-   If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

    ```Python
      my_list = [1, 2, 3]
      your_list = ["a", "b", "c", "d"]
      their_list = ["I", "II", "III", "IV"]

      print(list(zip(my_list, your_list, their_list)))
      # [(1, 'a', 'I'), (2, 'b', 'II'), (3, 'c', 'III')]
    ```

<h3 id='reduce'>reduce()</h3>

[Go Back to Summary](#summary)

-   Reduce doesn't come with Python by default, we have to import form `functools`
-   Python’s `reduce()` is a function that implements a mathematical technique called folding or reduction. `reduce()` is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.

    ```Python
      from functools import reduce
      my_list = [1, 2, 3]

      def sum_list(accumulator, array):
          return accumulator + array

      print(reduce(sum_list, my_list, 0))
      # 6
    ```

<h3 id='lambdaexpression'>Lambada Expressions</h3>

[Go Back to Summary](#summary)

-   How lambda expression works

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

<h2 id='listcomprehensions'>List Comprehensions</h2>

[Go Back to Summary](#summary)

-   how it works
-   Variable = **[** new_variable/expression **for** use_this_variable **in** string **]**

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

<h3 id='dictionarycomprehension'>Dictionary Comprehension</h3>

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
