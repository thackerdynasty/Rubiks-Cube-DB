from flask import Flask, render_template, url_for, request, redirect
import kociemba
import urllib.parse

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/solver')
def solver():
    return render_template("solver.html")

@app.route('/solver', methods=['POST'])
def solver_post():
    solution = kociemba.solve(request.form['cube_input'])
    return redirect(url_for("result", solution=urllib.parse.quote(solution)))

@app.route('/methods')
def methods():
    return render_template("methods/methods.html")

@app.route('/methods/cfop')
def cfop():
    return render_template("methods/cfop/cfop.html")

@app.route('/methods/cfop/ollalgs')
def cfop_oll_algs():
    return render_template("methods/cfop/ollalgs.html")

@app.route('/methods/cfop/pllalgs')
def cfop_pll_algs():
    return render_template("methods/cfop/pllalgs.html")

@app.route('/result/<solution>')
def result(solution):
    return render_template("result.html", solution=urllib.parse.unquote(solution))


if __name__ == '__main__':
    app.run(port=5000)
