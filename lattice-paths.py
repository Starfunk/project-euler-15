# Solution to problem 16 of Project Euler. 
# https://projecteuler.net/problem=15a

# We first convert the n by n grid into a a graph where each 
# grid intersection represents a vertex. So a 1x1 grid can be seen
# as a graph with 4 vertices (i.e. a 2x2 graph), likewise, a 2x2 grid 
# can be seen as a 3x3 graph and so on.

# How many unique paths are there starting from the top and leftmost
# vertex and assuming that the only legal moves are to the right and 
# down? In order to answer this question we work backwards starting from
# the rightmost and bottom vertex (i.e. the final vertex). Then the 
# vertices directly to the left and above the final vertex each possess 
# 1 unique path to the final vertex. We continue to work backwards
# figuring out each vertex's number of unique paths to the final vertex
# by looking its adjacent vertices. 

import numpy as np

# Specify to Python that we don't want it to round the answer
np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:0.2f}'.format})

#Specify number of dimensions. Note that in order to get an N by N grid,
# you must let n = N + 1, i.e. to get a 20x20 grid let n = 21. This
# is because n represents the number of vertices not the number of edges
n = 21

# Create graph with (21 times 21) 441 vertices
grid = np.zeros((n,n))

# Set the base values for the grid (these are our base case vertices 
# to the left and above the final vertex
grid[n-1][n-2] = 1
grid[n-2][n-1] = 1

# Initialize counters
row = 1
col = 3
row_start = 1
col_start = 3

# Initialize counter which keeps track of how many loops should be run 	
counter = 3

# While the number of unique paths for the initial vertex has not been
# found continue to iterate through the grid until the value for the
# initial vertex (i.e. the left and topmost vertex) has been calculated
while grid[0][0] == 0:
	row = row_start
	col = col_start
	for j in range(counter):
		if row != 1:
			grid[n-row][n-col] = grid[n-row][n-col] + grid[n-row+1][n-col]
		if col != 1:
			grid[n-row][n-col] = grid[n-row][n-col] + grid[n-row][n-col+1]
		row = row + 1	
		col = col - 1	
	if col_start != n: 
		col_start = col_start + 1
		counter = counter + 1
	else:
		row_start = row_start + 1
		counter = counter - 1

# Print solution	
print("The number of unique paths from the initial vertex is: "
		+ str(grid[0][0]))



	
