from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    n = 30 
    s = "Here are the perfect squares up to " + str(n) 
    for x in range (0, n + 1):
        s += "\n" +str(x*x) 
    return s
    