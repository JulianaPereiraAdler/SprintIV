from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = 'Name', 'Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'Diagnostic'

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    age = Column("Age", Integer)
    sex = Column("Sex", Integer)
    chest_pain_type = Column("ChestPainType", Integer)
    resting_BP = Column("RestingBP", Integer)
    cholesterol = Column("Cholesterol", Integer)
    fasting_BS = Column("FastingBS", Integer)
    resting_ECG = Column("RestingECG", Integer)
    max_HR = Column("MaxHR", Integer)
    exercise_Angina = Column("ExerciseAngina", Integer)
    oldpeak = Column("Oldpeak", Float)
    st_Slope = Column("ST_Slope", Integer)
    outcome = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:int, age:int, sex:int, chest_pain_type:int, resting_BP:int,
                 cholesterol:int, fasting_BS:int, resting_ECG:int, max_HR:int,
                 exercise_Angina:int, oldpeak:float, st_Slope:int, outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Dados:
            name: nome do paciente
            age: idade do paciente em anos.
            sex: sexo do paciente [Masculino = 1, Feminino=0]
            chest_pain_type: tipo de Dor no Peito inclui Angina Típica (TA = 3), Angina Atípica (ATA = 1), Dor Não Anginal (NAP = 2) e Assintomático (ASY = 0)
            resting_BP: pressão Arterial em Repouso: Medida em mm Hg
            cholesterol: colesterol, medido em mm/dl.
            fasting_BS: glicemia em jejum, indica diabetes se > 120 mg/dl.
            resting_ECG: ECG em Repouso, inclui normal (1), anormalidades de onda ST-T (2), e hipertrofia ventricular esquerda (0).
            max_HR: Frequência Cardíaca Máxima: Valor numérico entre 60 e 202.
            exercise_Angina: Angina Induzida por Exercício, indica a presença ou ausência de angina.
            oldpeak: Depressão de ST induzida por exercício em relação ao repouso, medida em milímetros.
            st_Slope: classificado como ascendente (2), plano (1) ou descendente (2).
            outcome: diagnóstico
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name=name
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_BP = resting_BP
        self.cholesterol = cholesterol
        self.fasting_BS = fasting_BS
        self.resting_ECG = resting_ECG
        self.max_HR = max_HR
        self.exercise_Angina = exercise_Angina
        self.oldpeak = oldpeak
        self.st_Slope = st_Slope
        self.outcome = outcome

        if data_insercao:
            self.data_insercao = data_insercao