from model.funcionarioModel import Funcionario

funcionario1 = Funcionario("Nome", "123.456.789-00", "usuario", "senha")
funcionario1.cadastrarFuncionario() #FEITO
#print(Funcionario.listarUsuarios()) #FEITO
#print(Funcionario.listarFuncionarioPorId(1)) #FEITO
#funcionario2 = Funcionario.listarFuncionarioPorId(2) #FEITO
#funcionario2.excluirFuncionario() #FEITO
print(Funcionario.listarUsuarios()) #FEITO

#funcionario2 = Funcionario.listarFuncionarioPorId(3) #FEITO
#funcionario2.setNome("João")
#funcionario2.setCpf("123")
#funcionario2.setLogin("a")
#funcionario2.setSenha("b")
#funcionario2.alterarFuncionario()
#print(Funcionario.listarFuncionarioPorId(3)) #FEITO


