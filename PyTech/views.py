from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/Auth')
def auth():
    return render_template("authPage.html", title="Autenticação")

@views.route('/AuthJuridical')
def authJuridical():
    return render_template("authJuridical.html", title="Autenticação")

@views.route('/ShoppingCart')
def carrinhoCompras():
    return render_template("shoppingCart.html")

@views.route('/Sobre')
def sobre():
    return render_template("sobre.html", title="Sobre")