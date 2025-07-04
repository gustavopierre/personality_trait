from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
avaliador = Avaliador()
pipeline = Pipeline()

# Parâmetros    
path_data = "./machinelearning/data/data.csv"

# Carga dos dados
dataset = carregador.carregar_dados(path_data)
array = dataset.values
X = array[:,0:7]
y = array[:,7]

# Método para testar o modelo de Extra Trees a partir do arquivo correspondente
def test_modelo_et():  
    # Importando o modelo de extra trees
    et_path = './machinelearning/models/et_personality_trait_pipeline.pkl'
    modelo_et = pipeline.carrega_pipeline(et_path)

    # Obtendo as métricas da Extra Trees
    acuracia_et = avaliador.avaliar(modelo_et, X, y)
    print(f"\nAcurácia do modelo Extra Trees: {acuracia_et:f}")
    # Testando as métricas da Extra Trees
    assert acuracia_et >= 0.98 


# Método para testar o modelo de Gradient Boosting a partir do arquivo correspondente
def test_modelo_gb():  
    # Importando o modelo de gradient boosting
    gb_path = './machinelearning/models/gb_personality_trait_pipeline.pkl'
    modelo_gb = pipeline.carrega_pipeline(gb_path)

    # Obtendo as métricas do Gradient Boosting
    acuracia_gb = avaliador.avaliar(modelo_gb, X, y)
    print(f"\nAcurácia do modelo Gradient Boosting: {acuracia_gb:f}")
    # Testando as métricas do Gradient Boosting
    assert acuracia_gb >= 0.98

# Método para testar o modelo de Bagging a partir do arquivo correspondente
def test_modelo_bagging():
    # Importando o modelo de bagging
    bagging_path = './machinelearning/models/bagging_personality_trait_pipeline.pkl'
    modelo_bagging = pipeline.carrega_pipeline(bagging_path)

    # Obtendo as métricas do Bagging
    acuracia_bagging = avaliador.avaliar(modelo_bagging, X, y)
    print(f"\nAcurácia do modelo Bagging: {acuracia_bagging:f}")
    # Testando as métricas do Bagging
    assert acuracia_bagging >= 0.98

# Método para testar o modelo de Random Forest a partir do arquivo correspondente
def test_modelo_rf():
    # Importando o modelo de random forest
    rf_path = './machinelearning/models/rf_personality_trait_pipeline.pkl'
    modelo_rf = pipeline.carrega_pipeline(rf_path)

    # Obtendo as métricas do Random Forest
    acuracia_rf = avaliador.avaliar(modelo_rf, X, y)
    print(f"\nAcurácia do modelo Random Forest: {acuracia_rf:f}")
    # Testando as métricas do Random Forest
    assert acuracia_rf >= 0.98
