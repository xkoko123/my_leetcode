#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.19%)
# Likes:    2490
# Dislikes: 0
# Total Accepted:    328.2K
# Total Submissions: 1.1M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        ans = ""
        if len(s) in(0,1):
            return s
        for i in range(len(s)-1):
            xx = self.center_expand(s,i,i)
            yy = self.center_expand(s,i,i+1)
            # print(xx)
            # print(yy)
            # print("=======")
            if len(xx) > maxlen:
                maxlen = len(xx)
                ans = xx
            if len(yy) > maxlen:
                maxlen = len(yy)
                ans = yy
        return ans
                
            
    def center_expand(self, s:str,l:int, r:int) ->str:
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]

                    

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

