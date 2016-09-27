import networkx as nx
import pprint

from utils.prints import log_print, print_graph_csv
from utils.progress_bar import ProgressBar


def power_set(seq):
    """
    Returns all the subsets of this set of nodes. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in power_set(seq[1:]):
            yield [seq[0]] + item
            yield item


def clear_seen(graph):
    """
    Assign a new property / refresh the one already present on all edges. This property is used to iterate on the graph
    :param graph:
    :return:
    """
    for node_a in graph.nodes():
        for node_b in graph.neighbors(node_a):
            graph.add_edge(node_a, node_b, seen=False)


def conductance(border_edges, internal_edges):
    """
    Calculate the conductance value of that sub-graph
    :param border_edges: edges that exit the given test case sub-graph
    :param internal_edges: edges of the given test case that remains inside the sub-graph
    :return: Conductance values if successful, else -1
    """
    if border_edges > 0 or internal_edges > 0:
        return border_edges / (2 * internal_edges + border_edges)
    else:
        return -1


def detect_conductance(graph, p_set):
    results = []
    prg_bar = ProgressBar(size=len(p_set), fraction=0.001)
    # Foreach power set let's check the conductance
    for potential_community in p_set:
        # we must count edges inside and inside.

        # internal and external are the edges that remain inside the comm or go outside
        internal = 0
        external = 0
        # foreach node inside the set, let's count if its edges go outside or inside the "community"
        for node in potential_community:
            neig = graph.neighbors(node)

            for nei in neig:
                if nei in potential_community and graph[node][nei]['seen'] == False:
                    internal += 1
                    graph[node][nei]['seen'] = True
                else:
                    external += 1
                    graph[node][nei]['seen'] = True

        cond = conductance(external, internal)
        results.append((cond, [potential_community, internal, external]))
        clear_seen(graph)

        prg_bar.update(1)
    return results


# ====================MAin
def calc_conductance():
    # g1 = nx.barbell_graph(5, 2)
    g1 = nx.gnp_random_graph(20, 0.35)
    log_print('Graph created')

    clear_seen(g1)
    log_print('Edges initialized')

    print_graph_csv(g1, 'Conductance gnpRandom')
    log_print('Graph saved to file')

    # Compute the power set of all nodes
    p_set = []

    for curr_set in power_set(g1.nodes()):
        p_set.append(curr_set)
    log_print('Power set computed')
    p_set.sort()
    log_print('Power set sorted')
    pp = pprint.PrettyPrinter(indent=4)

    # Test print of the power set
    pp.pprint(p_set)

    log_print('Starting community detection')
    results = detect_conductance(g1, p_set)
    log_print('Finished detection')
    results.sort(reverse=True)
    log_print('Finished sorting results')
    pp.pprint(results)

    print(g1.nodes())


def calc_modularity():
    # g1 = nx.barbell_graph(5, 2)
    g1 = nx.gnp_random_graph(20, 0.15)
    log_print(inp_str='Graph created')

    clear_seen(g1)
    log_print(inp_str='Edges initialized')

    print_graph_csv(g1, 'Modularity gnpRandom')
    log_print(inp_str='Graph saved to file')

    # generate a corresponding random graph
    log_print(inp_str='original degree', inp_obj=g1.degree())
    copy_degrees = g1.degree()
    # remove 0 vertex
    new_dict = dict()
    for vertex in copy_degrees:
        print(copy_degrees[vertex])
        if copy_degrees[vertex] != 0:
            new_dict[vertex] = copy_degrees[vertex]
    copy_degrees = new_dict
    log_print(inp_str='copy', inp_obj=copy_degrees)

    # Compute the power set of all nodes
    '''
    p_set = []

    for curr_set in power_set(g1.nodes()):
        p_set.append(curr_set)
    log_print('Power set computed')
    p_set.sort()
    log_print('Power set sorted')
    pp = pprint.PrettyPrinter(indent=4)

    # Test print of the power set
    pp.pprint(p_set)

    log_print('Starting community detection')
    results = detect_conductance(g1, p_set)
    log_print('Finished detection')
    results.sort(reverse=True)
    log_print('Finished sorting results')
    pp.pprint(results)

    print(g1.nodes())
    '''

# calc_conductance()
calc_modularity()