from funcionario import Funcionario

func = Funcionario()

func.nome = 'samuel'

with open('banco_dados.txt', 'a') as arq:
    arq.writelines(func.nome)
