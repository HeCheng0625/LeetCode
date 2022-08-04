#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

from typing import List

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_loc = 0
        for i in range(len(nums)):
            max_loc = max(max_loc, i+nums[i])
            if max_loc <= i:
                break
        if max_loc >= len(nums)-1:
            return True
        return False
# @lc code=end

