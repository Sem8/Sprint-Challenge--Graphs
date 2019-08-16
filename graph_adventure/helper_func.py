from util import Stack
from util import Queue

# Do a breadth first search to take player back to nearest room that has an unexplored exit
def unexplored_path(current_path, room_id, player):
    visited = set()
    # create a queue and enque a starting path as a vertex
    q = Queue()
    path = [room_id]
    q.enqueue(path)

    while q.size() > 0:
        # Deque the first path
        p = q.dequeue()
        # Set vertex as v as the first path
        v = p[0]
        # if vertex v is '?' set the path and break out of the if
        if v == '?':
            path = p[1:]
            break
        # if vertex v is not visited set is as visited
        if v not in visited:
            visited.add(v)
            # Add a path to all of it's neighbors and add it to queue
            for neighbors in current_path[v]:
                node = current_path[v][neighbors]
                new_path = p.copy()
                new_path.insert(0, node)
                q.enqueue(new_path)

    # set a player_move_directions list to contain directions a player needs to move back
    player_move_directions = []

    # Create a path of player_move_directions while the while loop runs
    while len(path) > 1:
        # remove the last room and store it as variable called current
        current = path.pop(-1)
        # find the prior direction that'll take you to the room you were in before and add it to player_move_directions list
        for route in current_path[current]:
            if current_path[current][route] == path[-1]:
                player_move_directions.append(route)

    # for every element in player_move_directions, move in those directions till you reach the spot
    for move in player_move_directions:
        player.travel(move)

    # return the player_move_directions to be appended to traversalPath
    return player_move_directions

# function to get the opposite direction to update our ? unexplored exits for the room we came from before
def opposite_direction(point):
    if point == 'n':
        direction = 's'
    elif point == 's':
        direction = 'n'
    elif point == 'e':
        direction = 'w'
    elif point == 'w':
        direction = 'e'
    return direction
