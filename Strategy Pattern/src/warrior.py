from typing import Type
from .hability import IHability


class Warrior:
   def __init__(self, hability: Type[IHability]):
      self.hability = hability
   def action(self):
      self.hability.comportamental()
   def attributes(self):
      self.hability.level_attr()
   