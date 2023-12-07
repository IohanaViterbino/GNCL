from view.funcionarioView import FuncionarioView
from view.noticiaView import NoticiaView

if __name__=='__main__':
    try:
        fun=FuncionarioView.loginF()
        if fun:
            try:
                print(f"\nBem vindo ao GNCL, {fun.getNome()}!",
                    "\nDigte 1 para entar no gerenciamento de usuários;",
                    "\nDigte 2 para entar no gerenciamento de notícias;")
                op=int(input())
                match(op):
                    case 1:
                        FuncionarioView.menuView(fun)
                    case 2:
                        NoticiaView.menuView(fun)
                    case _:
                        print("Opção inexistente.")
                        
            except ValueError:
                print("Digite uma opção NUMÉRICA válida")

    except IndexError:
        print("Login ou Senha inválido")
    
