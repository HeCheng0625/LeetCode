#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

from types import new_class
from typing import List

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        insert_index = len(intervals)
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                insert_index = i-1
                break
        if insert_index == -1:
            new_intervals = [newInterval]
            new_intervals.extend(intervals)
        elif insert_index == len(intervals):
            new_intervals = intervals
            new_intervals.append(newInterval)
        else:
            new_intervals = []
            for i in range(insert_index+1):
                new_intervals.append(intervals[i])
            new_intervals.append(newInterval)
            for i in range(insert_index+1, len(intervals)):
                new_intervals.append(intervals[i])
        answer = []
        answer.append(new_intervals[0])
        for i in range(1, len(new_intervals)):
            if new_intervals[i][0] > answer[len(answer)-1][1]:
                answer.append(new_intervals[i])
            else:
                answer[len(answer)-1] = [answer[len(answer)-1][0], max(answer[len(answer)-1][1], new_intervals[i][1])]
        return answer
# @lc code=end

