from PyTech import create_app
from flask import redirect, request, render_template, url_for, Flask
import mysql.connector
from flask_hashing import Hashing

app = create_app()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='labinfo',
    database='pytech'
)

hashing = Hashing(app)

@app.route('/', methods=['GET'])
def homepage():
    cursor = db.cursor(dictionary=True)
    select = "SELECT * FROM produto"
    cursor.execute(select)
    fetchdata = cursor.fetchall()
    
    select = "SELECT * FROM imagemproduto"
    cursor.execute(select)
    fetchdata2 = cursor.fetchall()
    print(fetchdata2)
    
    return render_template("homepage.html", title="Página Principal", produtos=fetchdata, imagens=fetchdata2)

@app.route("/signup", methods=['POST'])
def signup():
    pass

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
    nomeProduto = request.form['nome-produto']
    preco = request.form['preco']
    quant = request.form['quantidade']
    a = request.files['arq']
    
    ### Descobrir a extensao ###
    extensao = a.filename.rsplit('.',1)[1]
    '''
    foto.png.jpg > "foto.png.jpg".rsplit('.',1) > ['foto.png', 'jpg'][1] > jpg
    '''

    caminho = f'PyTech/static/img/produtos/{nomeProduto}.{extensao}'
    a.save(caminho)
    
    caminhoBD = f'../static/img/produtos/{nomeProduto}.{extensao}'
    
    cursor = db.cursor(dictionary=True)

    sql = ("INSERT INTO produto "
           "(NomeProduto, Preco) "
           "VALUES (%s, %s)")

    tupla = (nomeProduto, preco)
    cursor.execute(sql, tupla)
    cursor.close()
    db.commit()

    cursor = db.cursor(dictionary=True)
    select = (f"SELECT idproduto FROM produto WHERE NomeProduto='{nomeProduto}'")
    cursor.execute(select)
    fetchdata = cursor.fetchall()
    
    sql = ("INSERT INTO estoque (quantidade_produto, fornecedor_idfornecedor, produto_idproduto) VALUES (%s, %s, %s)")
    
    tupla = (int(quant), 1, fetchdata[0]['idproduto'])
    cursor.execute(sql, tupla)
    
    sql2 = ("INSERT INTO imagemproduto "
        "(Caminho, produto_idproduto) "
        "VALUES (%s, %s)")

    tupla2 = (caminhoBD, fetchdata[0]['idproduto'])
    
    cursor.execute(sql2, tupla2)
    cursor.close()
    db.commit()

    return render_template('teste.html')

if __name__ == '__main__':
    app.run(debug=True)