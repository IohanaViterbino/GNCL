
from model.noticiaModelo import Noticias
from datetime import datetime

class CadastrarNoticia:
    @staticmethod
    def cadastrar_noticia(titulo, autor, legenda, texto, categoria, idFuncionario):
        noticia = Noticias(titulo, autor, legenda, datetime.now(), texto, categoria, idFuncionario)
        noticia.criarNoticia()

class AtualizarNoticia:
    @staticmethod
    def alterar_dados_noticia(id, titulo, autor, texto, legenda, categoria, idFuncionario):
        noticia = Noticias.mostrarNoticias_por_id(id)
        if noticia:
            noticia.setAutor(autor)
            noticia.setTitulo(titulo)
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
            print(Noticias)

class BuscarFuncionario:
    @staticmethod
    def buscar_noticia_por_id(id):
        noticia = Noticias.mostrarNoticias_por_id(id)
        if noticia:
            print(noticia)
        else:
            print(f"Notícia com ID {id} não encontrado.")