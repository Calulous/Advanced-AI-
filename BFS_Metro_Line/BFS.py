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
LOGIC for MENU Options: 
MENU for ' METRO LINE NAVIGATION '
moved this up as the function must always be defined before its called in Python
------------------------------------------------------

'''

# OPTION 1 LOGIC 
def display_metro_map(graph):                               # BFS is graph traversal
    print("Metro Map (Adjacency list): ")                   # shows the node - node connection 
    
    # For each station in the metro network, print the station name followed by all stations directly connected to it.
    for station in graph:                                               # for metro station in the metro line 
        print(f"{station} -> {', '.join(graph[station])}")              # if station = A, graph[station]: ['B', 'C'] + join = 'B' , 'C'


'''********************************************************************************************************************'''

# OPTION 2 LOGIC 
from collections import deque   # deque gives us an efficient queue (FIFO)

def bfs_traversal(graph, start):
    """
    BFS starts from a selected station and explores all nearby stations first before moving deeper.
    A visited set prevents infinite loops and repeated visits.
    Explores the metro line level by level 
    """

    visited = set()      # Keeps track of stations already visited
    queue = deque()      # Queue for BFS (FIFO)

    # Step 1: Start from the chosen station
    visited.add(start)   # Mark starting station as visited
    queue.append(start)  # Add starting station to the queue

    order = []           # Stores the order in which stations are visited, it starts of with an empty list and then populates 

    # Step 2: Continue until there are no stations left to explore
    while queue:

        # Step 3: Remove the first station from the queue
        current_station = queue.popleft()
        order.append(current_station)   # "Visit" the station

        # Step 4: Explore all directly connected stations
        for neighbor in graph.get(current_station, []):

            # Step 5: Visit neighbor only if it hasn't been visited before
            if neighbor not in visited:
                visited.add(neighbor)      # Mark as visited
                queue.append(neighbor)     # Add to queue for future exploration

    # Step 6: Return the BFS traversal order
    return order


'''********************************************************************************************************************'''

# OPTIOM 3 LOGIC 
from collections import deque

def bfs_shortest_path(graph, start, target):
    """
    Finds the shortest path (fewest stops) from start to target using BFS.
    Returns a list of stations representing the path, or None if no path exists.
    """

    # Edge case: start is already the target
    if start == target:
        return [start]

    visited = set()
    queue = deque()

    # parent dictionary lets us rebuild the path later
    parent = {start: None}

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()

        # Explore neighbors of current station
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current   # record how we reached neighbor
                queue.append(neighbor)

                # Stop early as soon as we find the target (BFS guarantee)
                if neighbor == target:
                    # Reconstruct path by walking backwards using parent pointers
                    path = []
                    node = target
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    path.reverse()
                    return path

    return None  # Target not reachable



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
        print("Below is the Metro Map")                             # user selects red/ green and then metro map displays
        display_metro_map(graph)                                    # connecting the option 1 logic 
        return True                                                 # this is so that the menu keeps showing 

    elif choice == 2:
        print("BFS Traversal - Exploring All Stations")

        # Ask user for starting station
        start = input("Enter starting station: ").strip()

        # Validate station
        if start not in graph:
            print("Invalid station name. Please choose a station from the metro map.")
            return True

        # Run BFS
        traversal = bfs_traversal(graph, start)

        # Display result
        print("\nBFS Traversal Order:")
        print(" -> ".join(traversal))

        return True

    elif choice == 3: 

        start = input("Enter start station: ").strip()
        if start not in graph:
            print("Invalid start station. Please choose from the metro map.")
            return True

        target = input("Enter destination station: ").strip()
        if target not in graph:
            print("Invalid destination station. Please choose from the metro map.")
            return True

        path = bfs_shortest_path(graph, start, target)

        if path is None:
            print("\nNo route exists between those stations.")
        else:
            print("\nShortest Route (Fewest Stops):")
            print(" -> ".join(path))
            print(f"Stops: {len(path)-1}")   # number of edges = stops between stations

        return True


    elif choice == 4: 
        print("Exit: Leaving Metro Navigator bye bye!")
        return False 
    else:
        print("Invalid choice. Please select between 1 and 4.")
        return True 





'''
--------------------------------------------------------------
GRAPH 
RED LINE & GREEN LINE METRO MAP 
--------------------------------------------------------------
'''

red_graph = {
    "Etisalat by e&": ["Stadium"],
    "Stadium": ["Etisalat by e&", "Al Nahda"],
    "Al Nahda": ["Stadium", "Airport Terminal 1"],
    "Airport Terminal 1": ["Al Nahda", "Union"],
    "Union": ["Airport Terminal 1", "BurJuman"],
    "BurJuman": ["Union", "Business Bay"],
    "Business Bay": ["BurJuman"]
}

green_graph = {
    "Etisalat": ["Al Qusais"],
    "Al Qusais": ["Etisalat", "Stadium (Green)"],
    "Stadium (Green)": ["Al Qusais", "Union"],
    "Union": ["Stadium (Green)", "BurJuman"],
    "BurJuman": ["Union", "Sharaf DG"],
    "Sharaf DG": ["BurJuman"]
}




# WHERE THE USER INPUT STARTS  

metro_line = input("Enter Metro Line to simulate (Red/Green): ").strip().lower()
print(f"Simulating {metro_line.capitalize()} Line")

if metro_line == "red":                         # connecting the logic to the display metro map function 
    graph = red_graph                           # if the user chooses red line then it displays red graph and vv 
elif metro_line == "green":
    graph = green_graph
else:
    print("Invalid line. Defaulting to Red.")   # i have just made the default go to red for error handling 
    graph = red_graph





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





