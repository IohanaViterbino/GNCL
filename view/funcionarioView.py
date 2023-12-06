from controller.funcionarioController import CadastrarFuncionario, ExcluirFuncionario, AtualizarFuncionario, ListarFuncionario, BuscarFuncionario, LoginFuncionario

class FuncionarioView:
    def loginF():
        login= input("Insira o login: ")
        senha= input("Insira a senha: ")
        return LoginFuncionario.login(login, senha)

    def cadastroF():
        nome= input("Insira o seu nome: ")
        cpf= input("Insira o seu cpf: ")
        login= input("Insira o login: ")
        senha= input("Insira a senha: ")
        return CadastrarFuncionario.cadastrar_funcionario(nome,cpf,login,senha)

    def listarTudoF():
        return ListarFuncionario.listar_funcionarios()
    
    def BuscarPorNomeF(nome):
        try:
            return BuscarFuncionario.buscar_funcionario_por_nome(nome)
        except IndexError:
            print("Nome de usuário não encontrado.")

    def BuscarPorIdF(id):
        try:
            return BuscarFuncionario.buscar_funcionario_por_id(id)
        except IndexError:
            print("id de usuário não encontrado.")

    def AtualizarF(id, nome, cpf, login, senha): #colocar tratamento para campos em branco.
        try:
            return AtualizarFuncionario.alterar_dados_funcionario(id, nome, cpf, login, senha)
        except IndexError:
            print("id de usuário não encontrado.")
        

    def menuView(func):
        while True:
            print(f"\nBem vindo ao GNCL, {func.getNome()}!\nInsira a opção desejada:"
                +"\n1- Cadastro de Funcionários;"
                +"\n2- Listar Funcionários;"
                +"\n3- Buscar Funcionário por id;"
                +"\n4- Buscar Funcionário por nome;"
                +"\n5- Atualizar Funcionário (precisa do id, para concluir essa ação);")
            op=int(input())
            match(op):
                case 1:
                    FuncionarioView.cadastroF()

                case 2:
                    FuncionarioView.listarTudoF()

                case 3:
                    id=int(input("Insira o ID que procura: "))
                    FuncionarioView.BuscarPorIdF(id)

                case 4:
                    nome=input("Insira o nome que procura: ")
                    FuncionarioView.BuscarPorNomeF(nome.lower())

                case 5:
                    print("ATENÇÃO\nAS ALTERAÇÕES TEM QUE SER FEITAS EM TODAS AS INFORMAÇÕES,",
                        "CASO NÃO QUEIRA ALTERAR ALGO, INSIRA COMO ERA ANTES.")
                    id= int(input("Insira o seu Id: "))
                    nome= input("Insira o seu Nome: ")
                    cpf= input("Insira o seu Cpf: ")
                    login= input("Insira o Login: ")
                    senha= input("Insira a Senha: ")
                    FuncionarioView.AtualizarF(id, nome, cpf, login, senha)
                case _:
                    print("opção inválida. Insira uma válida")