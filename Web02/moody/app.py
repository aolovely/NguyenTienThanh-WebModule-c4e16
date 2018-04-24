from flask import *
from models.service import User, Song, Book, Video, Place
import mlab
from chuanhoa import ChuanHoa
from random import*

app = Flask(__name__)
app.secret_key = "moody"

mlab.connect()

admin = User.objects(username="admin", password="admin").first()
admin_id = str(admin["id"])

count = 0

@app.route('/')
def index():
    if "user_id" in session:
        return render_template('index.html')
    else:
        global count
        count += 1
        if count < 5:
            return render_template('index.html')
        else:
            return redirect(url_for('signup'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        acc = User.objects(username=username, password=password).first()
        if acc is None:
            return "tai khoan nay k ton tai"
        else:
            session["user_id"] = str(acc["id"])
            return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'user_id' in session:
        del session['user_id']
        return redirect(url_for('index'))
    else:
        return 'Have not logged in'

@app.route('/signup', methods=['GET','POST'])
def signup():
    global count
    count = 0
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        form = request.form
        new_user = User(fullname=form["fullname"],
                        username=form["username"],
                        password=form["password"],
                        email=form["email"],
                        )
        new_user.save()
        return redirect(url_for('login'))

@app.route('/recommend/<int:happy>')
def recommend(happy):
    global admin_id
    all_song_admin = Song.objects(happy=happy, user_id=admin_id)
    song_admin = sample(all_song_admin,4)

    all_book_admin = Book.objects(happy=happy, user_id=admin_id)
    book_admin = sample(all_book_admin,4)

    all_video_admin = Video.objects(happy=happy, user_id=admin_id)
    video_admin = sample(all_film_admin,4)

    all_place_admin = Place.objects(happy=happy, user_id=admin_id)
    place_admin = sample(all_place_admin,4)
    # user
    all_song_user = Song.objects(happy=happy, user_id__ne=admin_id)
    song_user = choice(all_song_user)

    all_book_user = Book.objects(happy=happy, user_id__ne=admin_id)
    book_user = choice(all_book_user)

    all_video_user = Video.objects(happy=happy, user_id__ne=admin_id)
    video_user = choice(all_film_user)

    all_place_user = Place.objects(happy=happy, user_id__ne=admin_id)
    place_user = choice(all_place_user)
    return render_template('recommend.html', song_admin=song_admin,
                                             book_admin=book_admin,
                                             video_admin=film_admin,
                                             place_admin=place_admin,
                                             song_user=song_user,
                                             book_user=book_user,
                                             video_user=film_user,
                                             place_user=place_user,
                                             )
#     #nguoi dung them
@app.route('/add', methods=["GET", "POST"])
def add():
    if  request.method == "GET":
        if "user_id" in session:
            return render_template("add.html")
        else:
            return redirect(url_for('login'))
    elif request.method == "POST":
        form = request.form
        new_song = Song(happy = form["happy"],
                        name = ChuanHoa(form["name"]),
                        author = form["singer"],
                        link = form["link"],
                        link_img = form["link_img"],
                        user_id = session["user_id"])
        new_song.save()
        new_book = Book(happy = form["happy"],
                        name = ChuanHoa(form["name"]),
                        author = form["author"],
                        link = form["link"],
                        link_img = form["link_img"],
                        user_id = session["user_id"])
        new_book.save()
        new_video = Video(happy = form["happy"],
                        name = ChuanHoa(form["name"]),
                        author = form["director"],
                        link = form["link"],
                        link_img = form["link_img"],
                        user_id = session["user_id"])
        new_video.save()
        new_place = Place(happy = form["happy"],
                          name = ChuanHoa(form["name"]),
                          describe = form["describe"],
                          link = form["happy"],
                          user_id = session["user_id"])
        new_place.save()
#trang quan tri cua nguoi dung
@app.route('/admin_user')
def admin_user():
    if "user_id" in session:
        all_song_user = Song.objects(happy=happy, user_id=session["user_id"])
        all_book_user = Book.objects(happy=happy, user_id=session["user_id"])
        all_video_user = Video.objects(happy=happy, user_id=session["user_id"])
        all_place_user = Place.objects(happy=happy, user_id=session["user_id"])
        return render_template("admin_user.html", all_song_user=all_song_user,
                                                  all_book_user=all_book_user,
                                                  all_video_user=all_film_user,
                                                  all_place_user=all_place_user,)
    else:
        return redirect(url_for('login'))

@app.route('/delete_song/<song_id>')
def delete_song(song_id):
    song = Song.objects.with_id(song_id)
    if song is None:
        return "not found"
    else:
        song.delete()
        return redirect(url_for('admin_user'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    book = Book.objects.with_id(book_id)
    if book is None:
        return "not found"
    else:
        book.delete()
        return redirect(url_for('admin_user'))

@app.route('/delete_video/<video_id>')
def delete_video(video_id):
    video = Video.objects.with_id(film_id)
    if video is None:
        return "not found"
    else:
        film.delete()
        return redirect(url_for('admin_user'))

@app.route('/delete_place/<place_id>')
def delete_place(place_id):
    place = Place.objects.with_id(place_id)
    if place is None:
        return "not found"
    else:
        place.delete()
        return redirect(url_for('admin_user'))

@app.route('/update_song/<song_id>', methods=["GET", "POST"])
def update_song(song_id):
    song = Song.objects.with_id(song_id)
    if song is None:
        return "not found"
    else:
        if  request.method == "GET":
            return render_template("update_song.html", song=song)
        elif request.method == "POST":
            form = request.form
            song.update(set__happy = form["happy"],
                        set__name = ChuanHoa(form["name"]),
                        set__author = form["singer"],
                        set__link = form["link"],
                        set__link_img = form["link_img"],
                        )
            song.reload()
            return redirect(url_for('admin_user'))

@app.route('/update_book/<book_id>', methods=["GET", "POST"])
def update_book(book_id):
    book = Book.objects.with_id(book_id)
    if book is None:
        return "not found"
    else:
        if  request.method == "GET":
            return render_template("update_book.html", book=book)
        elif request.method == "POST":
            form = request.form
            book.update(set__happy = form["happy"],
                        set__name = ChuanHoa(form["name"]),
                        set__author = form["singer"],
                        set__link = form["link"],
                        set__link_img = form["link_img"],
                        )
            book.reload()
            return redirect(url_for('admin_user'))

@app.route('/update_film/<film_id>', methods=["GET", "POST"])
def update_video(video_id):
    video = Video.objects.with_id(film_id)
    if video is None:
        return "not found"
    else:
        if  request.method == "GET":
            return render_template("update_film.html", film=film)
        elif request.method == "POST":
            form = request.form
            video.update(set__happy = form["happy"],
                        set__name = ChuanHoa(form["name"]),
                        set__author = form["singer"],
                        set__link = form["link"],
                        set__link_img = form["link_img"],
                        )
            video.reload()
            return redirect(url_for('admin_user'))

@app.route('/update_place/<place_id>', methods=["GET", "POST"])
def update_place(place_id):
    place = Place.objects.with_id(place_id)
    if place is None:
        return "not found"
    else:
        if  request.method == "GET":
            return render_template("update_place.html", place=place)
        elif request.method == "POST":
            form = request.form
            place.update(set__happy = form["happy"],
                        set__name = ChuanHoa(form["name"]),
                        set__describe = form["singer"],
                        set__link = form["link"],
                        )
            place.reload()
            return redirect(url_for('admin_user'))
if __name__ == '__main__':
  app.run(debug=True)
