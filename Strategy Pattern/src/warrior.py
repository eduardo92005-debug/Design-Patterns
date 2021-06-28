from typing import Type
from .hability import IHability

#Bib Type muito importante para explicitar tipagem de dados
class Warrior:
   def __init__(self, hability: Type[IHability]):
      self.hability = hability
   #Implementa comportamento e atributos atraves da interface IHability
   def action(self):
      self.hability.comportamental()
   def attributes(self):
      self.hability.level_attr()
   
