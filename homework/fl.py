from flask import Flask
from fib_num import fib_nums

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Returning Fibonacci numbers</p>'

@app.route('/num/<int:cnt>')
def get_fib(cnt):
    fib_gen = fib_nums(cnt)
    ret = []
    for _ in range(cnt):
        ret.append(next(fib_gen))
    return ret
