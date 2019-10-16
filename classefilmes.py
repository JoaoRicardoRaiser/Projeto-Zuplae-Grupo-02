class Filmes:
    def __init__(self):
        self.__id = 0
        self.__titulo  = ''
        self.__ano = 0
        self.__valor = 0
   

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self,ano):
        self.__ano = ano

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self,valor):
        self.__valor = valor

  