from flask import request, Flask, render_template, flash, redirect

global currentUser

class Score:
    def __init__(self, score, gamerTag):
        self.score = score
        self.gamerTag = gamerTag

class Leaderboard:
    def __init__(self):
        self.board=[Score(0, "TBD")]

leaderboard = Leaderboard()

class User:
    def __init__(self, firstName, lastName, gamerTag):
        self.firstName = firstName
        self.lastName = lastName
        self.gamerTag = gamerTag
        temp = Score(0, gamerTag)
        leaderboard.board.append(temp)
        # leaderboard.board.append(Score(0, gamerTag))
        # leaderboard.board.append({0: gamerTag})

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/leaderboard')
def scores():
    return render_template('leaderboard.html', leaderboard=sorted(leaderboard.board, key=lambda x: int(x.score), reverse=True))

@app.route('/introduction')
def introduction():
    return render_template("instructions.html")


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
