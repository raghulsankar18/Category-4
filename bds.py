# ============================================================
# 4. Bidirectional Search - Social Network Connection Finder
# ============================================================
from collections import deque

social_network = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David", "Eve"],
    "Charlie": ["Alice", "Frank"],
    "David": ["Bob", "Grace"],
    "Eve": ["Bob", "Grace"],
    "Frank": ["Charlie", "Grace"],
    "Grace": ["David", "Eve", "Frank", "Hank"],
    "Hank": ["Grace"]
}

def bfs_level(graph, frontier, visited, parents):
    next_frontier = deque()
    while frontier:
        person = frontier.popleft()
        for friend in graph.get(person, []):
            if friend not in visited:
                visited[friend] = True
                parents[friend] = person
                next_frontier.append(friend)
    return next_frontier

def build_path(parents_start, parents_end, meeting_point, start, goal):
    path = [meeting_point]

    node = meeting_point
    while node != start:
        node = parents_start[node]
        path.insert(0, node)

    node = meeting_point
    while node != goal:
        node = parents_end[node]
        path.append(node)

    return path

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    visited_start = {start: True}
    visited_goal = {goal: True}
    parents_start = {}
    parents_end = {}

    frontier_start = deque([start])
    frontier_goal = deque([goal])

    while frontier_start and frontier_goal:
        frontier_start = bfs_level(graph, frontier_start, visited_start, parents_start)
        meeting = set(visited_start) & set(visited_goal)
        if meeting:
            return build_path(parents_start, parents_end, meeting.pop(), start, goal)

        frontier_goal = bfs_level(graph, frontier_goal, visited_goal, parents_end)
        meeting = set(visited_start) & set(visited_goal)
        if meeting:
            return build_path(parents_start, parents_end, meeting.pop(), start, goal)

    return None

# ---- Run ----
person1 = "Alice"
person2 = "Hank"

connection = bidirectional_search(social_network, person1, person2)

if connection:
    print(f"Connection found between {person1} and {person2}:")
    print(" -> ".join(connection))
    print("Degrees of separation:", len(connection) - 1)
else:
    print(f"No connection found between {person1} and {person2}")
