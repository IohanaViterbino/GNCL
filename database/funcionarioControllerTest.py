from controller.funcionarioController import CadastrarFuncionario, ExcluirFuncionario, AtualizarFuncionario, ListarFuncionario, BuscarFuncionario, LoginFuncionario

if __name__ == '__main__':
    print('====Adicionar====')
    CadastrarFuncionario.cadastrar_funcionario("a", "b", "c", "d") #FEITO
    ListarFuncionario.listar_funcionarios() #FEITO
    
    if LoginFuncionario.login("c", "d", 1) == True:
        BuscarFuncionario.buscar_funcionario_por_id(1) #FEITO
        AtualizarFuncionario.alterar_dados_funcionario(1, "nome1", "cpf1", "login1", "senha1") #FEITO
        ListarFuncionario.listar_funcionarios() #FEITO
        # ExcluirFuncionario.excluir_funcionario(1) #FEITO
        # ListarFuncionario.listar_funcionarios() #FEITO
    



