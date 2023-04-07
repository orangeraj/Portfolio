from flask import Flask, request

app = Flask(__name__)

@app.route('/process-form', methods=['POST'])
def process_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Save the form data to a database or send it via email
    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run()
