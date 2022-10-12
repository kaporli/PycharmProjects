from flask import Flask
import random

app = Flask(__name__)


def func(function):
    def wrapper(*args, **kwargs):
        function()
    return wrapper
# def make_bold(string):
#     return f"<b>{string}<b/>"


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Guess a number from 0-9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


# @make_bold
@app.route("/bye")
def bye():
    return "Bye"

the_number = random.randint(0,9)

@app.route("/<number>")
def display(number):
    if int(number) == the_number:
        return f"You got it! The number is {the_number}!"
    elif int(number) > the_number:
        return "Too high"
    elif int(number) < the_number:
        return "Too low"

print(the_number)
app.run(debug=True)