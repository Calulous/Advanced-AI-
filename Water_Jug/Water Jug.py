"""
Why BFS is a Good Choice Here:

In the Water Jug Problem, we are trying to find the shortest sequence 
of actions that leads to the target amount. Since every action 
(fill, empty, pour) counts as one step, this problem can be modeled 
as an unweighted graph.

Breadth-First Search (BFS) is ideal in this case because it explores 
all possible states step-by-step, level by level. This ensures that 
the first time we find the solution, it uses the fewest number of moves.

That is why BFS guarantees the optimal solution for this problem.


Backtracking explores one path deeply before trying alternatives.
Greedy Search makes decisions based only on immediate improvement.
"""


from collections import deque
from math import gcd # Greatest Common Divisor 

'''
LOGIC:
Are the values solvable?
Can the target value be reached? 
'''
def is_solvable(jugA, jugB, target):                        # solvable = True 
    # A solution exists only if:                            # this function has the logic if the sizes r solvable 
    # 1) target is not bigger than the largest jug
    # 2) gcd(capA, capB) divides target
    if target < 0:
        return False
    if target == 0:
        return True
    if target > max(jugA, jugB):                            # target <= largest jug size 
        return False
    return target % gcd(jugA, jugB) == 0                    # remainder = 0, gcd(4.3) = 1 and gcd(6,10)=2, greatest common divider btw both jug sizes



"""
From a given state (a, b), generate all reachable next states.
Each move includes:
    1) The new state after performing the action
    2) A text description of the action (for path reconstruction)
"""

def get_next_states(state, jugA, jugB):
    
    # ---------------------------------------------------------
    # STEP 1: Unpack the current state
    # ---------------------------------------------------------
    # state is a tuple (a, b)
    # a = current amount of water in Jug A
    # b = current amount of water in Jug B
    a, b = state

    # This list will store all possible next moves from (a, b)
    # Each element will look like:
    # ((new_a, new_b), "Action description")
    moves = []

    # ---------------------------------------------------------
    # STEP 2: Try ALL possible legal operations
    # ---------------------------------------------------------
    # These 6 operations define the transition model of the problem.


    # ---------------------------------------------------------
    # 1) Fill Jug A completely
    # ---------------------------------------------------------
    # Only possible if Jug A is not already full
    if a < jugA:
        # New state becomes (jugA, b)
        moves.append(((jugA, b), f"Fill A to {jugA}"))


    # ---------------------------------------------------------
    # 2) Fill Jug B completely
    # ---------------------------------------------------------
    # Only possible if Jug B is not already full
    if b < jugB:
        # New state becomes (a, jugB)
        moves.append(((a, jugB), f"Fill B to {jugB}"))


    # ---------------------------------------------------------
    # 3) Empty Jug A completely
    # ---------------------------------------------------------
    # Only possible if Jug A has water
    if a > 0:
        # New state becomes (0, b)
        moves.append(((0, b), "Empty A"))


    # ---------------------------------------------------------
    # 4) Empty Jug B completely
    # ---------------------------------------------------------
    # Only possible if Jug B has water
    if b > 0:
        # New state becomes (a, 0)
        moves.append(((a, 0), "Empty B"))


    # ---------------------------------------------------------
    # 5) Pour water from Jug A into Jug B
    # ---------------------------------------------------------
    # Conditions:
    # - Jug A must have water
    # - Jug B must not be full
    if a > 0 and b < jugB:

        # Calculate how much we can pour WITHOUT overflowing
        # We pour the minimum of:
        # - how much water is in A
        # - how much space is left in B
        pour = min(a, jugB - b)

        # New state after pouring
        # A loses 'pour'
        # B gains 'pour'
        moves.append(((a - pour, b + pour), f"Pour {pour} from A -> B"))


    # ---------------------------------------------------------
    # 6) Pour water from Jug B into Jug A
    # ---------------------------------------------------------
    # Conditions:
    # - Jug B must have water
    # - Jug A must not be full
    if b > 0 and a < jugA:

        # Again, prevent overflow
        pour = min(b, jugA - a)

        # New state after pouring
        moves.append(((a + pour, b - pour), f"Pour {pour} from B -> A"))


    # ---------------------------------------------------------
    # STEP 3: Return all valid next states
    # ---------------------------------------------------------
    # BFS will use this list to explore the state space
    return moves



