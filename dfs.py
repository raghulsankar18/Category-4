# ============================================================
# 2. Depth First Search - Traversing a Family Tree / Graph
# ============================================================
family_tree = {
    "John": ["Michael", "Sarah"],
    "Michael": ["Emma", "David"],
    "Sarah": ["Olivia"],
    "Emma": [],
    "David": ["Sophia"],
    "Olivia": [],
    "Sophia": []
}

def dfs(tree, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for child in tree.get(node, []):
        if child not in visited:
            dfs(tree, child, visited)

    return visited

def dfs_find_path(tree, node, target, path=None):
    if path is None:
        path = [node]

    if node == target:
        return path

    for child in tree.get(node, []):
        if child not in path:
            result = dfs_find_path(tree, child, target, path + [child])
            if result:
                return result

    return None

# ---- Run ----
print("Full DFS Traversal from John:", dfs(family_tree, "John"))

target = "Sophia"
path = dfs_find_path(family_tree, "John", target)
print(f"Path from John to {target}:", path)
