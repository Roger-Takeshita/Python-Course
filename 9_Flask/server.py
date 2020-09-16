from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

def write_to_database_txt(data):
    with open('./database/database.txt', mode='a') as database_txt:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database_txt.write(f'\n{email}, {subject}, {message}')

def write_to_database_csv(data):
    with open('./database/database.csv', newline='', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:html>')
def serve_html(html):
    return render_template(html)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database_txt(data)
            write_to_database_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Something went wrong with the database'
    else:
        return 'Something went wrong'
