from BB import *
import tsplib95
import time
import numpy as np

# ? Tested benchmarks : br17.atsp, ft53.atsp, ftv33.atsp, ftv38.atsp

#? Function to load a benchmark 
def load_benchmark(file_name):
    problem = tsplib95.load(file_name)
    tmp = problem.edge_weights
    G = []
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            G.append(tmp[i][j])
    G = np.array(G).reshape((-1, problem.dimension))
    print(f"\nProblem size {problem.dimension}  G.shape={G.shape}  \n G = {G}")
    return G


#? Test 

G = load_benchmark("./benchmarks/ft53.atsp") #* Graph as adjacency matrix
n = 13      #* Number of nodes to use from the loaded graph 
A = 0       #* The starting point 
start = time.time()
print(f" Result of the execution : {BB(G[:n][:n], A, n)}")
end = time.time()
print(" Execution Time : "+str(end - start)+"s")
