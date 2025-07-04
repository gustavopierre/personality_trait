from sklearn.metrics import accuracy_score

class Avaliador:
    
    def __init__(self):
        """Inicializa o avaliador"""
        pass

    def avaliar(self, pipeline, X_test, y_test):
        """ Faz uma predição e avalia o pipeline que utiliza o modelo"""
        predicoes = pipeline.predict(X_test)
        
        return accuracy_score(y_test, predicoes)
