from pydantic import BaseModel, validator
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    """name=name,
    age=age,
    ht=ht,
    hd=hd,
    glucose=glucose,
    bmi=bmi,
    outcome=outcome"""
    name: str #= "Carlos"
    age: int #= 50
    ht: int #= 1
    hd: int #= 1
    glucose: float #= 33.6
    bmi: float #= 23

    @validator('age', 'ht', 'hd', pre=True)
    def validate_integers(cls, v):
        # Converte string para inteiro, se necessário
        if isinstance(v, str):
            try:
                return int(v)
            except ValueError:
                raise ValueError(f"Invalid integer value: {v}")
        return v

    @validator('glucose', 'bmi', pre=True)
    def validate_floats(cls, v):
        # Converte string para float, se necessário
        if isinstance(v, str):
            try:
                return float(v)
            except ValueError:
                raise ValueError(f"Invalid float value: {v}")
        return v


    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Carlos"
    age: int = 50
    ht: int = 1
    hd: int = 1
    glucose: float = 33.6
    bmi: float = 23
    outcome: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Carlos"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Carlos"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "ht": paciente.ht,
        "hd": paciente.hd,
        "glucose": paciente.glucose,
        "bmi": paciente.bmi,
        "outcome": paciente.outcome
    }
    
# Apresenta uma lista de pacientes
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
        "ht": paciente.ht,
        "hd": paciente.hd,
       "glucose": paciente.glucose,
        "bmi": paciente.bmi,
        "outcome": paciente.outcome
        })

    return {"pacientes": result}

