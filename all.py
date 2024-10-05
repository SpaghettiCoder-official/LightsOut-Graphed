# import copy

# class Weighted_edge:
#     def __init__(self, linked_node, weight):
#         self.linked_node = linked_node
#         self.weight = weight

# class Weighted_graph_traversal:
#     def __init__(self, graph):
#         self.graph=graph
#         self.visited=[False for i in range(graph.n+1)]
#         self.on_visited = lambda node, graph, visited: True #called when visted node, returns success
#         self.on_seek = lambda node, edge, graph, visited: True #called when seeking linked nodes, returns success
#     def set_activity(self,on_visited,on_seek):
#         self.on_visited = on_visited
#         self.on_seek = on_seek
#     def dfs(self):
#         self.reset_visited()
#         for i in range(1,self.graph.n+1):
#             if self.visited[i]:
#                 continue
#             self.dfs_from(i)
#     def dfs_from(self, node): #Returns success
#         self.visited[node]=True
#         if not self.on_visited(node,self.graph,self.visited):
#             return False

#         for edge in self.graph.edges[node]:
#             if not self.on_seek(node, edge,self.graph,self.visited):
#                 return False
#             linked_node=edge.linked_node
#             if not self.visited[linked_node]:
#                 if not self.dfs_from(linked_node):
#                     return False
#         return True
#     def reset_visited(self):
#         self.visited=[False for i in range(self.graph.n+1)]

# class Weighted_graph:
#     def __init__(self,n, edges):
#         self.n=n
#         self.edges=edges
#         self.components = []
#         self.set_components()
#     def set_components(self):
#         traversal = Weighted_graph_traversal(self)
#         component = []
#         for node in range(1,self.n+1):
#             if traversal.visited[node]:
#                 continue

#             traversal.on_visited = lambda node, graph, visited: self.establish_node_to_component(node,component)
#             traversal.dfs_from(node)
#             self.components.append(copy.deepcopy(component))
#             component=[]
            
#     def establish_node_to_component(self,node,component):
#         component.append(node)
#         return True

# class Graphed_lights_out:
#     def __init__(self,graph):
#         self.graph = graph
#     def get_edges_removed(self, graph, get_whether_remove):
#         edges_removed = [[edge for edge in edges if not get_whether_remove(edge)] for edges in graph.edges]
#         return Weighted_graph(graph.n,edges_removed)
#     def try_solve(self): #Returns onehot list that represents which nodes to be pressed, or None if it isn't solvable
#         graph_still_removed = self.get_edges_removed(self.graph, lambda edge:edge.weight==0)
#         graph_vibrating_removed = self.get_edges_removed(self.graph, lambda edge:edge.weight==1)

#         components = graph_still_removed.components
#         component_ids = [-1 for i in range(self.graph.n+1)]
#         component_cnt=1
#         for component in components:
#             for node in component:
#                 component_ids[node]=component_cnt
        
#                 for j in range(node+1, len(component)):
#                     edges_linking_ij = [edge for edge in graph_vibrating_removed.edges[node] if edge.linked_node==j]
#                     if len(edges_linking_ij):
#                         return None
#             component_cnt+=1

#         merged_edges = [[] for i in range(component_cnt+1)]
#         for component in components:
#             for node in component:
#                 merged_edges[component_ids[node]]+=[Weighted_edge(component_ids[edge.linked_node],0) for edge in graph_vibrating_removed.edges[node]]
        
#         merged_graph = Weighted_graph(component_cnt,merged_edges)
#         self.should_press_merged = [-1 for i in range(component_cnt+1)]
#         traversal=Weighted_graph_traversal(merged_graph)
#         traversal.on_seek = lambda node, edge, graph, visited: self.try_paint(node,edge.linked_node)

#         for cid in range(1, merged_graph.n+1):
#             if traversal.visited[cid]:
#                 continue
#             self.should_press_merged[cid]=1
#             success = traversal.dfs_from(cid)
#             if not success:
#                 return None
        
#         res=[]
#         for i in range(1, self.graph.n+1):
#             res.append(self.should_press_merged[component_ids[i]])

#         #select minimum-press answer
#         selections = [i for i in res if i==1]
#         if len(selections)>len(res)/2:
#             res=[1-i for i in res]

#         return res
    
#     def try_paint(self,current_node, linked_node):
#         if self.should_press_merged[linked_node]==self.should_press_merged[current_node]:
#             return False
#         self.should_press_merged[linked_node] = 1 - self.should_press_merged[current_node]
#         return True

# class Program:
#     @staticmethod
#     def input_ints():
#         return map(int,input().split())

#     @classmethod
#     def test_by_input(This):
#         n,e=This.input_ints()
#         edges = [[] for i in range(n+1)]
#         for i in range(e):
#             node1,node2,is_vibrating=This.input_ints() 
#             edges[node1].append(Weighted_edge(node2, is_vibrating))
#             edges[node2].append(Weighted_edge(node1, is_vibrating))
#         res = Graphed_lights_out(Weighted_graph(n,edges)).try_solve()
#         if res is not None:
#             print()
#             print("solution:",end=" ")
#             for choice in res:
#                 print(choice,end=" ")
#         else:
#             print("It's impossible to solve this game!")
    
#     @classmethod    
#     def main(This):
#         This.test_by_input()
    
# if __name__=='__main__':
#     Program.main()
