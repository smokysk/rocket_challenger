from funcionario import Funcionario
from banco_dados import BancoDados

class Aplicacao:
    def exibir_menu(self):
        soma_m = 0
        soma_f = 0
        while True:
            print("digite uma op abaixo")
            print("1-cadastrar: ")
            print("2-listar dados: ")
            print("3-saldo mulheres: ")
            print("4-saldo homens: ")
            print("0 - sair: ")
            op = int(input("digite uma opçao acima: "))
            db = BancoDados()
            func = Funcionario()
            funcionarios = []
            if op == 1:
                func.nome = input("digite seu nome: ")
                func.salario = float(input("Digite seu salario: "))
                func.sexo = input("digite seu sexo ")
                funcionarios.append(str({func.nome, func.salario, func.sexo})+'\n')
                db.salvar_arquivo(funcionarios)
                if func.sexo == 'M':
                    soma_m += func.salario
                else:
                    soma_f += func.salario
            elif op == 2:
                db.listar_arquivo()
            elif op == 3:
                print(soma_f)
            elif op == 4:
                print(soma_m)
            elif op == 0:
                break


ap = Aplicacao()
ap.exibir_menu()
