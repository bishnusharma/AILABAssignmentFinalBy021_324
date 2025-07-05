# 8-puzzle heuristics


goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                # Find goal position of val
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(i - x) + abs(j - y)
                            break
    return distance

state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

print("Misplaced Tiles Heuristic:", misplaced_tiles(state, goal_state))
print("Manhattan Distance Heuristic:", manhattan_distance(state, goal_state))
