from model.funcionarioModel import Funcionario

class LoginFuncionario:
    @staticmethod
    def login(login, senha, id):
        funcionario = Funcionario.listarFuncionarioPorId(id)
        if funcionario.getLogin().lower() == login.lower():
            if funcionario.getSenha().lower() == senha.lower():
                print("Login validado")
                return True
            else:
                print("Senha inválida. Tente novamente")
                return False
        else:
            print("Login inválido. Tente novamente")
            return False

class CadastrarFuncionario:
    @staticmethod
    def cadastrar_funcionario(nome, cpf, login, senha):
        funcionario = Funcionario(nome, cpf, login, senha)
        funcionario.cadastrarFuncionario()

class AtualizarFuncionario:
    @staticmethod
    def alterar_dados_funcionario(id, nome, cpf, login, senha):
        funcionario = Funcionario.listarFuncionarioPorId(id)
        if funcionario:
            funcionario.setNome(nome)
            funcionario.setCpf(cpf)
            funcionario.setLogin(login)
            funcionario.setSenha(senha)
            funcionario.alterarFuncionario()
        else:
            print(f"Funcionario com ID {id} não encontrado.")

class ExcluirFuncionario:
    @staticmethod
    def excluir_funcionario(id):
        funcionario = Funcionario.listarFuncionarioPorId(id)
        if funcionario:
            funcionario.excluirFuncionario()
        else:
            print(f"Funcionario com ID {id} não encontrado.")

class ListarFuncionario:
    @staticmethod
    def listar_funcionarios():
        funcionarios = Funcionario.listarUsuarios()
        for funcionario in funcionarios:
            print(funcionario)

class BuscarFuncionario:
    @staticmethod
    def buscar_funcionario_por_id(id):
        funcionario = Funcionario.listarFuncionarioPorId(id)
        if funcionario:
            print(funcionario)
        else:
            print(f"Funcionario com ID {id} não encontrado.")