def solve_water_jug_bfs(jugA, jugB, target):
    """
    Uses Breadth-First Search (BFS) to solve the Water Jug Problem.
    
    Returns:
        A list of steps representing the shortest solution path.
        Each step is a tuple:
            (state, action_taken)
        Starting from ((0, 0), "Start")
    """

    # ---------------------------------------------------------
    # STEP 1: Define the starting state
    # ---------------------------------------------------------
    # Initially, both jugs are empty.
    start = (0, 0)

    # ---------------------------------------------------------
    # STEP 2: Check if problem is solvable
    # ---------------------------------------------------------
    # If mathematical conditions fail, no need to run BFS.
    if not is_solvable(jugA, jugB, target):
        return None


    # ---------------------------------------------------------
    # STEP 3: Initialize BFS structures
    # ---------------------------------------------------------

    # Queue for BFS (FIFO structure)
    queue = deque([start])

    # Visited set prevents infinite loops
    visited = set([start])

    # Parent dictionary helps reconstruct path
    # parent[state] = (previous_state, action_used_to_get_here)
    parent = {start: (None, "Start")}


    # ---------------------------------------------------------
    # STEP 4: BFS Loop
    # ---------------------------------------------------------
    # Continue until queue becomes empty.
    while queue:

        # Remove first element from queue (FIFO behavior)
        current = queue.popleft()

        # Extract amounts in each jug
        a, b = current


        # -----------------------------------------------------
        # STEP 5: Goal Test
        # -----------------------------------------------------
        # If either jug has the target amount, we stop.
        if a == target or b == target:

            # Reconstruct the solution path
            path = []
            node = current

            # Backtrack from goal to start
            while node is not None:
                prev_state, action = parent[node]
                path.append((node, action))
                node = prev_state

            # Reverse path so it goes from start → goal
            path.reverse()

            return path


        # -----------------------------------------------------
        # STEP 6: Generate All Possible Next States
        # -----------------------------------------------------
        # Use the transition function
        for next_state, action in get_next_states(current, jugA, jugB):

            # Only explore if not visited before
            if next_state not in visited:

                visited.add(next_state)

                # Record how we reached this state
                parent[next_state] = (current, action)

                # Add new state to BFS queue
                queue.append(next_state)


    # ---------------------------------------------------------
    # STEP 7: If No Solution Found
    # ---------------------------------------------------------
    return None



#------------------------------------------------------------------------------------------------------------------------------#
'''
MAIN FUNCTION 
USER INPUT
THEN CALLS THE LOGIC FUNCTIONS 

'''

def main():
    print("\n WATER JUG PROBLEM SOLVER (BFS State-Space Search)")

    jugA = int(input("Enter capacity of Jug A: "))
    jugB = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    print("\n--- Problem Setup ---")
    print(f"Jug A Capacity : {jugA}")
    print(f"Jug B Capacity : {jugB}")
    print(f"Target Amount  : {target}")
    print("---------------------")


    solution = solve_water_jug_bfs(jugA, jugB, target)

    if solution is None:
        print("\n No solution exists for these inputs.")
        print("Rule: target <= max(jugA, jugB) and gcd(jugA, jugB) must divide target.")
        return

    print("\n Solution found (fewest moves):\n")
    for i, (state, action) in enumerate(solution):
        a, b = state
        print(f"Step {i}: {action:<18} -> (A={a}, B={b})")

    print(f"\n Target reached: {target}")


if __name__ == "__main__":
    main()