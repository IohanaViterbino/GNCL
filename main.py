from view.funcionarioView import FuncionarioView

if __name__=='__main__':
    try:
        fun=FuncionarioView.loginF()
        if fun:
            FuncionarioView.menuView(fun)
    except IndexError:
        print("Login ou Senha inválido")
