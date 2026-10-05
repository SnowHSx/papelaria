from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Papelaria Ponto Certo no ar!"

app.run(debug=True)