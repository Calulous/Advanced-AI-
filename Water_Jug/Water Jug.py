# JAR SIZES MUST BE TAKEN FROM USER 
# SHOW THE PATH 
# even jar c shud be user input ... basically the user shud enter the size of 2 jugs and how much they want in the jug 

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
    Each move includes an action description for showing the path.
"""

def get_next_states(state, jugA, jugB):
    
    a, b = state
    moves = []

    # 1) Fill A
    if a < jugA:
        moves.append(((jugA, b), f"Fill A to {jugA}"))

    # 2) Fill B
    if b < jugB:
        moves.append(((a, jugB), f"Fill B to {jugB}"))

    # 3) Empty A
    if a > 0:
        moves.append(((0, b), "Empty A"))

    # 4) Empty B
    if b > 0:
        moves.append(((a, 0), "Empty B"))

    # 5) Pour A -> B
    if a > 0 and b < jugB:
        pour = min(a, jugB - b)
        moves.append(((a - pour, b + pour), f"Pour {pour} from A -> B"))

    # 6) Pour B -> A
    if b > 0 and a < jugA:
        pour = min(b, jugA - a)
        moves.append(((a + pour, b - pour), f"Pour {pour} from B -> A"))

    return moves


def solve_water_jug_bfs(jugA, jugB, target):
    """
    BFS over state space.
    Returns a reconstructed path as a list of tuples:
    [(state, action), ...]
    starting with ((0,0), "Start")
    """
    start = (0, 0)

    if not is_solvable(jugA, jugB, target):
        return None

    queue = deque([start])
    visited = set([start])

    # parent[state] = (previous_state, action_used)
    parent = {start: (None, "Start")}

    while queue:
        current = queue.popleft()
        a, b = current

        # Goal test
        if a == target or b == target:
            # Reconstruct the path
            path = []
            node = current
            while node is not None:
                prev, action = parent[node]
                path.append((node, action))
                node = prev
            path.reverse()
            return path

        # Explore neighbors (next possible states)
        for next_state, action in get_next_states(current, jugA, jugB):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (current, action)
                queue.append(next_state)

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