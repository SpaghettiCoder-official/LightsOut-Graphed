from graphed_Lights_out import Graphed_Lights_out
from weighted_graph import *

class Program:
    @staticmethod
    def input_ints():
        return map(int,input().split())

    @classmethod
    def test_by_input(This):
        n,e=This.input_ints()
        edges = [[] for i in range(n+1)]
        for i in range(e):
            node1,node2,is_vibrating=This.input_ints() 
            edges[node1].append(Weighted_edge(node2, is_vibrating))
            edges[node2].append(Weighted_edge(node1, is_vibrating))
        res = Graphed_Lights_out(Weighted_graph(n,edges)).try_solve()
        if res is not None:
            print()
            print("solution:",end=" ")
            for choice in res:
                print(choice,end=" ")
        else:
            print("It's impossible to solve this game!")
    
    @classmethod    
    def main(This):
        This.test_by_input()
    
if __name__=='__main__':
    Program.main()