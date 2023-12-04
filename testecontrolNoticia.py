from controller.noticiaController import AtualizarNoticia, ExcluirNotícia, CadastrarNoticia, ListarNoticias, BuscarNoticia

if __name__=='__main__':
    CadastrarNoticia.cadastrar_noticia("o q somos", "contest", "somo somos", "blávlal", "saúde", 1)
    ListarNoticias.listar_noticias()
    BuscarNoticia.buscar_noticia_por_id(1)
    AtualizarNoticia.alterar_dados_noticia(1, "a", "b", "c", "d", "e", 1)
    BuscarNoticia.buscar_noticia_por_id(1)
    ExcluirNotícia.excluir_noticia(1)
    ListarNoticias.listar_noticias()

