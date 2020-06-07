import heapq
from math import *

def manhatten(current, goal):
    return hypot(goal[0] - current[0], goal[1] - current[1])


def shortest_path(M,start,goal):
    paths = list()
    cost_heuristic = dict()
    cost = 0
    path = dict()
    path_front = [(cost,start)]
    cost_heuristic[start] = 0
    path[start] = None


    if start == goal:
        return [start]

    while len(path_front) > 0:
        
#         print(len(path_front))

        current = heapq.heappop(path_front)[1]

        if current==goal:
            break

        for neighbour in M.roads[current]:

            path_cost = manhatten(M.intersections[current], M.intersections[neighbour])

            cost = cost_heuristic[current] + path_cost

            if neighbour not in cost_heuristic or cost < cost_heuristic[neighbour]:

                path[neighbour] = current
                cost_heuristic[neighbour] = cost
                heapq.heappush(path_front,(cost,neighbour))
                
    temp = goal


    if temp not in cost_heuristic:
        return 

    while temp != start:

        paths.append(temp)

        temp = path[temp]

    paths.append(start)

    paths.reverse()

    print("shortest path called ", paths)
    return paths

