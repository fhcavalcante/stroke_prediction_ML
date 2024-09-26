from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    age = Column("age", Integer)
    ht = Column("ht", Integer)
    hd = Column("hd", Integer)
    glucose = Column("glucose", Float)
    bmi = Column("bmi", Integer)
    outcome = Column("outcome", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, age:int, ht:int, name:str,
                 hd:int, glucose:int, outcome:int, bmi:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
        name: nome do paciente
            age: idade
            ht: historico de hipertensao
            hd: historico de doenças do coração
            glucose: 
            bmi: índice de massa corporal
            outcome: diagnóstico
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name=name
        self.age=age
        self.ht = ht
        self.hd = hd
        self.glucose = glucose
        self.bmi = bmi
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao