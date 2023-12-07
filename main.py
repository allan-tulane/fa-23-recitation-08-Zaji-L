from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
  """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

  ### TODO
  def get_neighbors(vertex):
    return graph[vertex]

  dist = {node: (float('inf'), float('inf')) for node in graph}
  dist[source] = (0, 0)

  frontier = [(0, source)]  # (distance, vertex)

  while frontier:
    cur_dist, current = heappop(frontier)

    if cur_dist > dist[current][0]:
      continue

    for neighbor, weight in get_neighbors(current):
      alt_dist = (dist[current][0] + weight, dist[current][1] + 1)

      if alt_dist < dist[neighbor]:
        dist[neighbor] = alt_dist
        heappush(frontier, (alt_dist[0], neighbor))

      elif alt_dist == dist[neighbor]:
        dist[neighbor] = (alt_dist[0], min(alt_dist[1], dist[neighbor][1]))

  return dist


def bfs_path(graph, source):
  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

  ###TODO
  def get_neighbors(vertex):
    return graph[vertex]

  parent = {source: None}
  frontier = deque([source])

  while frontier:
    current = frontier.popleft()

    for neighbor in get_neighbors(current):
      if neighbor not in parent:
        parent[neighbor] = current
        frontier.append(neighbor)

  return parent


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
  ###TODO
  path = []
  current = destination

  while current is not None and current in parents:
    path.append(current)
    current = parents[current]

  if path and path[-1] != destination:
    return "No path"
  else:
    return ''.join(reversed(path[:-1]))
