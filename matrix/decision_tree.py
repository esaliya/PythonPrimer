import networkx as nx


class DecisionTree:
    def __init__(self, g):
        """
        Initialize the decision tree
        :type g: networkx.DiGraph
        :return: a matrix.DecisionTree object
        """
        self.g = g

    def evaluate(self):
        """
        Evaluates the tree
        :return:
        """
        self.__find_root()

    def __find_root(self):
        print(self.g.size())

