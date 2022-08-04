#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

from typing import List

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sums = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i >= 1 and j >= 1:
                    sums[i][j] = grid[i][j] + min(sums[i-1][j], sums[i][j-1])
                elif i >= 1:
                    sums[i][j] = grid[i][j] + sums[i-1][j]
                elif j >= 1:
                    sums[i][j] = grid[i][j] + sums[i][j-1]
                else:
                    sums[i][j] = grid[i][j]
        print(sums)
        return sums[m-1][n-1]
# @lc code=end

