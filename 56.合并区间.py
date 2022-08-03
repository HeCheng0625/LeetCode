#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

from typing import List

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        answer = []
        answer.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > answer[len(answer)-1][1]:
                answer.append(intervals[i])
            else:
                answer[len(answer)-1] = [answer[len(answer)-1][0], max(answer[len(answer)-1][1], intervals[i][1])]
        return answer
# @lc code=end

