from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
    {
        "title" : "tho",
        "content" : "xxx",
        "author" : "by:",
        "gender" : 1
    },
    {
        "title" : "tho1",
        "content" : "dd",
        "author" : "by:",
        "gender" : 1
    },
    {
        "title" : "tho1",
        "content" : "dd",
        "author" : "by:",
        "gender" : 0
    }

    ]

    return render_template("index.html",
                            posts = posts
                                )



@app.route('/hello')
def hello():
     return "Hello 12"

@app.route('/hi/<name>/<age>')
def hi(name, age):
    return "Hi " + name + ". Your age: " + age

@app.route('/Sum/<int:x>/<int:y>')
def sum(x, y):

    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
