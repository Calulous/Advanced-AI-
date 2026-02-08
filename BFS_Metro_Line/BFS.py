'''
The following is an explanation of the BFS algorithm
& 
Steps to code a BFS algorithm 

'''

# Breadth - First Search (BFS) algorithm 
# bfs is a graph traversal algorithm that explores a graph level by level (imagine a lil tree branching down)
# uses FIFO - first in first out - shortest path 

# Source node - friends - friends' friends 

# STEPS
# 1- Take a graph from the user
# 2- Store it as an adjacency list
# 3- Use a queue to explore nodes level-by-level
# 4- Keep track of visited nodes so we don’t loop forever
# 5- Find the shortest path


'''
------------------------------------------------------
PROGRAM START: 
MENU for ' METRO LINE NAVIGATION '
------------------------------------------------------

'''

'''
SCL METRO NAVIGATOR — BFS DEMONSTRATION
----------------------------------------
1. Display Metro Map
2. Perform BFS Traversal (Explore all stations)
3. Find Shortest Route (Fewest Stops)
4. Exit
----------------------------------------
Enter your choice:

'''

print("---------------------------------------------------")
print("    SCL METRO NAVIGATOR — BFS DEMONSTRATION")
print("---------------------------------------------------")
print("1. Display Metro Map")
print("2. Perform BFS Traversal (Explore all stations)")
print("3. Find Shortest Route (Fewest Stops)")
print("4. Exit")
print("---------------------------------------------------")


choice = int(input("Enter your choice: "))
print("Your entered choice is: ", choice)






