from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    users = {
	"quy":   {
			"name": "Dinh Cong Quy",
			"age": 20
                    },
    "love" : {
			"name" : "love love",
			"age" : 20
             }
            }

    if name in users:
        inf = users[name]
        return render_template("ex2.html",inf = inf)
    else:
        return "User not found"

if __name__ == '__main__':
    app.run(debug=True)
