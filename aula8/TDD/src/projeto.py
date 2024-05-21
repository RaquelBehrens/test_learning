from src.funcionario import Funcionario

class Projeto:
    def __init__(self, id: int, titulo: str, custo: float, prazo: str, gerente: Funcionario, equipe=[]):
        self.__id = id
        self.__titulo = titulo
        self.__custo = custo
        self.__prazo = prazo
        self.__gerente = gerente
        self.__equipe = equipe

    @property
    def id(self):
        return self.__id
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def prazo(self):
        return self.__prazo
    
    @property
    def gerente(self):
        return self.__gerente
    
    @property
    def equipe(self):
        return self.__equipe