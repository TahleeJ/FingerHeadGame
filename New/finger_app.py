from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    templs = ["layout.html", "left.jpg", "right.jpg", "up.jpg", "down.jpg"]
    return render_template(templs)

if __name__ == '__main__':
    app.run(debug=True)
