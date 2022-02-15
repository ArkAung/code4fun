from typing import List

"""
The purpose of robot A is not maximizing its path value.
Its purpose is to minimize the path value of robot B.
Therefore, using a dynamic programming approach won't work since it will 
only maximize the path value of robot A while not providing a guarantee that robot B
will only be left with minimum path value after robot A's traversal

So what we will have to do is to consider every possible path that robot B can take 
and minimize the path value that robot B can have

There are not that many paths that robot A or robot B can take for a grid of 2 rows.
Since the robots can only move down or right. They can only move down once. 
Once they have moved down, they have no choice but to continue the path on the bottom 
row until they reach the end of the grid.

So now, the problem is more tractable since all we need to consider is 
i) for every position that robot A can move down, which path would yield the maximum path for robot B.
ii) what is the minimum of all the paths that robot B can take for every position that robot A can move down


Robot B will maximize as much as it can after robot A has traversed the grid.
Robot A has to make sure that it minimizes as much as possible for every possible path that 
it can traverse before robot B.

For every position that robot A can move down, robot B has two possible paths which can yield as much score as possible.
robot B will take the path which yields the maximum path. For all those maximum paths, which path from robot A can 
result in the minimum value for robot B.
"""


def gridGame(grid: List[List[int]]) -> int:
    toprow = sum(grid[0])
    bottomrow = 0
    ans = float("inf")

    n = len(grid[0])

    for i in range(n):
        toprow -= grid[0][i]
        ans = min(ans, max(bottomrow, toprow))
        bottomrow += grid[1][i]

    return ans
