from weighted_graph import *

class Graphed_Lights_out:
    def __init__(self,graph):
        self.graph = graph
    def get_edges_removed(self, graph, get_whether_remove):
        edges_removed = [[edge for edge in edges if not get_whether_remove(edge)] for edges in graph.edges]
        return Weighted_graph(graph.n,edges_removed)
    def try_solve(self): #Returns onehot list that represents which nodes to be pressed, or None if it isn't solvable
        graph_still_removed = self.get_edges_removed(self.graph, lambda edge:edge.weight==0)
        graph_vibrating_removed = self.get_edges_removed(self.graph, lambda edge:edge.weight==1)

        components = graph_still_removed.components
        component_ids = [-1 for i in range(self.graph.n+1)]
        component_cnt=1
        for component in components:
            for node in component:
                component_ids[node]=component_cnt
        
                for j in range(node+1, len(component)):
                    edges_linking_ij = [edge for edge in graph_vibrating_removed.edges[node] if edge.linked_node==j]
                    if len(edges_linking_ij):
                        return None
            component_cnt+=1

        merged_edges = [[] for i in range(component_cnt+1)]
        for component in components:
            for node in component:
                merged_edges[component_ids[node]]+=[Weighted_edge(component_ids[edge.linked_node],0) for edge in graph_vibrating_removed.edges[node]]
        
        merged_graph = Weighted_graph(component_cnt,merged_edges)
        self.should_press_merged = [-1 for i in range(component_cnt+1)]
        traversal=Weighted_graph_traversal(merged_graph)
        traversal.on_seek = lambda node, edge, graph, visited: self.try_paint(node,edge.linked_node)

        for cid in range(1, merged_graph.n+1):
            if traversal.visited[cid]:
                continue
            self.should_press_merged[cid]=1
            success = traversal.dfs_from(cid)
            if not success:
                return None
        
        res=[]
        for i in range(1, self.graph.n+1):
            res.append(self.should_press_merged[component_ids[i]])

        #select minimum-press answer
        selections = [i for i in res if i==1]
        if len(selections)>len(res)/2:
            res=[1-i for i in res]

        return res
    
    def try_paint(self,current_node, linked_node):
        if self.should_press_merged[linked_node]==self.should_press_merged[current_node]:
            return False
        self.should_press_merged[linked_node] = 1 - self.should_press_merged[current_node]
        return True
