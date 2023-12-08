
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
        
    #to string
    def __str__(self):
        return f"ID: '{self.__id}'\nNome: '{self.__nome}'\nLogin:'{self.__login}'"
