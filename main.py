from PyTech import create_app
from flask import redirect, request, render_template, url_for
import mysql.connector
from flask_hashing import Hashing

app = create_app()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='labinfo',
    database='PyTech'
)

hashing = Hashing(app)

@app.route("/product/<produto>")
def produto(produto):
    return render_template('productPage.html')

@app.route("/user/usuario")
def usuario(usuario):
    return render_template('productPage.html')

if __name__ == '__main__':
    app.run(debug=True)