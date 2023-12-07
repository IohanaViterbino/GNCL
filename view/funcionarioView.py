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
    
    def buscarPorNomeF():
        try:
            nome=input("Insira o nome que procura: ")
            return BuscarFuncionario.buscar_funcionario_por_nome(nome.lower())
        
        except IndexError:
            print("Nome de usuário não encontrado.")

    def buscarPorIdF():
        try:
            id=int(input("Insira o ID que procura: "))
            return BuscarFuncionario.buscar_funcionario_por_id(id)
        
        except IndexError:
            print("id de usuário não encontrado.")

    def excluirPorIdF():
        try:
            id= int(input("Insira o Id do usuário a ser removido: "))
            return ExcluirFuncionario.excluir_funcionario(id)
        
        except IndexError:
            print("id de usuário não encontrado.")

    def atualizarF(func): #colocar tratamento para campos em branco.
        try:
            nome= input("Insira o seu novo Nome: ")
            cpf= input("Insira o seu novo Cpf: ")
            login= input("Insira o novo Login: ")
            senha= input("Insira a nova Senha: ")
            return AtualizarFuncionario.alterar_dados_funcionario(func.getId(), nome, cpf, login, senha)
        
        except IndexError:
            print("id de usuário não encontrado.")

    def listarTudoF():
        return ListarFuncionario.listar_funcionarios()
        
    def menuView(func):
        while True:
            try:
                print(f"\nBem vindo ao GNCL, {func.getNome()}!\nInsira a opção desejada:"
                    +"\n1- Cadastro de Funcionários;"
                    +"\n2- Listar Funcionários;"
                    +"\n3- Buscar Funcionário por id;"
                    +"\n4- Buscar Funcionário por nome;"
                    +"\n5- Atualizar Funcionário (precisa do id para concluir essa ação);"
                    +"\n6- Remover Funcionário (precisa do id para concluir essa ação);")
                op=int(input())

                match(op):
                    case 1:
                        FuncionarioView.cadastroF()

                    case 2:
                        FuncionarioView.listarTudoF()

                    case 3:
                        FuncionarioView.buscarPorIdF()

                    case 4:
                        FuncionarioView.buscarPorNomeF()

                    case 5:
                        print("ATENÇÃO\nAS ALTERAÇÕES TEM QUE SER FEITAS EM TODAS AS INFORMAÇÕES,",
                            "CASO NÃO QUEIRA ALTERAR ALGO, INSIRA COMO ERA ANTES.")
                        FuncionarioView.atualizarF(func)
                    case 6:
                        print("ATENÇÃO\nESSA AÇÃO É DE CARÁTER CRÍTICO!")
                        FuncionarioView.excluirPorIdF()
                        
                    case _:
                        print("opção inválida. Insira uma válida")
            except ValueError:
                print("Digite uma opção NUMÉRICA válida")