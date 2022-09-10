
# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

# You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod.
#  The map is represented as a matrix of 0s and 1s,
# where 0s are passable space and 1s are impassable walls.
# The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

# Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod,
#  where you are allowed to remove one wall as part of your remodeling plans.
# The path length is the total number of nodes you pass through,
# counting both the entrance and exit nodes.
# The starting and ending positions are always passable (0).
#  The map will always be solvable, though you may or may not need to remove a wall.
#  The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

# =========


def get_available_moves(map, pos, wall_removed):
    moves = []
    # Right
    if (pos[0] < len(map[0]) - 1 and (map[pos[1]][pos[0] + 1] == 0 or not wall_removed)):
        moves.append((1, 0))

    # down
    if (pos[1] < len(map) - 1 and (map[pos[1] + 1][pos[0]] == 0 or not wall_removed)):
        moves.append((0, 1))

    # left
    if (pos[0] > 0 and (map[pos[1]][pos[0] - 1] == 0 or not wall_removed)):
        moves.append((-1, 0))

    # up
    if (pos[1] > 0 and (map[pos[1] - 1][pos[0]] == 0 or not wall_removed)):
        moves.append((0, -1))
    
    return moves


def path_finding(map, moves, pos, wall_removed, depth = 0):

    if(depth > 100):
        return -1

    if((pos[0] == len(map[0]) - 1 and pos[1] == len(map) - 1)):
        return 100

    available_moves = get_available_moves(map, pos, wall_removed)
    if(len(available_moves) == 0):
        return -1

    moves += 1
    for move in available_moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        new_wall_removed = wall_removed
        if(not new_wall_removed):
            if(map[new_pos[1]][new_pos[0]] == 1):
                new_wall_removed = True
        
        score = path_finding(map, moves, new_pos, new_wall_removed, depth + 1)
        if(score == 100):
            # print("HURRAY", moves)
            return 100
    return 10
def solution(map):
    moves = 1
    pos = (0, 0)  # x, y
    wall_removed = False 

    available_moves = get_available_moves(map, pos, wall_removed)

    for move in available_moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if(path_finding(map, moves, new_pos, wall_removed) == 100):
            pos = new_pos
            moves += 1

    return moves


def middleware(map):
    output = solution(map)
    print(output)
    return output


if __name__ == "__main__":
    cases = [
        ([[0, 1, 1, 0],
          [0, 0, 0, 1],
          [1, 1, 0, 0],
          [1, 1, 1, 0]], 7),
        ([[0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]], 11),
        ([[0, 0],
          [0, 0]], 3),
        ([[0, 1],
          [1, 0]], 3),
    ]

    for case in cases:
        print("Testing", case[1], "OK" if middleware(
            case[0]) == case[1] else "FAIL")
