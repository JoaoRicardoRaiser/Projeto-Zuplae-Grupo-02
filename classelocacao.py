class Locacao:
    def __init__(self):
        self.__nome = ''
        self.__id = 0
        self.__valor = 0
        self.__id_cliente = 0
        self.__id_filme = 0
        self.__data_locacao = 0

@property
def nome(self):
    return self.__nome

@nome.setter
def id(self,nome):
    self.__nome = nome


@property
def valor(self):
    return self.__valor

@valor.setter
def valor(self,valor):
    self.__valor = valor




    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    @property
    def id_filme(self):
        return self.__id_filme

    @id_filme.setter
    def id_filme(self, id_filme):
        self.__id_filme = id_filme


    @property
    def data_locacao(self):
        return self.__data_locacao

    @data_locacao.setter
    def data_locacao(self,data_locacao):
        self.__data_locacao = data_locacao

# class  Locacao:
#     def __init__(self, id, idcliente, idfilme, datalocacao):
#         self.id = id
#         self.idcliente = idcliente
#         self.idfilme = idfilme
#         self.datalocacao = datalocacao
