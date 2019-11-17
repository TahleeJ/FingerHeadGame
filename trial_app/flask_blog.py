from flask import request, Flask, render_template, flash, session, redirect
# from flask.ext.session import Session

class Score:
    def __init__(self, score, gamerTag):
        self.score = score
        self.gamerTag = gamerTag

class Leaderboard:
    def __init__(self):
        self.board=[Score(0, "TBD")]

leaderboard = Leaderboard()
leaderboard.board.sort(key=lambda x:x.score, reverse=True)

class User:
    def __init__(self, firstName, lastName, gamerTag):
        self.firstName = firstName
        self.lastName = lastName
        self.gamerTag = gamerTag
        temp = Score(0, gamerTag)
        leaderboard.board.append(temp)
        # leaderboard.board.append(Score(0, gamerTag))
        # leaderboard.board.append({0: gamerTag})

from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Jackson Leone',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': "November 13, 2019"
    },
    {
        'author': 'Juan Nicolas Ramirez',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': "November 12, 2019"
    }
]

# scores = [leaderboard.keys()]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, leaderboard=sorted(leaderboard.board, key=lambda x: int(x.score), reverse=True))

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html', title='Webcam')

@app.route('/newUser', methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        gamerTag = request.form['gamerTag']
        currentUser = User(firstName, lastName, gamerTag)
        # flash("Welcome")
        return redirect("/home")
    else:
        return render_template('new_user.html', title='NewUser')

@app.route('/testUser', methods =['GET', 'POST'])
def testUser():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        gamerTag = request.form['gamerTag']
        score = request.form['score']
        leaderboard.board.append(Score(score, gamerTag))
            # flash("Welcome")
        return redirect("/home")
    else:
        return render_template('test_user.html', title='testUser')

if __name__ == '__main__':
    app.run(debug=True)
