# Shortest Paths and Minimum Spanning Trees algorithm implementations
In this project one graph algorithm is being implemented:
    
    Prim's algorithm for the minimum spanning tree


## How to run
Ideally, the tool uv should be used to run this project, so the python libraries can be easily synchronized.
To sync the libraries execute ``uv sync`` in the root of the project.

To run the algorithm, simply execute ``uv run python3 ./src/prim.py {path to the .dot file}`` from the root of the project.

In case uv is not being used, this project needs the pydot library installed 


## Output of the program

Prim's algorithm will output a .dot file with the minimum spanning tree of the given graph.

