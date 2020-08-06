<h1 id='summary'>Summary</h1>

-   [Python Modules](#modules)
    -   [Python Package](#pythonpackage)
        -   [Different Ways To Import](#differentimport)
    -   [`__name__`](#name)

<h1 id='modules'>Python Modules</h1>

-   To create a Python module, we just have to create a new Python file (`.py`) and then import into the file we want to use

-   in `utility.py`

    ```Python
      def multiply (num1, num2):
          return num1 * num2

      def divide(num1, num2):
          return num1 / num2
    ```

-   in `main.py`

    ```Python
      import utility

      print(utility.multiply(3, 3))
      # 9
    ```

<h2 id='pythonpackage'>Python Package</h2>

[Go Back to Summary](#summary)

-   Python packages are just folders with a special file (`__init__.py`)
-   the `__init__.py` means that this is a python package
-   to import a python package, we just need to `<folder_name>.<file_name>`

-   in `shopping/shopping_cart.py`

    ```Python
      def buy(item):
      cart = []
      cart.append(item)
      return cart
    ```

-   in `main.py`

    ```Python
      import utility
      import shopping.shopping_cart

      print(utility.multiply(3, 3))
      print(shopping.shopping_cart.buy('apple'))
      # 9
      # ['apple']
    ```

<h3 id='differentimport'>Different Ways To Import</h3>

[Go Back to Summary](#summary)

-   The easiest way to import new packages is to chain the folder structure
    -   `import shopping.shopping_cart.more_shopping.cart`
-   Another way is to use `from` ... `import` ...

    -   we can partial import a package to avoid name collision

    ```Python
      from utility import multiply, divide
      from shopping.shopping_cart.more_shopping.cart import shopping_cart

      print(multiply(3, 3))
      print(shopping_cart.buy('apple'))
    ```

<h2 id='name'>__name__</h2>

[Go Back to Summary](#summary)

-   We often see something like:
    -   `if __name__ == '__main__'`
    -   This line checks if the file that we are running is the main file, in other words, if the file is the
