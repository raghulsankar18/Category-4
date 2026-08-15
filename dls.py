# ============================================================
# 3. Depth Limited Search - Web Crawler with Link Depth Limit
# ============================================================
web_graph = {
    "HomePage": ["About", "Products", "Blog"],
    "About": ["Team", "History"],
    "Products": ["Electronics", "Clothing"],
    "Blog": ["Post1", "Post2"],
    "Team": ["TeamMember1"],
    "History": [],
    "Electronics": ["Laptops", "Phones"],
    "Clothing": [],
    "Post1": [],
    "Post2": [],
    "TeamMember1": [],
    "Laptops": [],
    "Phones": []
}

def depth_limited_search(graph, node, target, limit, path=None):
    if path is None:
        path = [node]

    if node == target:
        return path

    if limit <= 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = depth_limited_search(graph, neighbor, target, limit - 1, path + [neighbor])
            if result:
                return result

    return None

# ---- Run ----
start_page = "HomePage"
target_page = "Phones"
depth_limit = 3

result = depth_limited_search(web_graph, start_page, target_page, depth_limit)

if result:
    print(f"Found '{target_page}' within depth {depth_limit}")
    print("Path:", result)
    print("Depth Reached:", len(result) - 1)
else:
    print(f"'{target_page}' not found within depth limit {depth_limit}")
