# SUMMARY

- [SUMMARY](#summary)
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

# FLASK

## Flask Links

[Go Back to Summary](#summary)

-   [Flask](https://flask.palletsprojects.com/)
-   [Flask Request Data](https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data)
-   [HTML5/CSS3 Free Templates](http://www.mashup-template.com/templates.html)
-   [HTML5 UP](https://html5up.net/)
-   [PythonAnyWhere](https://www.pythonanywhere.com/)
-   [PythonAnyWhere - Deploy Tutorial](https://help.pythonanywhere.com/pages/Flask/)

## Flask vs. Django

[Go Back to Summary](#summary)

-   Flask small framework. It's a small library that we can do things fast
-   Django big framework

## New Project

[Go Back to Summary](#summary)

-   Create a new project
-   Create the following files and folders

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

-   Then create a new virtual environment

    ```Bash
      python3 -m venv 9_Flask
    ```

    -   **ATTENTION** do not run this command inside the folder (9_Flask) we have to run this command one lvl up (outside of the project's folder)
    -   After we create our virtual environment we will have the following structure.

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

-   Then we have to activate the server

    ```Bash
      . 9_Flask/bin/activate
    ```

    -   **ATTENTION** once again, we are running the command outside of the project's folder
    -   After executing this command, on the terminal we will have something like `(9_Flask) Python-Course   master ` the `(9_Flask)` means that we are running in a virtual environment. Now e can install any kind of package for this environment.

    ```Bash
      pip install flask
    ```

### Start Server

[Go Back to Summary](#summary)

-   In `server.py`

    -   Let's build a basic web server
    -   Create our server using the root file (app = Flask(\_\_name\_\_) -> `server`)
    -   Create our routes using decorators - `@app.route('/')`

    ```Python
      from flask import Flask
      app = Flask(__name__)

      @app.route('/')
      def hello_world():
          return 'hello world'
    ```

    -   After that we just need to export our app and then run our server
    -   Set the debug mode **on**, In debug mode, we don't need to restart our server to apply the changes, but we still need to refresh the browser to see the modifications.
    -   In the project's folder

    ```Bash
      export FLASK_APP=server.py
      export FLASK_ENV=development
      flask run
    ```

### Flask Templates

[Go Back to Summary](#summary)

-   We can send `html` using flask by importing the `render_template` method from `flask`
    -   `from flask import Flask, render_template`
-   With `render_template` flask will automatically look for a folder called `templates` on our root directory

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

-   in `server.py`

    ```Python
      from flask import Flask, render_template
      app = Flask(__name__)

      @app.route('/')
      def hello_world():
          return render_template('index.html')
    ```

#### Static Folder - CSS / JavaScript

[Go Back to Summary](#summary)

-   To use **CSS** or **JavaScript** we need to create a static folder

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

-   then in our `html` files we just need to update the paths

    ```HTML
      <link rel="stylesheet" type="text/css" href="static/css/style.css">
      <script defer src="static/JavaScript/script.js"></script>
    ```

##### favicon

[Go Back to Summary](#summary)

-   Adding a **favicon** we can simply import in our `html`
-   With the help of [url_for](https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building)

    -   To build a URL to a specific function, use the `url_for()` function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

    ```HTML
      <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico')}}">
    ```

#### Variable Rules

[Go Back to Summary](#summary)

-   [Variable Rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)
-   You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`.

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

-   We can use flask to check the request type (`POST`, `GET`, ...)

#### The Request Object

[Go Back to Summary](#summary)

-   The request object is documented in the API section. Here is a broad overview of some of the most common operations. First of all you have to import it from the flask module:

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

-   In `server.py`

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

-   In `contact.html`

    -   We can set our form to send the data to our backend
    -   where the:
        -   `action="/submit_form"` is the server endpoint
        -   `method="POST"` to attach a method to this form
    -   To use the form information in our backend, we need to give a name to the input fields. This way we ca use the `Request` library to get these form information

        -   We can check the submitted form in the `Network Tab`, we will have a field called `Form Data`

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

    -   In the `Headers` we send this form using the standard `Content-Type`
        -   `Content-Type: application/x-www-form-urlencoded`
    -   And we get a `Response` type `html`
        -   `Content-Type: text/html; charset=utf-8`

### Redirect Module

[Go Back to Summary](#summary)

-   We can redirect the user to another page using teh `redirect` module
-   To use we just need to import the module

    -   `from flask import redirect`

-   Then we simply pass the route

    -   `return redirect('/thankyou.html')`

-   In `server.py`

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

-   To save the incoming form, we can simply save into a TXT file

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

-   Another good option is to use the `CSV`, We just need to import the `CSV` module that comes builtin in Python

    -   `import csv`
    -   To write in the csv, we need to call the `.writer()` method
        -   the `.writer(database, delimiter, quotechar, quoting)`
            -   `database` is the file that we've just opened (`database_csv`)
            -   `delimiter=','` is the separator
            -   `quotechar='"'` the type of quotes that we want around our text
            -   `quoting=csv.QUOTE_MINIMAL`, don't quote data if don't need it
    -   To write a new row, we just call the `.writerow()` and pass as a list
        -   `csv_writer.writerow([email, subject, message])`

-   If csvfile is a file object, it should be opened with newline=''

-   in `server.py`

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

-   To generate the installation package, run the following command inside our virtual environment

    -   `pip3 freeze > requirements.txt`
    -   This will generate a new file `requirements.txt` with all the package that we installed in our virtual environment

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

-   in `.gitignore`

    ```Bash
      bin
      inclue
      lib
      pyvenv.cfg
    ```
