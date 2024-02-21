from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

#TODO: use .get for less scary error pages

@app.get('/add')
def add_nums():
    """returns sum of url params a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(add(a,b))

@app.get('/sub')
def sub_nums():
    """returns difference of url params a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(sub(a,b))

@app.get('/mult')
def mult_nums():
    """returns product of url params a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(mult(a,b))

@app.get('/div')
def div_nums():
    """returns quotient of url params a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(div(a,b))