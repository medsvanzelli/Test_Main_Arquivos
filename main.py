

usuarios = []
senhas = []
logado = 0

while True:
    menu = input("Digite '1' para cadastrar um usuário ou '2' para fazer login: ")

    if menu == '1':
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        usuarios.append(usuario)
        senhas.append(senha)
        with open('usuarios.txt','a') as arquivo_usuarios:
          arquivo_usuarios.write(usuario +';'+ senha)
          arquivo_usuarios.write('\n')

           
    elif menu == '2':
        
      usuario_entrar = input("Digite o nome do usuário: ")
      senha_entrar = input("Digite a senha do usuário: ")
      senhas_usuario = open('usuarios.txt', 'r')
      for linha in senhas_usuario:
        usuario_senha = linha.split(';')
        usuario_senha[1] = usuario_senha[1].replace("\n", '')
        if usuario_entrar == usuario_senha[0] and senha_entrar == usuario_senha[1]:
          logado = True

        else:
          logado = False
          

      if logado == True:
        print('Login realizado com sucesso')
        break
      else:
        print('Usuário ou senha inválidos, tente novamente')
