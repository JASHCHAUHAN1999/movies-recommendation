from flask import Flask , render_template , request

import movies


app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def hello():
    movies_pred=""
    if request.method =="POST":
        movie = request.form["movie"]
        movies_pred = movies.movies_prediction(movie)
        #mr = movies_pred
    return render_template("index.html", mov = movies_pred)
"""
@app.route("/sub", methods = ["POST"])
def submit():
    # html -> py
    if request.method == "POST":
        name = request.form["movie"]
    # py -> html
    return render_template("sub.html", n = name)

"""


if __name__ == "__main__":
    app.run(debug=True)


