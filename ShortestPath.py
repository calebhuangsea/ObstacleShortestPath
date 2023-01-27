"""
Cile Huang | calebhuangsea@gmail.com
Find the shortest path between start and end states that doesn't pass obstacles
using A* algorithm.
"""
import heapq
from shapely.geometry import LineString

"""
find the distance between two points
@:param x1: x coordinate for the first point
@:param x2: x coordinate for the first point
@:param y1: y coordinate for the second point
@:param y2: y coordinate for the second point
@:return: return the distance between two points
"""


def distance(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


"""
check if two line segments intersect
@:param p1: coordinate of head of line1
@:param p2: coordinate of head of line1
@:param p3: coordinate of tail of line2
@:param p4: coordinate of tail of line2
@:return: True if there is an intersection, false otherwise
https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018
"""


def intersect(p1, p2, p3, p4):
    # if two lines intersect on tails or heads
    if p1 == p3 or p2 == p3 or p1 == p4 or p2 == p4:
        return False

    # check if two lines intersect
    l1 = LineString([p1, p2])
    l2 = LineString([p3, p4])
    if l1.intersection(l2).is_empty:
        # if there is an intersection, return false
        return False
    return True


"""
check if a line is blocked by any obstacles
@:param A: coordinate of the head of the line
@:param B: coordinate of the tail of the line
@:param obstacles: every obstacles
@:return: return true if there is an intersection, false otherwise
"""


def block(A, B, obstacles):
    for line in obstacles:
        if intersect(A, B, line[0], line[1]):
            return True
    return False


"""
Represent a single state(point), contains coordinates
f, g, h values and parents
"""


class State:
    x: float = 0
    y: float = 0
    f: float = 0
    g: float = 0
    h: float = 0
    parent = None

    def __init__(self, x, y, p, dist):
        self.x = x
        self.y = y
        self.parent = p
        self.setG()
        self.setH(dist)
        self.f = self.g + self.h

    """
    Create a new g value if we have parent, otherwise default 0
    """

    def setG(self):
        if self.parent is not None:
            self.g = self.parent.g + distance(self.x, self.parent.x, self.y, self.parent.y)

    """
    Create a new h value
    """

    def setH(self, dist):
        self.h = distance(self.x, dist[0], self.y, dist[1])

    """
    Comparator, compare other states with f value
    """

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other) -> bool:
        if other:
            return self.x == other.x and self.y == other.y
        return False


# read file, construct states
# pass in the file path here
lines = open('', 'r').readlines()
# construct start state and pass it into states list, initialize goal
firstLine = [float(x) for x in lines[0].split()]
secondLine = [float(x) for x in lines[1].split()]
goal = (secondLine[0], secondLine[1])

start = State(firstLine[0], firstLine[1], None, goal)
states = []
# construct obstacles lines and pass points into the state
obstacles = []

# initialize open list and close list
openList = [(start.f, start)]
closeList = []

rec_num = int(lines[2])
# assign value to obstacles and states list
for i in range(rec_num):
    line = [float(x) for x in lines[3 + i].split()]

    p1 = State(line[0], line[1], None, goal)
    p2 = State(line[2], line[3], None, goal)
    p3 = State(line[4], line[5], None, goal)
    p4 = State(line[6], line[7], None, goal)
    states.append(p1)
    states.append(p2)
    states.append(p3)
    states.append(p4)

    # pass two obstacle line segments into the obstacles
    o1 = ((p1.x, p1.y), (p3.x, p3.y))
    obstacles.append(o1)
    o2 = ((p2.x, p2.y), (p4.x, p4.y))
    obstacles.append(o2)

tri_num = int(lines[rec_num + 3])
for i in range(tri_num):
    line = [float(x) for x in lines[4 + rec_num + i].split()]

    p1 = State(line[0], line[1], None, goal)
    p2 = State(line[2], line[3], None, goal)
    p3 = State(line[4], line[5], None, goal)

    # pass three obstacle line segments into the obstacles
    o1 = ((p1.x, p1.y), (p2.x, p2.y))
    obstacles.append(o1)
    o2 = ((p2.x, p2.y), (p3.x, p3.y))
    obstacles.append(o2)
    o3 = ((p3.x, p3.y), (p1.x, p1.y))
    obstacles.append(o3)

while True:
    # if openList is empty, stop the for loop
    if len(openList) == 0:
        break

    heapq.heapify(openList)

    # find and remove the lowest state in open list
    currState = heapq.heappop(openList)
    # put it in the closed state
    closeList.append(currState)

    # check if it is a goal state
    if (currState[1].x, currState[1].y) == goal:
        temp = currState[1]
        result = str((temp.x, temp.y)) + "(cost:" + str(temp.g) + ")"
        temp = temp.parent
        while temp:
            result = str((temp.x, temp.y)) + "(cost:" + str(temp.g) + ")" + "-->\n" + result
            temp = temp.parent
        print(result)

    # keep track of states that we are going to append later
    L = []
    # keep track of states that we are going to remove later
    removing = []

    # generate successors for current state
    for successor in states:
        if successor == currState[1] or block((currState[1].x, currState[1].y), (successor.x, successor.y), obstacles):
            continue

        # store the new successor
        newState = State(successor.x, successor.y, currState[1], goal)

        # check if it is already in the close list
        if (successor.f, successor) in closeList:
            if newState.f <= successor.f:
                closeList.remove((successor.f, successor))
                removing.append(successor)
                L.append(newState)
        # check if it is already in the openlist
        elif (successor.f, successor) in openList:
            if newState.f <= successor.f:
                openList.remove((successor.f, successor))
                removing.append(successor)
                L.append(newState)
        else:
            removing.append(successor)
            L.append(newState)

    for s in removing:
        states.remove(s)

    for s in L:
        states.append(s)
        openList.append((s.f, s))
