import networkx as nx
import matplotlib.pyplot as plt
import task4
import matplotlib.colors as mcolors

    


def treeTraversal(tree_root:task4.Node,method="DFS"):
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = task4.add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}# Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.draw()
    plt.pause(0.5)

    sq=[tree_root]

    cmap=plt.get_cmap("Reds")
    i=0
    while sq:
        plt.pause(1)
        if method=="DFS":
            cur_node=sq.pop()
        else:
            cur_node=sq.pop(0)
        
        tree.nodes[cur_node.id]["color"]=cmap(1-i/len(tree))
        i+=1
         
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.draw()

        if cur_node.left!=None:
            sq.append(cur_node.left)
        if cur_node.right!=None:
            sq.append(cur_node.right)

    plt.show()            


treeTraversal(task4.root,0)
treeTraversal(task4.root)