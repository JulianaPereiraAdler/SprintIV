from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/HeartFailurePredictionDataset_golden.csv"
colunas = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    ml_path = 'ml_model/model.pkl'
    modelo_knn = Model.carrega_modelo(ml_path)
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X, Y)
    
    assert acuracia_knn >= 0.70
    assert recall_knn >= 0.5 
    assert precisao_knn >= 0.5 
    assert f1_knn >= 0.5 
    