from controller.noticiaController import AtualizarNoticia, ExcluirNotícia, CadastrarNoticia, ListarNoticias, BuscarNoticia

class NoticiaView:
    def cadastroN(func):
        titulo=input("Insira o título da notícia: ")
        legenda=input("Insira a legenda da notícia: ")
        categoria=input("Insira a categoria da notícia: ")
        texto=input("Insira o texto da notícia: ")
        return CadastrarNoticia.cadastrar_noticia(titulo, func.getNome(), texto, legenda, categoria, func.getId())
    
    def listarTudoN():
        return ListarNoticias.listar_noticias()
    
    def buscarPorIdN():
        try:
            id=int(input("Insira o ID que procura: "))
            return BuscarNoticia.buscar_noticia_por_id(id)
        
        except IndexError:
            print("ID da notícia não encontrado.")

    def buscarPorTituloN():
        try:
            titulo=input("Insira o titulo que procura: ")
            return BuscarNoticia.buscar_noticia_por_titulo(titulo.lower())
        
        except IndexError:
            print("Título da notícia não encontrado. Escreva-o por completo.")
    
    def atualizarN(func):
        try:
            id=int(input("Insira o ID da notícia: "))
            titulo=input("Insira o novo título da notícia: ")
            legenda=input("Insira a nova legenda da notícia: ")
            categoria=input("Insira a nova categoria da notícia: ")
            texto=input("Insira o novo texto da notícia: ")
            return AtualizarNoticia.alterar_dados_noticia(id, titulo, func.getNome(), texto, legenda, categoria, func.getId())

        except IndexError:
            print("id da notícia não encontrado.")

    def excluirPorIdN():
        try:
            id= int(input("Insira o Id do usuário a ser removido: "))
            return ExcluirNotícia.excluir_noticia(id)

        except IndexError:
            print("id de usuário não encontrado.")

    def menuView(func):
        while True:
            try:
                print(f"\nBem vindo ao GNCL, {func.getNome()}!\nInsira a opção desejada:"
                    +"\n1- Cadastro de nova Notícia;"
                    +"\n2- Listar Notícias;"
                    +"\n3- Buscar Notícia por id;"
                    +"\n4- Buscar Notícia por título;"
                    +"\n5- Atualizar Notícia (precisa do id para concluir essa ação);"
                    +"\n6- Remover Notícia (precisa do id para concluir essa ação);")
                op=int(input())

                match(op):
                    case 1:
                        NoticiaView.cadastroN(func)

                    case 2:
                        NoticiaView.listarTudoN()

                    case 3:
                        NoticiaView.buscarPorIdN()

                    case 4:
                        NoticiaView.buscarPorTituloN()

                    case 5:
                        print("ATENÇÃO\nAS ALTERAÇÕES TEM QUE SER FEITAS EM TODAS AS INFORMAÇÕES,",
                            "CASO NÃO QUEIRA ALTERAR ALGO, INSIRA COMO ERA ANTES.")
                        NoticiaView.atualizarN(func)
                    case 6:
                        print("ATENÇÃO\nESSA AÇÃO É DE CARÁTER CRÍTICO!")
                        NoticiaView.excluirPorIdN()
                        
                    case _:
                        print("opção inválida. Insira uma válida")

            except ValueError:
                print("Digite uma opção NUMÉRICA válida")