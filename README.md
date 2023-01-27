# ObstacleShortestPath
- A Python program implemented using A* algorithm, allow users to input start location and goal location, as well as rectangle and triangle obstacles. 
- The programm will print out the shortest path and its backtrace distance. 
- MAKE SURE TO MODIFY THE CODE TO SET YOUR TEST FILE PATH

# Input Format(Input file must be a txt file)
x, y (start point)  
x, y (goal point)  
n (number of rectangle obstacles)  
x1 y1 x2 y2 x3 y3 x4 y4 (coordinates of 4 corners of rectangles)  
....  
m (number of triangle obstacles)  
x1 y1 x2 y2 x3 y3 (coordinates of 3 corners of triangles)  

# Example input file
0 0  
9 9  
5  
0 0 1 0 1 1 0 1  
2 2 3 2 3 3 2 3  
4 4 5 4 5 5 4 5  
6 6 7 6 7 7 6 7  
8 8 9 8 9 9 8 9  
1  
1 1 2 2 3 3  

# Example output of the example input file
(0.0, 0.0)(cost:0)-->  
(0.0, 1.0)(cost:1.0)-->  
(2.0, 3.0)(cost:3.8284271247461903)-->  
(4.0, 5.0)(cost:6.656854249492381)-->  
(6.0, 7.0)(cost:9.485281374238571)-->  
(8.0, 9.0)(cost:12.313708498984761)-->  
(9.0, 9.0)(cost:13.313708498984761)  

(0.0, 0.0)(cost:0)-->  
(1.0, 0.0)(cost:1.0)-->  
(3.0, 2.0)(cost:3.8284271247461903)-->  
(5.0, 4.0)(cost:6.656854249492381)-->  
(7.0, 6.0)(cost:9.485281374238571)-->  
(9.0, 8.0)(cost:12.313708498984761)-->  
(9.0, 9.0)(cost:13.313708498984761)  
