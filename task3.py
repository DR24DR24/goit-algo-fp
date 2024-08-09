import task3_graph
#import math
import heapq

class Node:
    def __init__(self,node,previous_node="None",distance=float("inf")):
        self.distance=distance
        self.previous_node=previous_node
        self.node=node

    def __lt__(self, node:"Node"):
        return self.distance<node.distance    



def dijkstra(graph, start):
    nodes_table={node:Node(node) for node in graph.nodes()}
    nodes_table[start].previous_node=start
    nodes_table[start].distance=0
    heapq_nodes=[nodes_table[start]]
    #nodes_table[start][0]=0
    while heapq_nodes:
        current=heapq.heappop(heapq_nodes)

        for neighbour in graph[current.node]:
            new_weight=nodes_table[current.node].distance+\
                graph.get_edge_data(neighbour,current.node)["time"]
            if nodes_table[neighbour].distance>new_weight:
                nodes_table[neighbour].distance=new_weight
                nodes_table[neighbour].previous_node=current
                heapq.heappush(heapq_nodes,nodes_table[neighbour])
                
                    
    return nodes_table

#table = dijkstra(task1.G, "A")
nodes_list=list(task3_graph.G.nodes())
dinstance_table=[]
for i,k in enumerate(nodes_list):
    table = dijkstra(task3_graph.G, k)
    dinstance_table.append([])
    for j,l in enumerate(nodes_list):
        dinstance_table[i].append(table[l].distance)

print(" ",nodes_list)
for i,k in enumerate(nodes_list):
    print(k,dinstance_table[i])

