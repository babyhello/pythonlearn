import graphviz
import itertools

g1 = graphviz.Digraph(format='svg')

teams = ['taipei', 'hsinchu', 'taichung', 'kaohsiung', 'account']
#races = tuple(itertools.combinations(teams, 2))
races = tuple(itertools.permutations(teams, 2))

for t in teams:
    g1.node(t)

for edges in races:
    # g1.edge(edges[0], edges[1])
    g1.edge(*edges)

g1.render('graph/lab58')