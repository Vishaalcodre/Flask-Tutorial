from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Soldiers!"


@app.route('/new/')
def greeting(greetings="hello"):
    value = request.args.get('greeting', greetings)
    return "<h1>This is the greeting: {0}</h1>".format(value)

@app.route('/user/')
@app.route('/user/<name>')
def user(name="Praveen"):
    return "<h1>Hello {}</h1>".format(name)


@app.route('/numbers/')
@app.route('/numbers/<int:number>')
def numbers(number=5):
    return "<h1>The number is: {}</h1>".format(number)


@app.route('/temp/')
def html():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug=True)
