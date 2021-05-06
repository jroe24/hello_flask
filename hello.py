from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/repeat/<num>/<content>')
def repeat(num,content):
    return "Hello" * int(num)

if __name__=="__main__":     
    app.run(debug=True)    
