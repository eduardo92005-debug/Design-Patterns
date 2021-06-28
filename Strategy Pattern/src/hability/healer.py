from .interfaces import IHability

class UsingHealer(IHability):

    def __init__(self, level):
        self.__level = level
    def comportamental(self):
        print("Action: You healed the target! ")
    def level_attr(self):
        print("Level of using heal: %d" % self.__level)
