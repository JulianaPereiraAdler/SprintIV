import numpy as np
import pickle

class Model:
    
    def carrega_modelo(path):
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([form.age,
                            form.sex,
                            form.chest_pain_type,
                            form.resting_BP,
                            form.cholesterol,
                            form.fasting_BS,
                            form.resting_ECG,
                            form.max_HR,
                            form.exercise_Angina,
                            form.oldpeak,
                            form.st_Slope
                            ])
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])

       