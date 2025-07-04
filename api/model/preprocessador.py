from sklearn.model_selection import train_test_split
import pickle
import numpy as np

from schemas.personality_trait_schema import PersonalityInputSchema

class PreProcessador:

    def __init__(self):
        """Inicializa o preprocessador"""
        pass

    def separa_teste_treino(self, dataset, percentual_test, seed=3):
        # divisão em treino e teste
        X_train, X_test, y_train, y_test = self.__preparar_holdout(dataset, 
                                                                   percentual_test, 
                                                                   seed)
        
        return (X_train, X_test, y_train, y_test)
    
    def __preparar_holdout(self, dataset, percentual_test, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        dados = dataset.values
        X = dados[:, 0:7]
        y = dados[:, 7]

        return train_test_split(X, y, test_size=percentual_test, shuffle=True, 
                                random_state=seed)
    
    def preparar_body(self, body:PersonalityInputSchema):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([
            body.timeSpentAlone, 
            body.stageFear, 
            body.socialEventAttendance, 
            body.goingOutside, 
            body.drainedAfterSocializing, 
            body.friendsCircleSize, 
            body.postFrequency
        ]).reshape(1, -1)

        return X_input
