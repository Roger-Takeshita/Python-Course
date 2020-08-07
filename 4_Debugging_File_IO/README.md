<h1 id='summary'>Summary</h1>

-   [Debugging](#debugging)
-   [Working With Files](#workingwithfiles)
    -   [Option 1](#workingfiles1)
        -   [Read All Lines - .read()](#readfile)
        -   [Read Single Line - .readline()](#readline)
        -   [Read All Lines as a List - .readlines()](#readlines)
    -   [Option 2](#workingfiles2)
        -   [Read and Write Files - mode='r+'](#readwritefile)
        -   [Append Files - mode='a'](#appendfile)
        -   [Write Files - mode='w'](#writefile)
    -   [Paths](#paths)
    -   [Handling File Errors](#errorfiles)

<h1 id='debugging'>Debugging</h1>

[Go Back to Summary](#summary)

-   [The Python Debugger - Official Docs](https://docs.python.org/3/library/pdb.html)
-   We can enhance our debugging problem by importing `pdb` from our Python libraries.

    -   `pdb` is an interactive debugger that we can pause the code any time
        -   `pdb.set_trace()`
    -   during debugging we can also change the variables if we want to
        -   `num1 = 5`
    -   few useful commands:
        -   `step` on the terminal, we go line by line
        -   `a` returns all the available arguments
        -   `w` returns the content of the current line
        -   `continue` continue the code until we return something
        -   `exit`

    ```Python
      import pdb

      def add(num1, num2):
          pdb.set_trace()
          return num1 + num2

      add(4, 'error')
    ```

<h1 id='workingwithfiles'>Working With Files</h1>

<h2 id='workingfiles1'>Option 1</h2>

[Go Back to Summary](#summary)

-   We can import external files using `open()`

    ```Python
      my_file = open('my_txt.txt')
      print(my_file)
      # <_io.TextIOWrapper name='my_txt.txt' mode='r' encoding='UTF-8'>
    ```

    -   This will output the file wrapper with:

        -   name = `my_txt.txt`
        -   mode = `r` (read)
        -   encoding = `UTF-8` (encoding type)

-   **IMPORTANT** after we finish using the file, we have to manually close the file using `.close()`

<h3 id='readfile'>Read All Lines - .read()</h3>

[Go Back to Summary](#summary)

-   with `.read()`, Python reads the current line by using the cursor position
-   When we open the file the cursor is in the beginning of the first line
-   Once Python reads the line (`.read()`) the cursor will be in the end of the file, so if we try to run the command again, it will print nothing
-   To move the cursor to the beginning of the file, we use `.seek(0)`

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

<h3 id='readline'>Read Single Line - .readline()</h3>

[Go Back to Summary](#summary)

-   with `.readline()`, Python will read line by line

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

<h3 id='readlines'>Read All Lines as a List - .readlines()</h3>

[Go Back to Summary](#summary)

-   With `.readlines()` Python will return all the lines in a form of a list

    ```Python
      my_file = open('my_txt.txt')

      print(my_file.readlines())
      my_file.close()

      # ['Hello world\n', 'Second line\n', 'Third line\n', 'Fourth line']
    ```

<h2 id='workingfiles2'>Option 2</h2>

[Go Back to Summary](#summary)

-   A better option to work with files is to use `with`
-   **Advantage:** we don't need to manually close the file

    ```Python
      with open('my_txt.txt') as my_file:
          print(my_file.readlines())
    ```

-   `open()` method, has a second parameter (**mode**)
-   By default `mode='r'` (read only)

<h3 id='readwritefile'>Read and Write Files - mode='r+'</h3>

[Go Back to Summary](#summary)

-   `more='r+'` stands for read and write
-   When we write something to a file, the new text will be written on the current location of the cursor
-   **ATTENTION:** Be careful to now overwrite things

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

<h3 id='appendfile'>Append Files - mode='a'</h3>

[Go Back to Summary](#summary)

-   `mode='a'` will append the new information to the end of the file
-   if the file doesn't exist, Python will create one

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

<h3 id='writefile'>Write Files - mode='w'</h3>

[Go Back to Summary](#summary)

-   `mode='w'` will overwrite the whole file with the new information
-   if the file doesn't exist, Python will create one

    ```Python
      with open('my_txt.txt', mode='w') as my_file:
          text = my_file.write("Hi it's me")
          print(text)
      # 10
    ```

    ```Text
      Hi it's me
    ```

<h2 id='paths'>Paths</h2>

[Go Back to Summary](#summary)

-   Linux/Mac:

    -   We can add the relative path using `/`

    ```Python
      with open('.relative_path/../../my_txt.txt', mode='w') as my_file:
          text = my_file.write("Hi it's me")
          print(text)
    ```

-   Windows

    -   With windows we have to use `\`

    ```Python
      with open('.relative_path\..\..\my_txt.txt', mode='w') as my_file:
          text = my_file.write("Hi it's me")
          print(text)
    ```

-   A good option is to use a library to access certain files/folder in our OS like [pathlib](https://docs.python.org/3/library/pathlib.html)

<h2 id='errorfiles'>Handling File Errors</h2>

[Go Back to Summary](#summary)

-   A good way to handle errors if the file does not exist is to use a `try/except` block
-   It's also good catch `IOError`, `IOError` means that something went wrong reading/writing the file

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
