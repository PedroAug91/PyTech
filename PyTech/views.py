from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/auth')
def auth():
    return render_template("authPage.html", title="Autenticação")

@views.route('/authJuridical')
def authJuridical():
    return render_template("authJuridical.html", title="Autenticação")

@views.route('/shoppingCart')
def carrinhoCompras():
    return render_template("shoppingCart.html")

@views.route('/sobre')
def sobre():
    return render_template("sobre.html", title="Sobre")