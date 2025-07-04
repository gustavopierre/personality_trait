import pandas as pd

class Carregador:

    def __init__(self):
        """Inicializa o carregador"""
        pass

    def carregar_dados(self, url: str):
        """ Carrega e retorna um DataFrame """
        return pd.read_csv(url, delimiter=',')
    