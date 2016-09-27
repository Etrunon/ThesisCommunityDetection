from datetime import datetime


def print_graph_csv(graph, name):
    # Writes a file.
    time = datetime.now()
    out_file = open(name + " " + time.strftime('%d-%m-%Y %H:%M') + ".csv", "w")
    # out_file.write("This Text is going to out file\nLook at it and see\n")
    for node in graph.nodes():
        for neighbour in graph.neighbors(node):
            out_file.write(str(node)+';'+str(neighbour) + '\n')

    out_file.close()


def log_print(inp_str='', inp_obj=None):
    """
    Prints the given string with an initial label.
    :param inp_obj:
    :param inp_str:
    :return:
    """
    label = 'GraphOS: '
    try:
        print(label + inp_str + ' ' + inp_obj.__str__())
    except TypeError as e:
        try:
            print(label + inp_str + ' ' + str(inp_obj))
        except TypeError as e:
            print(label + e.__str__())

