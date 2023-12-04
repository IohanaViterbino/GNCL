from controller.noticiaController import AtualizarNoticia, ExcluirNotícia, CadastrarNoticia, ListarNoticias

if __name__=='__main__':
    CadastrarNoticia.cadastrar_noticia("o q somos", "contest", "somo somos", "blávlal", "saúde", 1)

    ListarNoticias.listar_noticias()