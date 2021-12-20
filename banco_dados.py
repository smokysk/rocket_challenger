from funcionario import Funcionario


class BancoDados:
    def __init__(self):
        self.registros = list()

    def salvar_arquivo(self, funcionarios):
        with open('banco_dados.txt', 'a') as arq:
            arq.writelines(funcionarios)

    def listar_arquivo(self):
        with open("banco_dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha)

