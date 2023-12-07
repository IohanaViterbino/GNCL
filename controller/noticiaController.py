
from model.noticiaModelo import Noticias
from model.funcionarioModel import Funcionario
from datetime import datetime

class CadastrarNoticia:
    @staticmethod
    def cadastrar_noticia(titulo, autor, texto, legenda, categoria, idFuncionario):
        if Funcionario.listarFuncionarioPorId(idFuncionario):
            noticia = Noticias(titulo.lower(), autor, texto, legenda, datetime.now(), categoria, idFuncionario)
            noticia.criarNoticia()

class AtualizarNoticia:
    @staticmethod
    def alterar_dados_noticia(id, titulo, autor, texto, legenda, categoria, idFuncionario):
        if Funcionario.listarFuncionarioPorId(idFuncionario):
            noticia = Noticias.mostrarNoticias_por_id(id)
            if noticia:
                noticia.setAutor(autor)
                noticia.setTitulo(titulo.lower())
                noticia.setDataEHora(datetime.now())
                noticia.setTexto(texto)
                noticia.setLegenda(legenda)
                noticia.setCategoria(categoria)
                noticia.setIdFuncionario(idFuncionario)
                noticia.editarNoticia()
            else:
                print(f"Notícia com ID {id} não encontrado.")

class ExcluirNotícia:
    @staticmethod
    def excluir_noticia(id):
        noticia = Noticias.mostrarNoticias_por_id(id)
        if noticia:
            noticia.deletarNoticia()
        else:
            print(f"Notícia com ID {id} não encontrado.")

class ListarNoticias:
    @staticmethod
    def listar_noticias():
        noticias = Noticias.mostrarNoticias()
        for noticia in noticias:
            print(noticia)

class BuscarNoticia:
    @staticmethod
    def buscar_noticia_por_id(id):
        noticia = Noticias.mostrarNoticias_por_id(id)
        print(noticia)

    @staticmethod
    def buscar_noticia_por_titulo(titulo):
        noticia = Noticias.mostrarNoticias_por_Tiulo(titulo)
        print(noticia)