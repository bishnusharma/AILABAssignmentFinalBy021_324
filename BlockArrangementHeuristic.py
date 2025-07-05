def local_heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        block = state[i]
        below_state = state[i + 1] if i + 1 < len(state) else "Table"
        goal_index = goal.index(block)
        below_goal = goal[goal_index + 1] if goal_index + 1 < len(goal) else "Table"

        if below_state == below_goal:
            h += 1
        else:
            h -= 1
    return h

def global_heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        block = state[i]
        below_state = state[i + 1:]
        goal_index = goal.index(block)
        below_goal = goal[goal_index + 1:]

        k = len(below_state)

        if below_state == below_goal:
            h += k
        else:
            h -= k
    return h

# Example usage:
start_state = ['A', 'D', 'C', 'B']    # Your image "Start"
goal_state = ['D', 'C', 'B', 'A']     # Your image "Goal"

print("Local Heuristic (Start):", local_heuristic(start_state, goal_state))
print("Global Heuristic (Start):", global_heuristic(start_state, goal_state))

print("Local Heuristic (Goal):", local_heuristic(goal_state, goal_state))
print("Global Heuristic (Goal):", global_heuristic(goal_state, goal_state))
