import networkx as nx
from matrix.decision_tree import DecisionTree


def main():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1,2)
    dt = DecisionTree(g)

    dt.evaluate()

    dt = DecisionTree(create_decision_tree())



def create_decision_tree():
    g = nx.DiGraph()
    g.add_node("root", func="eval_root")
    return g


if __name__ == "__main__":
    main()
