# dijkstra.py
import heapq
from typing import Dict, List, Optional
from .graph import Graph

def dijkstra(graph: Graph, start: str) -> Dict[str, float]:
    """
    使用 Dijkstra 算法计算从 start 到所有其他节点的最短距离。
    返回 {节点: 最短距离}
    """
    # 初始化距离字典，所有节点距离为无穷大
    distances = {v: float('inf') for v in graph.get_vertices()}
    distances[start] = 0

    # 优先队列 (距离, 节点)
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get_neighbors(current):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def shortest_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    返回从 start 到 end 的最短路径节点列表（使用 Dijkstra 和父节点追踪）。
    """
    # 初始化
    distances = {v: float('inf') for v in graph.get_vertices()}
    distances[start] = 0
    previous = {v: None for v in graph.get_vertices()}
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get_neighbors(current):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))

    # 回溯路径
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return None  # 不存在路径
