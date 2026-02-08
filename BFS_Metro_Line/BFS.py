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

def show_menu(): # wrapping the menu display in a function so that they use the menu until they exit 
    print("---------------------------------------------------")
    print("    SCL METRO NAVIGATOR — BFS DEMONSTRATION")
    print("---------------------------------------------------")
    print("1. Display Metro Map")
    print("2. Perform BFS Traversal (Explore all stations)")
    print("3. Find Shortest Route (Fewest Stops)")
    print("4. Exit")
    print("---------------------------------------------------")



def chosen_option(choice, graph):
    if choice == 1:
        print("Below is the Metro Map")
        display_metro_map(graph)                                    # connecting the me

    elif choice == 2:
        print("BFS Traversal - Exploring All Stations")
    elif choice == 3: 
        print("Finding Shortest Route - Fewest Stops")
    elif choice == 4: 
        print("Exit: Leaving Metro Navigator bye bye!")
    else:
        print("Invalid choice. Please select between 1 and 4.")


# GRAPH - Metro Line 

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


metro_line = input("Enter Metro Line to simulate (Red/Green): ")
print(f"Simulating {metro_line} Line")


# -------- MAIN METRO MENU LOOP --------      
running = True

while running:                              # using a while loop so that the user can keep using the menu, instead of using menu options only once
    show_menu()
    try:                                    # try and except for error-handling
        choice = int(input("Enter your choice: "))          # asking user to enter choice
        running = chosen_option(choice, graph)                     # chosen_option function runs with the value of choice var............. the return value gets stored in running var
                                                            # we do this so 'choice' is not a global var
                                                            # running has a true/ false value - false when user chooses 'Exit'
                                                            # return values help separate decision logic from control flow 
    except ValueError:                                      
        print("Please enter a valid number.")



'''
------------------------------------------------------
LOGIC for MENU Options: 
MENU for ' METRO LINE NAVIGATION '
------------------------------------------------------

'''

def display_metro_map(graph):                               # BFS is graph traversal
    print("Metro Map (Adjacency list): ")                   # shows the node - node connection 
    

    # For each station in the metro network, print the station name followed by all stations directly connected to it.
    for station in graph:                                               # for metro station in the metro line 
        print(f"{station} -> {', '.join(graph[station])}")              # if station = A, graph[station]: ['B', 'C'] + join = 'B' , 'C'



