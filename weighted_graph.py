import copy
class Weighted_edge:
    def __init__(self, linked_node, weight):
        self.linked_node = linked_node
        self.weight = weight

class Weighted_graph_traversal:
    def __init__(self, graph):
        self.graph=graph
        self.visited=[False for i in range(graph.n+1)]
        self.on_visited = lambda node, graph, visited: True #called when visted node, returns success
        self.on_seek = lambda node, edge, graph, visited: True #called when seeking linked nodes, returns success
    def set_activity(self,on_visited,on_seek):
        self.on_visited = on_visited
        self.on_seek = on_seek
    def dfs(self):
        self.reset_visited()
        for i in range(1,self.graph.n+1):
            if self.visited[i]:
                continue
            self.dfs_from(i)
    def dfs_from(self, node): #Returns success
        self.visited[node]=True
        if not self.on_visited(node,self.graph,self.visited):
            return False

        for edge in self.graph.edges[node]:
            if not self.on_seek(node, edge,self.graph,self.visited):
                return False
            linked_node=edge.linked_node
            if not self.visited[linked_node]:
                if not self.dfs_from(linked_node):
                    return False
        return True
    def reset_visited(self):
        self.visited=[False for i in range(self.graph.n+1)]

class Weighted_graph:
    def __init__(self,n, edges):
        self.n=n
        self.edges=edges
        self.components = []
        self.set_components()
    def set_components(self):
        traversal = Weighted_graph_traversal(self)
        component = []
        for node in range(1,self.n+1):
            if traversal.visited[node]:
                continue

            traversal.on_visited = lambda node, graph, visited: self.establish_node_to_component(node,component)
            traversal.dfs_from(node)
            self.components.append(copy.deepcopy(component))
            component=[]
            
    def establish_node_to_component(self,node,component):
        component.append(node)
        return True
