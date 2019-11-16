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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html', title='Webcam')

if __name__ == '__main__':
    app.run(debug=True)
