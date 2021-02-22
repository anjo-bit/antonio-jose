import os
from models import cliente
from pages import tela_admin, tela_cliente, tela_entregador

def telaLogin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*************************************")
    print("             Açai Universo            ")
    print("Bem vindo a melhor acaiteria da cidade!")
    print("--------------------------------------")
    print("Digite email e senha para continuar...")
    try:  
      email = input("Digite seu email: ")
    except:
      print('email contem erro')
    try:
      senha = input("Digite sua senha: ")
    except:
      print('senha contem erro')    
    minhaConta = cliente.Cliente()
    role = minhaConta.fazerLogin(email, senha)
    try:
      if(role == 1):
        tela_admin.telaAdmin()
      elif(role == 2):
        tela_entregador.telaEntregador()
      elif(role == 3):
        tela_cliente.telaCliente(minhaConta)
    except ValueError:
      print('algo nao esta certo')
    finally:
      print('tudo ocorreu corretamente')

