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


def chosen_option():
    if choice == 1:
        print("Below is the Metro Map")
    elif choice == 2:
        print("BFS Traversal - Exploring All Stations")
    elif choice == 3: 
        print("Finding Shortest Route - Fewest Stops")
    elif choice == 4: 
        print("Exit: Leaving Metro Navigator bye bye!")
    else:
        print("Invalid choice. Please select between 1 and 4.")


chosen_option()




