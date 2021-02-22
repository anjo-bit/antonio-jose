
class Usuario(object):
  id_counter = 0
  def __init__(self):
    self.id= Usuario.id_counter
    Usuario.id_counter += 1
    self.nome = ""
    self.foto = ""
    self.email = ""
    self.telefone = ""
    self.senha = ""
    self.endereco = ""
    self.permissao = 0
    dados_cliente = {
        'Nome': '',
        'Email': '',
        'Senha': '',
        'Telefone': '',
        'Endereço': '' 
    }
  def fazerLogin(self,email,senha):
    usuarios = dados_cliente
    for user in usuarios:
      usuarioModel =  dados_cliente[]
      email_user = dados_cliente['Email']
      email.split(' ')
      email_user.split(' ')
      senha_user = dados_cliente['Senha']
      role = usuarioModel["role"]
      if (email == email_user and senha == senha_user ):
        print("acesso autorizado")
        self.email = email
        self.senha = senha
        self.nome = usuarioModel["nome"]
        if (role == 1):
          return 1
        elif(role == 2):
          return 2
        elif(role == 3):
          return 3
        break
      else:
        print("acesso negado")
      
  def fazerLogout(self):
    self.email = None
    self.senha = None
  def registrarConta(self,nome,email, senha, telefone):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.telefone = telefone
    nome = int(input(""))
    email = int(input(""))
    senha = int(input(""))
    telefone = int(input(""))

    dados_cliente = {
        'Nome': nome,
        'Email': email,
        'Senha': senha,
        'Telefone': telefone 
    }
    p = int(input("deseja ver seus dados?(sim/nao)"))
    if p == "sim":
      print(dados_cliente['Nome'])
      print(dados_cliente['Email'])
      print(dados_cliente['Senha'])
      print(dados_cliente['Telefone'])
    else:
      print("tenha um bom dia")
  def editarConta(self,nome,email,senha, foto):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.foto = foto
    dados_cliente = {
        'Nome': nome,
        'Email': email,
        'Senha': senha
    }

    print(dados_cliente['Nome'])
    print(dados_cliente['Email'])
    print(dados_cliente['Senha'])
    