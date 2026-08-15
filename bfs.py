# ============================================================
# 1. Breadth First Search - Shortest Path in a Maze/Grid
# ============================================================
from collections import deque

def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        row, col = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            if (0 <= new_row < rows and 0 <= new_col < cols
                    and maze[new_row][new_col] == 0
                    and new_pos not in visited):
                visited.add(new_pos)
                queue.append(path + [new_pos])

    return None

# ---- Run ----
maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = bfs_maze(maze, start, goal)
print("Start:", start, "Goal:", goal)
print("Shortest Path:", path)
print("Path Length:", len(path) if path else "No path found")
