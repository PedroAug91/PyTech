from PyTech import create_app
from flask import redirect, request, render_template, url_for, Flask
import mysql.connector
from flask_hashing import Hashing

app = create_app()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='010705',
    database='pytech'
)

hashing = Hashing(app)

@app.route('/', methods=['GET'])
def homepage():
    cursor = db.cursor(dictionary=True)
    select = "SELECT * FROM Produto"
    cursor.execute(select)
    fetchdata = cursor.fetchall()
    
    select = "SELECT * FROM Imagem_Produto"
    cursor.execute(select)
    fetchdata2 = cursor.fetchall()
    print(fetchdata2)
    
    return render_template("homepage.html", title="Página Principal", produtos=fetchdata, imagens=fetchdata2)

@app.route("/signup", methods=['POST'])
def signup():
    nome_fisica = request.form['name']
    sobrenome_fisica = request.form['last-name']
    cpf = request.form['cpf']
    email_fisica = request.form['email']
    telefone_fisica = request.form['telephone']
    senha_fisica = request.form['password']
    
    #dando hashing na senha, hashing de 16 caracteres
    hashed_password = hashing.hash_value(senha_fisica)
    hashed_password = hashed_password[:16]
    
    #checando se o cpf já está cadastrado
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Cliente WHERE cpf='{cpf}'")
    check_pessoa_existe = cursor.fetchall()
    
    if check_pessoa_existe:
        raise Exception("Esse cpf já está cadastrado")
    else:
        # dando post no banco com as informações do cliente
        post_cliente = "INSERT INTO Cliente (nome, sobrenome, cpf, email, senha) VALUES (%s, %s, %s, %s, %s)"
        
        tupla_cliente_infos = (nome_fisica, sobrenome_fisica, cpf, email_fisica, hashed_password)
        
        cursor.execute(post_cliente, tupla_cliente_infos)
        cursor.close()
        db.commit()
        
        # criando outro cursor para pegar o id_cliente que acabou de ser adicionado para adicionar o telefone do mesmo
        cursor = db.cursor(dictionary=True)
        select_id_cliente = (f"SELECT id_cliente FROM Cliente WHERE cpf='{cpf}'")
        cursor.execute(select_id_cliente)
        fetch_cpf = cursor.fetchall()
        fetch_cpf[0]['id_cliente']
        
        post_cliente_telefone = "INSERT INTO Telefone (id_cliente, telefone) VALUES (%s, %s)"
        
        tupla_ciente_telefone = (fetch_cpf[0]['id_cliente'], telefone_fisica)
        cursor.execute(post_cliente_telefone, tupla_ciente_telefone)
        cursor.close()
        db.commit()
        return redirect("/")
    
@app.route("/signupJuridical", methods=['POST'])
def signupJuridical():
    razao_social = request.form['social-reason']
    cnpj = request.form['cnpj']
    email_juridico = request.form['email']
    telefone_juridico = request.form['telephone']
    inscricao_estadual = request.form['state-registration']
    senha_juridico = request.form['password']
    
    #dando hashing na senha, hashing de 16 caracteres
    hashed_password = hashing.hash_value(senha_juridico)
    hashed_password = hashed_password[:16]
    
    #checando se o cpf já está cadastrado
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Fornecedor WHERE cnpj='{cnpj}'")
    check_juridico_existe = cursor.fetchall()
    
    if check_juridico_existe:
        raise Exception("Esse cnpj já está cadastrado")
    else:
        # dando post no banco com as informações do fornecedor
        post_fornecedor = "INSERT INTO Fornecedor (razao_social, email, cnpj, senha, inscricao_estadual) VALUES (%s, %s, %s, %s, %s)"
        
        tupla_fornecedor_infos = (razao_social, email_juridico, cnpj, hashed_password, inscricao_estadual)
        
        cursor.execute(post_fornecedor, tupla_fornecedor_infos)
        cursor.close()
        db.commit()
        
        # criando outro cursor para pegar o id_dornecedor que acabou de ser adicionado para adicionar o telefone do mesmo
        cursor = db.cursor(dictionary=True)
        select_id_fornedor = (f"SELECT id_fornecedor FROM Fornecedor WHERE cnpj='{cnpj}'")
        cursor.execute(select_id_fornedor)
        fetch_cnpj = cursor.fetchall()
        fetch_cnpj[0]['id_fornecedor']
        
        post_fornecedor_telefone = "INSERT INTO Telefone (id_fornecedor, telefone) VALUES (%s, %s)"
        
        tupla_fornecedor_telefone = (fetch_cnpj[0]['id_fornecedor'], telefone_juridico)
        cursor.execute(post_fornecedor_telefone, tupla_fornecedor_telefone)
        cursor.close()
        db.commit()
        return redirect("/")

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

    sql = ("INSERT INTO Produto "
           "(nome_produto, preco) "
           "VALUES (%s, %s)")

    tupla = (nomeProduto, preco)
    cursor.execute(sql, tupla)
    cursor.close()
    db.commit()

    cursor = db.cursor(dictionary=True)
    select = (f"SELECT id_produto FROM Produto WHERE nome_produto='{nomeProduto}'")
    cursor.execute(select)
    fetchdata = cursor.fetchall()
    
    sql = ("INSERT INTO estoque (quantidade, id_fornecedor, id_produto) VALUES (%s, %s, %s)")
    
    tupla = (int(quant), 1, fetchdata[0]['id_produto'])
    cursor.execute(sql, tupla)
    
    sql2 = ("INSERT INTO imagem_produto "
        "(caminho, id_produto) "
        "VALUES (%s, %s)")

    tupla2 = (caminhoBD, fetchdata[0]['id_produto'])
    
    cursor.execute(sql2, tupla2)
    cursor.close()
    db.commit()

    return render_template('teste.html')

if __name__ == '__main__':
    app.run(debug=True)