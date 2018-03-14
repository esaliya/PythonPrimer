import yaml
import networkx as nx
from networkx import Graph

# G = nx.path_graph(4)
# # nx.write_gml(G, 'data/graphs/simpl_graph.gml')
# # nx.write_graphml(G, 'data/graphs/simpl_graph.graphml')
# # nx.write_yaml(G, 'data/graphs/simple_graph.yaml')
# H = nx.read_yaml('data/graphs/simple_graph.yaml')  # type: Graph
#
#
# print(H.degree)
# print(G.degree)
#
#
# G = nx.Graph()
# G.add_node(1)


def main():
    g = nx.read_yaml('data/simple_yaml.yaml')
    print(g['adj'])


if __name__ == "__main__":
    main()



