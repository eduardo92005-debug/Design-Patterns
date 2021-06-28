from abc import ABC, abstractclassmethod

class IHability(ABC):
    
    @abstractclassmethod
    def comportamental(self):
        pass
    @abstractclassmethod
    def level_attr(self):
        pass