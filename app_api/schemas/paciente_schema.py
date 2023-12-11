from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "João"
    age: int = 40
    sex: int = 1
    chest_pain_type: int = 1
    resting_BP: int = 140
    cholesterol: int = 289
    fasting_BS: int = 0
    resting_ECG: int = 1
    max_HR: int = 132
    exercise_Angina: int = 1
    oldpeak: float = 0.0
    st_Slope: int = 2

class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "João"
    age: int = 40
    sex: int = 1
    chest_pain_type: int = 1
    resting_BP: int = 140
    cholesterol: int = 289
    fasting_BS: int = 0
    resting_ECG: int = 1
    max_HR: int = 132
    exercise_Angina: int = 1
    oldpeak: float = 0.0
    st_Slope: int = 2
    outcome: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "João"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "João"
    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex": paciente.sex,
        "chest_pain_type": paciente.chest_pain_type,
        "resting_BP": paciente.resting_BP,
        "cholesterol": paciente.cholesterol,
        "fasting_BS": paciente.fasting_BS,
        "resting_ECG": paciente.resting_ECG,
        "max_HR": paciente.max_HR,
        "exercise_Angina": paciente.exercise_Angina,
        "oldpeak": paciente.oldpeak,
        "st_Slope": paciente.st_Slope,
        "outcome": paciente.outcome
    }
    
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
          "id": paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "sex": paciente.sex,
            "chest_pain_type": paciente.chest_pain_type,
            "resting_BP": paciente.resting_BP,
            "cholesterol": paciente.cholesterol,
            "fasting_BS": paciente.fasting_BS,
            "resting_ECG": paciente.resting_ECG,
            "max_HR": paciente.max_HR,
            "exercise_Angina": paciente.exercise_Angina,
            "oldpeak": paciente.oldpeak,
            "st_Slope": paciente.st_Slope,
            "outcome": paciente.outcome
        })

    return {"pacientes": result}