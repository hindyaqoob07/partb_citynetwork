# -*- coding: utf-8 -*-
"""partb_graph

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tWRQLsb448a8GjWkFjPKq7xvtfzWk8fP
"""

import networkx as nx # import the networkx library for working with graphs
import matplotlib.pyplot as plt# import the matplotlib.pyplot library for visualization
G = nx.Graph()# This line creates  a new road network graph
intersections = [
    "Z1", "Z2", "Z3", "K1", "K2", "DA1", "DA2", "E1", "E2", "MBZ1",
    "JB1", "JB2", "JB3", "JB4", "W1", "W2", "W3", "W4", "S1", "S2",
    "US1", "US2", "AS1", "AS2", "Q1", "Q2", "AB1", "AB2", "AD1", "AD2",
    "H1", "H2", "AM1", "AM2", "JR1", "JR2", "MS1", "MS2", "DSC1", "DSC2",
    "AF1", "AF2"
] #This line defines the intersections
roads_with_weights = [
    ("Z1", "K1", 17), ("Z1", "MBZ1", 20), ("Z1", "DA1", 46),
    ("K1", "Z1", 13), ("K1", "E1", 14),
    ("DA1", "Z1", 50), ("DA1", "E1", 35),
    ("E1", "DA1", 28), ("E1", "K2", 17),
    ("MBZ1", "Z1", 21),
    ("JB1", "W2", 4), ("JB1", "S1", 8), ("JB1", "JB3", 18), ("JB1", "JB4", 17),
    ("W1", "Z1", 13), ("W1", "W2", 12), ("W1", "JB3", 12), ("W1", "W4", 11),
    ("S1", "JB1", 9), ("S1", "Z1", 16),
    ("US1", "Z1", 11), ("US1", "W2", 13),
    ("AS1", "Z1", 6), ("AS1", "K2", 13),
    ("Q1", "E1", 25), ("Q1", "JR1", 23),
    ("AB1", "Z1", 13), ("AB1", "K2", 12),
    ("AD1", "Z1", 16), ("AD1", "W2", 9),
    ("H1", "Z1", 13), ("H1", "K2", 10),
    ("AM1", "Z1", 10), ("AM1", "W2", 9),
    ("JR2", "E1", 12), ("JR2", "Q1", 22),
    ("MS1", "Z1", 15), ("MS1", "K2", 10),
    ("DSC1", "MBZ1", 8), ("DSC1", "E1", 8),
    ("AF1", "Z1", 15), ("AF1", "E1", 16)
]# This defines the roads with the corresponding weights which represent the average travel time in minutes

# This line add roads as edges with weights
for edge in roads_with_weights:#this line uses a foor loop which iterates over the roads_with_weights
    G.add_edge(edge[0], edge[1], weight=edge[2])

def dijkstra_path(graph, start, end):#This line defines a function for the dijstra algorithm which includes graph start and end in the argument
    try: #This line try to find the shortest path using NetworkX's dijkstra_path function
        return nx.dijkstra_path(graph, start, end)
    except nx.NetworkXNoPath: #If no path exists between the start and end nodes it return None
        return None
# Test cases for package distribution
package_distribution_test_cases = [
    ("Z1", "E1"),
    ("JB1", "AB1"),
    ("US1", "H2")
]

print("[2] Package Distribution Scenario:")
for start, end in package_distribution_test_cases: #This line uses a for loop that iterates through each test case & find the shortest path using the dijkstra_path function
    path = dijkstra_path(G, start, end) #This line defines a variable path 
    print(f"Shortest path from {start} to {end}: {path}")

# Test cases for reaching a point
reach_point_test_cases = [
    ("Z1", "MBZ1"),
    ("JB3", "S1"), 
    ("W4", "AB2")
]

print("\n[3] Reaching a Point Scenario:")
for start, end in reach_point_test_cases:#This line uses a for loop that iterates through each test case and find the shortest path using the dijkstra_path function
    path = dijkstra_path(G, start, end) #This line defines a variable path 
    print(f"Shortest path from {start} to {end}: {path}")
    
# These lines draw the graph
plt.figure(figsize=(20, 15)) #This line creates a new figure with a specific size for the plot
pos = nx.spring_layout(G, seed=42)  # This line computes node positions using the spring layout algorithm
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightgrey')  # This line draws nodes with specified size and color
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='grey')  # This line draws edges with specified width and color
labels = nx.get_edge_attributes(G, 'weight')  # This line gets the edge labels (weights) from the graph
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)  # This line draws the edge labels with specified font size
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')  # This line draws the node labels with specified font size and weight
plt.title("City Road Network - Dubai Roads & Intersections")  # This line sets the title for the plot
plt.tight_layout()  # This line adjusts the layout to prevent overlapping elements
plt.show()  # This line displays the plot

# Print the number of nodes and edges in the graph
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
