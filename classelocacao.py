class Locacao:
    def __init__(self):
        self.__id = 0
        self.__id_cliente = 0
        self.__id_filmes = 0
        self.__id_valor = 0
        self.__data_locacao = 0

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
    def id_cliente(self,id_cliente):
        self.__id_cliente = id_cliente

    @property
    def id_filmes(self):
        return self.__id_filmes
    @id_filmes.setter
    def __id_filmes(self,id_filmes):
        self.__id_filmes = id_filmes

    @property
    def id_valor(self):
        return self.__id_valor
    @id_valor.setter
    def id_valor(self,id_valor):
        self.__id_valor = id_valor

    @property
    def data_locacao(self):
        return self.__data_locacao
    @data_locacao.setter
    def data_locacao(self,data_locacao):
        self.__data_locacao = data_locacao