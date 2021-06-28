from .interfaces import IHability

class UsingSword(IHability):

    def __init__(self, level):
        self.__level = level
    def comportamental(self):
        print("Action: You attacked with sword ")
    def level_attr(self):
        print("Level of using sword: %d" % self.__level)
