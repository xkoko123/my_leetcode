#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (62.14%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 54.1K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 
# 示例 1:
# 
# 
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
# 
# 
# 示例 2:
# 
# 
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 注意:
# 
# 
# 输入的字符串长度不会超过1000。
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) in (0,1):
            return 1
        count = 0
        for i in range(len(s)):
            xx = self.center_expand(s,i,i)
            yy = self.center_expand(s,i,i+1)
            # print(xx)
            # print(yy)
            # print("=======")
            count = count + xx + yy
        return count


    def center_expand(self, s:str,l:int, r:int) ->int:
        if r == len(s):
            return 0
        count = 0
        while l>=0 and r<len(s) and s[l] == s[r]:
            count += 1
            l-=1
            r+=1
        return count

                    

    def ishui(self, s:str)->bool:
        left = 0
        right = len(s)
        while left<right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

        
# @lc code=end

