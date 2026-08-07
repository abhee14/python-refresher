def count_reachable(
    graph: dict[int, list[int]],
    start: int,
) -> int:
    visited: set[int] = set()

    def dfs(node: int) -> None:
        if node in visited:
            return

        visited.add(node)

        for neighbour in graph.get(node, []):
            dfs(neighbour)

    dfs(start)
    return len(visited)