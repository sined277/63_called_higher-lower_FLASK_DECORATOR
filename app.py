from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper


def make_emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


def make_underlined(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hell0_world():
    return 'Hello world!'



@app.route("/username/<name>/<int:years>")
def greet(name, years):
    return f'hello there {name} you are {years}'


if __name__ == '__main__':
    app.run(debug=True)



class User():
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authentificated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper

@is_authentificated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new post!!!")

new_user = User('Dennis')


