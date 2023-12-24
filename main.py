from PyTech import create_app
from flask import redirect, request, render_template, url_for, Flask
import mysql.connector
from flask_hashing import Hashing

app = create_app()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='010705',
    database='PyTech'
)

hashing = Hashing(app)

@app.route("/product/<produto>")
def produto(produto):
    return render_template('productPage.html')

@app.route("/user/usuario")
def usuario(usuario):
    return render_template('productPage.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route('/cadastrarProduto', methods=['POST'])
def enviar():
    i = request.form['idi']
    m = request.form['mens']
    a = request.files['arq']
    
    ### Descobrir a extensao ###
    extensao = a.filename.rsplit('.',1)[1]
    '''
    foto.png.jpg > "foto.png.jpg".rsplit('.',1) > ['foto.png', 'jpg'][1] > jpg
    '''

    caminho = f'PyTech/static/img/produtos/{i}.{extensao}'
    print(caminho)
    a.save(caminho)
    
    cursor = db.cursor(dictionary=True)

    sql = ("INSERT INTO produto "
           "(NomeProduto, Preco) "
           "VALUES (%s, %s)")

    tupla = (i, m)

    select = (f"SELECT idproduto "
              "FROM produto "
              "WHERE NomeProduto = '{i}'")
    cursor.execute(select)
    fetchdata = cursor.fetchall()
    print(fetchdata)
    
    sql2 = ("INSERT INTO imagemproduto "
        "(Caminho, produto_idproduto) "
        "VALUES (%s, %s)")

    tupla2 = (caminho, fetchdata)
    
    cursor.execute(sql2, tupla2)
    cursor.execute(sql, tupla)
    db.commit()
    cursor.close()

    return ('<h1>Deu Bom</h1>')

if __name__ == '__main__':
    app.run(debug=True)