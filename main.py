import networkx as nx
import matplotlib.pyplot as plt

def get_dependencies():
    """Read all dependencies and subdependencies from a file and put them into a list

    Returns:
        list: List of dependencies and their respective subdependencies
    """
    dependencies = []
    current_dep = None
    
    with open('dependencies.txt', 'r', encoding='UTF-16') as file:
        for line in file:
            if '==' in line:
                dep = line.split('==')[0].strip()
                current_dep = [dep, []]
                dependencies.append(current_dep)
            else:
                if current_dep is not None:
                    dep = line.split('[')[0].strip()
                    current_dep[1].append(dep[2:])
                else:
                    print(f"Warning: found sub-dependency before any main dependency — line was: {line.strip()}")

    dependencies.sort(key=lambda x: len(x[1]), reverse=True)
    
    return dependencies

def gen_graph(theme="light"):
    """Generates the dependency graph with respective subdependencies

    Args:
        theme (str, optional): Light and dark theme. Defaults to "light".
    """

    deps = get_dependencies()                                           # Grab dependencies
    
    dg = nx.star_graph(0)                                               # Set graph to star graph with 0 nodes

    if theme == "dark":
        plt.figure(figsize=(9, 9), facecolor='black')
    else:
        plt.figure(figsize=(9, 9), facecolor='white')

    for dep in deps:                                                    # Cycle through dependencies and subdependencies to create graph
        dep_name = dep[0]
        dg.add_node(dep_name)
        subdeps = dep[1]
        for subdep in subdeps:
            dg.add_node(subdep)
            dg.add_edge(dep_name, subdep)

    dep_size_map = {dep[0]: len(dep[1]) * 150 for dep in deps}          # Define node size based on how many subdependencies a dependency has
    nodesize = [dep_size_map.get(node, 300) for node in dg.nodes()]

    color_pairs = [
        ('#1f77b4', '#aec7e8'),
        ('#ff7f0e', '#ffbb78'),
        ('#2ca02c', '#98df8a'),
        ('#d62728', '#ff9896'),
        ('#9467bd', '#c5b0d5'),
        ('#8c564b', '#c49c94'),
    ]

    main_deps = [dep[0] for dep in deps]
    main_color_map = {name: color_pairs[i % len(color_pairs)] for i, name in enumerate(main_deps)}      # Define colors for different dependencies and subdependencies

    node_colors = []
    for node in dg.nodes():
        if node in main_color_map:
            node_colors.append(main_color_map[node][0])
        else:
            for dep_name, subdeps in deps:
                if node in subdeps:
                    node_colors.append(main_color_map[dep_name][1])
                    break
            else:
                node_colors.append("#cccccc")
    
    edge_colors = []
    for u, v, in dg.edges():
        color = main_color_map.get(u, ("#ffb0f1",))[0]                 # Set edge color to node color unless shared between dependencies
        edge_colors.append(color)

    pos = nx.kamada_kawai_layout(dg)    
    pos["networkx"] += (0.50, -0.10)                                     # Move 'networkx' to the side because it has no subdependencies
    pos[0] = (float('inf'), float('inf'))
    
    if theme == "dark":
        nx.draw_networkx_nodes(dg, pos, node_size=nodesize, node_color=node_colors, alpha=0.9)
        nx.draw_networkx_edges(dg, pos, arrows=True, edge_color="white", arrowstyle='-', width=1.0, alpha=0.5)
        nx.draw_networkx_edges(dg, pos, width=5, alpha=0.5, edge_color=edge_colors)
        nx.draw_networkx_labels(dg, pos, font_color="whitesmoke")
    else:
        nx.draw_networkx_nodes(dg, pos, node_size=nodesize, node_color=node_colors, alpha=0.9)
        nx.draw_networkx_edges(dg, pos, arrows=True, edge_color="black", arrowstyle='-', width=1.0, alpha=0.5)
        nx.draw_networkx_edges(dg, pos, width=5, alpha=0.5, edge_color=edge_colors)
        nx.draw_networkx_labels(dg, pos, font_color="black")

    plt.style.use('dark_background')
    plt.tight_layout()
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    gen_graph("dark")
