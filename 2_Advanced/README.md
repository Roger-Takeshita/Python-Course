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
    -   [xxxxxxxx](#xxxxxxx)

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
