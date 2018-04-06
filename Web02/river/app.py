from flask import Flask, render_template
from models.river import River
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete-all')
def deleteAll():
    River.objects.delete()
    return render_template('index.html')
#exercise8
@app.route("/africa")
def africa():
    rivers = River.objects(continent="Africa")
    if rivers is None:
        return "river not found"
    else:
        return render_template('rivers.html', rivers=rivers)
#exercise9
@app.route("/S.America")
def s_america():
    rivers = River.objects(continent="S. America", length__lt=1000)
    if rivers is None:
        return "river not found"
    else:
        return render_template('rivers.html', rivers=rivers)

if __name__ == '__main__':
  app.run(debug=True)
