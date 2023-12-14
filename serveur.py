from flask import Flask, render_template
from src.movies import mainProgram

app = Flask(__name__)

@app.route('/')
def index():
    movies = mainProgram()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)