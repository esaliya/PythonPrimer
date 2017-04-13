# coding: utf-8
import networkx as nx
G = nx.read_edgelist('/Users/esaliya/sali/projects/DARPA-NGS2/intersim/nim.11.1.1.is.run/original-files/n.1000.k.10.v.01.edges')
len(G)
G.number_of_edges()
for node, data in G.nodes(data=True):
    data['color'] = node
    
G.nodes(data=True)
nx.write_gml(G, '/Users/esaliya/sali/projects/DARPA-NGS2/intersim/nim.11.1.1.is.run/original-files/n.1000.k.10.v.01.gml')
