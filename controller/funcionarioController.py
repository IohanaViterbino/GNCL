from model.funcionarioModel import Funcionario
from database.bd import _executar

class LoginFuncionario:
    def login(login, senha):
        funcionario = BuscarFuncionario.listarFuncionarioPorLogin(login,senha)
        if funcionario.getLogin().lower() == login.lower():
            if funcionario.getSenha().lower() == senha.lower():
                print("Login validado")
                return funcionario

class CadastrarFuncionario:
    query = "CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, login TEXT, senha TEXT)"
    _executar(query)

    def cadastrar_funcionario(nome, cpf, login, senha):
       funcionario = Funcionario(nome, cpf, login.lower(), senha.lower())
       CadastrarFuncionario.cadastrarFuncionario(funcionario)
    
    def cadastrarFuncionario(object):
        query = f"INSERT INTO funcionarios(nome, cpf, login, senha) VALUES ('{object.getNome()}', '{object.getCpf()}', '{object.getLogin()}', '{object.getSenha()}')"
        _executar(query)

class AtualizarFuncionario:
    def alterar_dados_funcionario(id, nome, cpf, login, senha):
        funcionario = BuscarFuncionario.listarFuncionarioPorId(id)
        funcionario.setNome(nome)
        funcionario.setCpf(cpf)
        funcionario.setLogin(login)
        funcionario.setSenha(senha)
        AtualizarFuncionario.alterarFuncionario(funcionario)
        print("Funcionário alterado com sucesso!")

    def alterarFuncionario(object):
        query = f"UPDATE funcionarios SET nome='{object.getNome()}', cpf='{object.getCpf()}', login='{object.getLogin()}', senha='{object.getSenha()}' WHERE id={int(object.getId())}"
        _executar(query)


class ExcluirFuncionario:
    def excluir_funcionario(id):
        funcionario = BuscarFuncionario.listarFuncionarioPorId(id)
        ExcluirFuncionario.excluirFuncionario(funcionario)

    def excluirFuncionario(object):
        query = f"DELETE FROM funcionarios WHERE id={int(object.getId())}"
        _executar(query)


class ListarFuncionario:
    def listar_funcionarios():
        funcionarios = ListarFuncionario.listarUsuarios()
        for funcionario in funcionarios:
            print(funcionario)

    def listarUsuarios():
        query = "SELECT * FROM funcionarios"
        funcionarios = _executar(query)
        return funcionarios


class BuscarFuncionario:
    def buscar_funcionario_por_id(id):
        funcionario = BuscarFuncionario.listarFuncionarioPorId(id)
        if funcionario:
            print(funcionario)
        else:
            print(f"Funcionario com ID {id} não encontrado.")
            
    def buscar_funcionario_por_nome(nome):
        funcionario = BuscarFuncionario.listarFuncionarioPorNome(nome)
        if funcionario:
            print(funcionario)
        else:
            print(f"Funcionario com o nome '{nome}' não encontrado.")

    def listarFuncionarioPorId(id):
        query = f"SELECT * FROM funcionarios WHERE id={int(id)}"
        resultado = _executar(query)[0]
        funcionario = Funcionario(
            nome=resultado[1],
            cpf=resultado[2],
            login=resultado[3],
            senha=resultado[4],
            id=resultado[0]
        )
        return funcionario
        
    def listarFuncionarioPorLogin(login, senha):
        query = f"SELECT * FROM funcionarios WHERE login='{login}' and senha='{senha}'"
        resultado = _executar(query)[0]
        funcionario = Funcionario(
            nome=resultado[1],
            cpf=resultado[2],
            login=resultado[3],
            senha=resultado[4],
            id=resultado[0]
        )
        return funcionario

    def listarFuncionarioPorNome(nome):
        query = f"SELECT * FROM funcionarios WHERE nome='{nome}'"
        resultado = _executar(query)[0]
        funcionario = Funcionario(
            nome=resultado[1],
            cpf=resultado[2],
            login=resultado[3],
            senha=resultado[4],
            id=resultado[0]
        )
        return funcionario

