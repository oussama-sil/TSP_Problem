import math 
import numpy as np


#? Function to compute the cost of a given path C in graph G 
def calc_path_cost(G,C): 
    #? G: Graph 
    #? C: List of node indices representing the path
    tmp = 0
    if(len(C)>1):
        for i in range(len(C)-1):
            tmp += G[C[i]][C[i+1]]
    return tmp


#? Estimate the cost of the unvisited path using the minimum edges
def evaluate_rest(G,A,C):
    #? G :Graphe
    #? A : Starting point 
    #? C : Path
    n = len(G)
    tmp = np.full((n,),999999) #! 999999 => inf
    for i in range(n):
        for j in range(n):
                #* Check if an edge exists between i and j
                if(i not in C or i == C[-1]) and (j not in C or j == A ) and G[i][j] > 0:
                    if(G[i][j]<tmp[i]):
                        tmp[i]= G[i][j]
    tmp.sort()  #? Place the infinite cost values at the end
    return np.sum(tmp[:n-len(C)+1])  #* sum of selected edges

#? Evaluate the cost of a given path C in graph G
def evaluate(G,A,C):
    #? G :Graphe
    #? A : Starting point 
    #? C : Path
    return calc_path_cost(G,C)  +  evaluate_rest(G,A,C)  

def BB(G,A,n):
    #? G :Graphe
    #? A : Starting point (starting node)
    #? C : Path
        
    nb_visited = 0 #* Counter for the visited nodes 

    P1 = [] #* DFS stack 
    P2 = [] #* Stack for the current path 

    #* Initialize the best path  
    cost_min = math.inf 
    path_min = None

    P1.append((A,1))  

    while (len(P1) > 0):
        s,d = P1.pop()
        nb_visited += 1
        
        while(len(P2) != d-1):
            P2.pop()
        P2.append(s)

        if(len(P2)==n+1): #* Check if a circuit is found 
            path_cost = calc_path_cost(G,P2)    
            print(f"Eval {P2} = {path_cost}  ---> {path_min} {cost_min}") 
            if(path_cost<cost_min):
                cost_min = path_cost
                path_min = P2.copy()
        else: 
            node_eval = evaluate(G,A,P2)  #* Evaluate the the node  
            if(node_eval <= cost_min): #? Check the bound condition 
                for k in range(n): #* neighbors of the current node 
                    if(G[s][k]>0): 
                        if(k not in P2 or len(P2)==n and k==A): 
                            P1.append((k,d+1))
    return path_min,cost_min,nb_visited


