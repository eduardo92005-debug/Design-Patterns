from .interfaces import IHability

class UsingArch(IHability):

    def __init__(self, level):
        self.__level = level
    def comportamental(self):
        print("Action: You attacked with arrows ")
    def level_attr(self):
        print("Level of using arch: %d" % self.__level)
