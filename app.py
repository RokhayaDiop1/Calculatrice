from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculatrice.html', result=None)

@app.route('/calculer', methods=['POST'])
def calculer():
    expression = request.form['expression']
    try:
        # Autoriser les fonctions mathématiques
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        result = eval(expression, {"__builtins__": None}, allowed_names)
    except Exception as e:
        result = "Erreur"
    return render_template('calculatrice.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
