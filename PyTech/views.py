from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("homepage.html", title="Página Principal")

@views.route('/auth')
def auth():
    return render_template("authPage.html", title="Autenticação")

@views.route('/shoppingCart')
def carrinhoCompras():
    return render_template("shoppingCart.html")

@views.route('/sobre')
def sobre():
    return render_template("sobre.html", title="Sobre")