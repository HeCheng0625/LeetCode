#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        char_map = {s[0]: 0}
        answers = [0 for i in range(len(s))]
        answers[0] = 1
        for i in range(1, len(s)):
            if s[i] not in char_map:
                answers[i] = answers[i-1] + 1
            else:
                answers[i] = min(i - char_map[s[i]], answers[i-1] + 1)
            char_map[s[i]] = i
        return max(answers)
# @lc code=end
