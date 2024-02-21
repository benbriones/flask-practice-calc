from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.get("/math/<operation>")
def do_operation(operation):
    """Given operation, run on received query params"""
    if len(request.args) < 2:
        return "Needed value not inputted!"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    chosen_operation = OPERATIONS[operation]

    return str(chosen_operation(a,b))


@app.get('/add')
def add_nums():
    """returns sum of url params a and b"""
    if len(request.args) < 2:
        return "Needed value not inputted!"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(add(a,b))

@app.get('/sub')
def sub_nums():
    """returns difference of url params a and b"""
    if len(request.args) < 2:
        return "Needed value not inputted!"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(sub(a,b))

@app.get('/mult')
def mult_nums():
    """returns product of url params a and b"""
    if len(request.args) < 2:
        return "Needed value not inputted!"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a,b))

@app.get('/div')
def div_nums():
    """returns quotient of url params a and b"""
    if len(request.args) < 2:
        return "Needed value not inputted!"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(div(a,b))