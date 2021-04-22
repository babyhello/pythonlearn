import graphviz

g1 = graphviz.Digraph(format='svg')

g1.node('a')
g1.node('b')
g1.node('c')
g1.edge('a', 'b')
g1.edge('b', 'a')
g1.edge('c', 'b')
g1.edge('c', 'b')
g1.edge('c', 'b')
g1.edge('a','a')
g1.edge('c','c')
g1.edge('c','c')
g1.edge('c','c')
g1.render('graph/lab57')