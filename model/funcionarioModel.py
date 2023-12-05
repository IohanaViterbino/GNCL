from bd import _executar

class Funcionario:
    def __init__(self, nome, cpf, login, senha, id=None):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__login = login
        self.__senha = senha

    def getId(self):
        return self.__id
    def setId(self, novo_id):
        self.__id = novo_id

    def getNome(self):
        return self.__nome
    def setNome(self, novo_nome):
        self.__nome = novo_nome

    def getCpf(self):
        return self.__cpf
    def setCpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def getLogin(self):
        return self.__login
    def setLogin(self, novo_login):
        self.__login = novo_login

    def getSenha(self):
        return self.__senha
    def setSenha(self, nova_senha):
        self.__senha = nova_senha

    query = "CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, login TEXT, senha TEXT)"
    _executar(query)
   
    # Inserir
    def cadastrarFuncionario(self):
        query = f"INSERT INTO funcionarios(nome, cpf, login, senha) VALUES ('{self.getNome()}', '{self.getCpf()}', '{self.getLogin()}', '{self.getSenha()}')"
        _executar(query)
    # Alterar
    def alterarFuncionario(self):
        query = f"UPDATE funcionarios SET nome='{self.getNome()}', cpf='{self.getCpf()}', login='{self.getLogin()}', senha='{self.getSenha()}' WHERE id={int(self.getId())}"
        _executar(query)

    # Excluir
    def excluirFuncionario(self):
        query = f"DELETE FROM funcionarios WHERE id={int(self.getId())}"
        _executar(query)

    # Listar professores cadastrados.
    @staticmethod
    def listarUsuarios():
        query = "SELECT * FROM funcionarios"
        funcionarios = _executar(query)
        return funcionarios

    # Buscar professor pelo ID.
    @staticmethod
    def listarFuncionarioPorId(id):
        query = f"SELECT * FROM funcionarios WHERE id={int(id)}"
        resultado = _executar(query)[0]
        if resultado:
            funcionario = Funcionario(
                nome=resultado[1],
                cpf=resultado[2],
                login=resultado[3],
                senha=resultado[4],
                id=resultado[0]
            )
            return funcionario
        else:
            return None

    #to string
    def __str__(self):
        return f"'{self.__nome}': '{self.__id}'"
