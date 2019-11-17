from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    # return "hello world"
    return render_template('/hello.html')

if __name__ == '__main__':
    app.run(debug=True)
