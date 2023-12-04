from bd import _executar

class Noticias:
    def __init__(self, titulo, autor, legenda, dataEHora, texto, categoria, idFuncionario, id=None):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__texto = texto
        self.__legenda = legenda
        self.__dataEHora = dataEHora
        self.__categoria = categoria
        self.__idFuncionario = idFuncionario

        query="CREATE TABLE IF NOT EXISTS noticias(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, texto TEXT, legenda TEXT, dataEHora TEXT, categoria TEXT, idFuncionario INTERGER)" 
        _executar(query)

    def getId(self):
        return self.__id
    
    def setId(self, valor):
        self.__id = valor

    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, valor):
        self.__titulo = valor

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, valor):
        self.__autor = valor

    def getTexto(self):
        return self.__texto
    
    def setTexto(self, valor):
        self.__texto = valor

    def setLegenda(self, valor):
        self.__legenda = valor
        
    def getLegenda(self):
        return self.__legenda
    
    def getDataEHora(self):
        return self.__dataEHora
        
    def setDataEHora(self, valor):
        self.__dataEHora = valor
        
    def getCategoria(self):
        return self.__categoria
        
    def setCategoria(self, valor):
        self.__categoria = valor

    def getIdFuncionario(self):
        return self.__idFuncionario
    
    def setIdFuncionario(self, valor):
        self.__idFuncionario = valor
        
        # tudo que você precisa para comandar isso aqui de cima

    def criarNoticia(self):
        query = f"INSERT INTO  noticias (titulo, autor, texto, legenda, dataEHora, categoria, idFuncionario) VALUES ('{self.getTitulo()}', '{self.getAutor()}', '{self.getTexto()}', '{self.getLegenda()}', '{self.getDataEHora()}', '{self.getCategoria()}', '{int(self.getIdFuncionario())}')"
        _executar(query)
        print("Criado")

    def editarNoticia(self):
        query = f"UPDATE noticias SET titulo='{self.getTitulo()}', autor='{self.getAutor()}', texto='{self.getTexto()}', legenda='{self.getLegenda()}', dataEHora='{self.getDataEHora()}', categoria='{self.getCategoria()}' WHERE id={self.getId()}"
        _executar(query)

    def deletarNoticia(self):
        query = f"DELETE FROM noticias WHERE id={self.getId()}"
        _executar(query)

    @staticmethod
    def mostrarNoticias():
        query = "SELECT * FROM noticias"
        noticias = _executar(query)
        return noticias
    
    @staticmethod
    def mostrarNoticias_por_id(id):
        query = f"SELECT * FROM noticias WHERE id={int(id)}"
        noticias = _executar(query)[0]
        noticias = Noticias(id = noticias[0], titulo = noticias[1], autor = noticias[2], texto=noticias[3], legenda=noticias[4], dataEHora=noticias[5], categoria=noticias[6], idFuncionario=noticias[7])
        return noticias

    #to string
    def __str__(self):
        return f"'{self.__id}', '{self.__titulo}', '{self.__autor}'"