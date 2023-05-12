from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/<int:number>')
def check_number(number):
    if number > random_number:
        return f'<h1>{number} is too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif number < random_number:
        return f'<h1>{number} is too low:</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    else:
        return f'<h1>Yes it {number} YOU FOUND MEEEE:</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

@app.route('/')
def my_task():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'



if __name__ == '__main__':
    app.run(debug=True)