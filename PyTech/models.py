class Cliente:
    def __init__(self, nome, sobrenome, cpf, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        
    def get_email(self):
        return self.email
      
    def set_info(self, nome, sobrenome, cpf, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.senha = senha
      
class Fornecedor:
    def __init__(self, razao_social, cnpj, email, senha, inscricao_estadual):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.email = email
        self.senha = senha
        self.inscricao_estadual = inscricao_estadual
    
    def get_email(self):
        return self.email
      
    def set_info(self, razao_social, cnpj, email, senha, inscricao_estadual):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.email = email
        self.senha = senha
        self.inscricao_estadual = inscricao_estadual