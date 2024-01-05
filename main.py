from PyTech import create_app
from PyTech.models import Cliente, Fornecedor
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

cliente = Cliente(None, None, None, None, None)
fornecedor = Fornecedor(None, None, None, None, None)

hashing = Hashing(app)

@app.route('/', methods=['GET'])
def homepage():
    cursor = db.cursor(dictionary=True)
    select = "SELECT * FROM Produto"
    cursor.execute(select)
    produtos = cursor.fetchall()
    
    select = "SELECT * FROM Imagem_Produto"
    cursor.execute(select)
    imagens_produtos = cursor.fetchall()

    return render_template("homepage.html", title="Página Principal", produtos=produtos, imagens=imagens_produtos, cliente=cliente.nome, fornecedor=fornecedor.razao_social)

### CADASTRO DE UMA PESSOA FÍSICA/CLIENTE ###
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

### CADASTRO DE UM FORNECEDOR ###
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

### LOGIN DE UM USUÁRIO ###
@app.route("/login", methods=['GET', 'POST'])
def login():
    cpf_cnpj_email = request.form.get("info")
    senha = request.form.get("password")

    hashed_password = hashing.hash_value(senha)
    hashed_password = hashed_password[:16]
    
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Cliente WHERE email='{cpf_cnpj_email}'")
    select_email_cliente = cursor.fetchall()
    cursor.execute(f"SELECT * FROM Fornecedor WHERE email='{cpf_cnpj_email}'")
    select_email_fornecedor = cursor.fetchall()
    cursor.execute(f"SELECT * FROM Cliente WHERE cpf='{cpf_cnpj_email}'")
    select_cpf_cliente = cursor.fetchall()
    cursor.execute(f"SELECT * FROM Fornecedor WHERE cnpj='{cpf_cnpj_email}'")
    select_cnpj_fornecedor = cursor.fetchall()
    
    for dados in (select_email_fornecedor, select_email_cliente, select_cpf_cliente, select_cnpj_fornecedor):
        if(dados):
            if(hashed_password == dados[0]["senha"] and 'cpf' in dados[0]):
                cliente.set_info(dados[0]['nome'], dados[0]['sobrenome'], dados[0]['cpf'], dados[0]['email'], dados[0]['senha'])
                print(cliente.nome)
                return redirect(f'/ShoppingCart')
            elif(hashed_password == dados[0]["senha"] and 'cnpj' in dados[0]):
                fornecedor.set_info(dados[0]['razao_social'], dados[0]['cnpj'], dados[0]['email'], dados[0]['senha'], dados[0]['inscricao_estadual'])
                print(fornecedor.razao_social)
                return redirect(f'/SendProducts')
        else:
            continue
        
    raise Exception("Ei boy, esse usuario nem existe")
    
@app.route("/Product/<produto>")
def produto(produto):
    cursor = db.cursor(dictionary=True)
    select = f"SELECT * FROM produto where nome_produto = '{produto}'"
    cursor.execute(select)
    dados_produto = cursor.fetchone()

    select = f"SELECT * FROM imagem_produto where id_produto = '{dados_produto['id_produto']}'"
    cursor.execute(select)
    imagem_produto = cursor.fetchone()

    select = f"SELECT e.quantidade, f.razao_social FROM estoque e INNER JOIN fornecedor f ON e.id_fornecedor = f.id_fornecedor INNER JOIN produto p ON e.id_produto = p.id_produto WHERE p.id_produto = '{dados_produto['id_produto']}'"
    cursor.execute(select)
    quantidade_fornecedor = cursor.fetchone()

    return render_template('productPage.html', produto=dados_produto, imagem=imagem_produto, quantidade_fornecedor=quantidade_fornecedor, title=dados_produto['nome_produto'])

@app.route("/Client/<usuario>")
def client(usuario):
    return render_template('profileClient.html', cliente=cliente.nome)

@app.route("/Supplier/<usuario>")
def supplier(usuario):
    return render_template('profileSupplier.html', fornecedor=fornecedor.razao_social)

@app.route("/Admin")
def admin():
    return render_template('admin.html')

@app.route('/SendProducts')
def enviandoProdutos():
    return render_template('cadastrarProdutos.html')

### CADASTRO DE UM PRODUTO NO BANCO ###
@app.route('/cadastrarProduto', methods=['POST'])
def enviar():
    nomeProduto = request.form['nome-produto']
    preco = request.form['preco']
    quant = request.form['quantidade']
    imagem = request.files['imagem']
    
    ### Descobrir a extensao ###
    extensao = imagem.filename.rsplit('.',1)[1]
    '''
    foto.png.jpg > "foto.png.jpg".rsplit('.',1) > ['foto.png', 'jpg'][1] > jpg
    '''

    caminho = f'PyTech/static/img/produtos/{nomeProduto}.{extensao}'
    imagem.save(caminho)
    
    caminhoBD = f'../static/img/produtos/{nomeProduto}.{extensao}'
    
    cursor = db.cursor(dictionary=True)

    sql = ("INSERT INTO Produto "
           "(nome_produto, preco, id_fornecedor) "
           "VALUES (%s, %s, %s)")

    tupla = (nomeProduto, preco, 1)
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

    return render_template('homepage.html')

@app.route('/ShoppingCart')
def carrinhoCompras():
    if cliente.email != None:
        cursor = db.cursor(dictionary=True)
        
        #seleionando id do cliente a partir do email salvo através do login
        cursor.execute(f'SELECT id_cliente FROM Cliente WHERE email=\'{cliente.email}\'')
        id_cliente = cursor.fetchall()
        print(id_cliente)
        
        #seleionando carrinho do cliente 
        cursor.execute(f'SELECT id_carrinho FROM Carrinho WHERE id_cliente={id_cliente[0]["id_cliente"]}')
        carrinho_cliente = cursor.fetchall()
        
        if carrinho_cliente != []:
            #selecionando carrinho com  produtos do cliente
            cursor.execute(f'SELECT * FROM Carrinho_has_Produto WHERE id_carrinho={carrinho_cliente[0]["id_carrinho"]}')
            carrinho_comProduto_cliente = cursor.fetchall()

            #lista que guarda todos os produtos que estão no carrinho
            lista_produtos = []
            imagens_produtos = []
            fornecedor_infos = []
            
            #pegando todos os produtos, imagens e fornecedores que estão dentro do carrinho do cliente
            for produto in carrinho_comProduto_cliente:
                cursor.execute(f'SELECT * FROM Produto WHERE id_produto={produto["id_produto"]}')
                produtos_dentro_carrinho = cursor.fetchall()
                lista_produtos.append(produtos_dentro_carrinho)
                
                cursor.execute(f'SELECT * FROM imagem_produto WHERE id_produto={produto["id_produto"]}')
                imgs_produtos_dentro_carrinho = cursor.fetchall()
                imagens_produtos.append(imgs_produtos_dentro_carrinho)
                
                cursor.execute(f'SELECT * FROM Fornecedor WHERE id_fornecedor={produtos_dentro_carrinho[0]["id_fornecedor"]}')
                fornecedor_dados = cursor.fetchall()
                fornecedor_infos.append(fornecedor_dados)
            
            print(fornecedor_infos)
            return render_template("shoppingCart.html", title="Carrinho de compras", produtos = lista_produtos, quantidade_valorTot=carrinho_comProduto_cliente, imagens=imagens_produtos, cliente=cliente.nome, fornecedor=fornecedor.razao_social, vendedores=fornecedor_infos)
        else:
            return render_template("shoppingCart.html", produtos=[])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    cliente.set_info(None, None, None, None, None)
    fornecedor.set_info(None, None, None, None, None)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)