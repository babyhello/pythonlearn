import graphviz as gv
import functools
import itertools

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g4 = digraph()


def add_nodes(g, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            g.node(n[0], **n[1])
        else:
            g.node(n)
    return g


def add_edges(g, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            g.edge(*e[0], **e[1])
        else:
            g.edge(*e)
    return g


teams = ['taipei', 'hsinchu', 'taichung', 'kaohsiung', 'account']
# races = tuple(itertools.combinations(teams, 2))
races = tuple(itertools.permutations(teams, 2))

g3 = add_nodes(g3, teams)
g3 = add_edges(g3, races)
g3.render("graph/lab59_g3")

node1 = ('A', {'label': 'ASUS'})
node2 = ('B', {'label': "ACER"})
node3 = ('C', {'label': '宏達電'})
node4 = ('D', {})
g4_nodes = [node1, node2, node3, node4]
g4 = add_nodes(g4, g4_nodes)

edge1 = (('A', 'B'), {'label': '筆電龍頭'})
edge2 = (('A', 'C'), {'label': '前後股王'})
edge3 = (('A', 'C'), {'label': '都在新店'})
edge4 = (('B', 'D'), {})
g4_edges = [edge1, edge2, edge3, edge4]
g4 = add_edges(g4, g4_edges)
g4.render("graph/lab59_g4")


def apply_styles(g, s):
    g.graph_attr.update(('graph' in s and s['graph']) or {})
    g.node_attr.update(('nodes' in s and s['nodes']) or {})
    g.edge_attr.update(('edges' in s and s['edges']) or {})
    return g


styles = {'graph': {'label': '台灣家電',
                    'fontsize': '24',
                    'fontcolor': '#224488',
                    'bgcolor': '#C0FFEE',
                    'rankdir': 'LR',
                    'fillcolor': '#FFC0EE'},
          'nodes': {'fontname': 'Consolas',
                    'shape': 'box',
                    'fontcolor': 'green',
                    'color': 'black',
                    'style': 'filled',
                    'fillcolor': '#FFC0EE'},
          'edges': {'style': 'dotted',
                    'color': '#002299',
                    'arrowhead': 'open',
                    'fontname': 'Courier',
                    'fontsize': '24',
                    'fontcolor': '#440088'}}
g5 = apply_styles(g4, styles)
g5.render("graph/lab59_g5")