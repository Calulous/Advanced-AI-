# JAR SIZES MUST BE TAKEN FROM USER 
# SHOW THE PATH 
# even jar c shud be user input ... basically the user shud enter the size of 2 jugs and how much they want in the jug 

from collections import deque
from math import gcd # Greatest Common Divisor 


def is_solvable(capA, capB, target):                        # the user will provide sizes of jugs and target value 
    # A solution exists only if:                            # this function has the logic if the sizes r solvable 
    # 1) target is not bigger than the largest jug
    # 2) gcd(capA, capB) divides target
    if target < 0:
        return False
    if target == 0:
        return True
    if target > max(capA, capB):
        return False
    return target % gcd(capA, capB) == 0


def get_next_states(state, capA, capB):
    """
    From a given state (a, b), generate all reachable next states.
    Each move includes an action description for showing the path.
    """
    a, b = state
    moves = []

    # 1) Fill A
    if a < capA:
        moves.append(((capA, b), f"Fill A to {capA}"))

    # 2) Fill B
    if b < capB:
        moves.append(((a, capB), f"Fill B to {capB}"))

    # 3) Empty A
    if a > 0:
        moves.append(((0, b), "Empty A"))

    # 4) Empty B
    if b > 0:
        moves.append(((a, 0), "Empty B"))

    # 5) Pour A -> B
    if a > 0 and b < capB:
        pour = min(a, capB - b)
        moves.append(((a - pour, b + pour), f"Pour {pour} from A -> B"))

    # 6) Pour B -> A
    if b > 0 and a < capA:
        pour = min(b, capA - a)
        moves.append(((a + pour, b - pour), f"Pour {pour} from B -> A"))

    return moves


def solve_water_jug_bfs(capA, capB, target):
    """
    BFS over state space.
    Returns a reconstructed path as a list of tuples:
    [(state, action), ...]
    starting with ((0,0), "Start")
    """
    start = (0, 0)

    if not is_solvable(capA, capB, target):
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
        for next_state, action in get_next_states(current, capA, capB):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (current, action)
                queue.append(next_state)

    return None



'''
MAIN FUNCTION 
USER INPUT
THEN CALLS THE LOGIC FUNCTIONS 

'''
def main():
    print("\n WATER JUG PROBLEM SOLVER (BFS State-Space Search)")

    capA = int(input("Enter capacity of Jug A: "))
    capB = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    solution = solve_water_jug_bfs(capA, capB, target)

    if solution is None:
        print("\n No solution exists for these inputs.")
        print("Rule: target <= max(capA, capB) and gcd(capA, capB) must divide target.")
        return

    print("\n Solution found (fewest moves):\n")
    for i, (state, action) in enumerate(solution):
        a, b = state
        print(f"Step {i}: {action:<18} -> (A={a}, B={b})")

    print(f"\n Target reached: {target}")


if __name__ == "__main__":
    main()