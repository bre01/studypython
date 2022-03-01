#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack)==0 or d[stack.pop()]!=i:
                return False
        return len(stack)==0
# @lc code=end

