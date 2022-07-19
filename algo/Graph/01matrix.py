"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

"""


from typing import Tuple


def updateMatrix(mat):

    def distanceFromZero(coordinates: Tuple):
        distance = 1

    def bfs(list, coordinates: Tuple,  memo={}):

        res = distanceFromZero(coordinates)

    return bfs(mat)


updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  # => [[0,0,0],[0,1,0],[0,0,0]]

updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])  # => [[0,0,0],[0,1,0],[1,2,1]]

"""
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
