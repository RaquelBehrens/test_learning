class Funcionario:
    def __init__(self, nome:str, cpf:str, cargo:str, salario:float):
        self.__nome = nome
        self.__cpf = cpf
        self.__cargo = cargo
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cargo(self):
        return self.__cargo

    @property
    def salario(self):
        return self.__salario