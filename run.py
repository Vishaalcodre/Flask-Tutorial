from datetime import datetime
from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql+pg8000://postgres:root@localhost/catalog_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="topsecret"

# app.config.update(
#     SECRET_KEY="root",
#     SQLALCHEMY_DATABASE_URI="postgresql://postgres:root@localhost/catalog_db",
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )

db = SQLAlchemy(app)

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


# strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'


# rendering templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


# JINJA TEMPLATES

# For Condition
@app.route('/watch')
def top_movies():
    movie_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template("hello.html", movies=movie_list, name="Praveen")


# If-Else Condition
@app.route('/movies')
def movie_ratings():
    movie_list = {'autopsy of jane doe': 2.5,
                  'neon demon': 3.3,
                  'ghost in a shell': 3.5,
                  'kong: skull island': 4.0,
                  'john wick 2': 4.5,
                  'spiderman - homecoming': 4.7}

    return render_template("table_data.html", movies=movie_list, name="Vishal")


@app.route('/filter')
def filter_data():
    movie_list = {'autopsy of jane doe': 2.5,
                  'neon demon': 3.3,
                  'ghost in a shell': 3.5,
                  'kong: skull island': 4.0,
                  'john wick 2': 4.5,
                  'spiderman - homecoming': 4.7}

    return render_template('filter_data.html',
                           movies=movie_list,
                           name=None,
                           film='a christmas carol')


@app.route('/macros')
def jinja_macros():
    movie_dict = {'autopsy of jane doe': 2.5,
                  'neon demon': 3.3,
                  'ghost in a shell': 3.5,
                  'kong: skull island': 4.0,
                  'john wick 2': 4.5,
                  'spiderman - homecoming': 4.7}

    return render_template('using_macros.html', movies=movie_dict)

#Session
@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'praveen'
    return render_template('session.html',session=session, name=session['name'])

#Publication Table
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer ,primary_key= True)
    name = db.Column(db.String(80), nullable= False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "The id is {} and the Name is {}".format(self.id, self.name)

#Book Table
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.now())

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
