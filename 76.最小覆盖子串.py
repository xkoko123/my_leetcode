#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.98%)
# Likes:    659
# Dislikes: 0
# Total Accepted:    65.2K
# Total Submissions: 170.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 示例：
# 
# 输入: S = "PADAPOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        book = [0]*26
        right = 0
        left = 0
        import sys
        need = {}
        for c in t:
            need[c] = need.get(c,0)+1
        window = {}
        valid = 0

        length = sys.maxsize
        start = 0
        while right < len(s):
            c = s[right]
            right = right + 1
            if c in t:
                window[c] = window.get(c,0) + 1
                if need[c] == window[c]:
                    valid += 1
            # print("%d   %d  %d"%(left, right, valid))
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                    # print("UPDATE %d   %d  %s"%(start, right,s[start:start+length]))
                c = s[left]
                left += 1
                if c in t:
                    if need[c] == window[c]:
                        valid -= 1
                    window[c] = window.get(c) - 1
        if length == sys.maxsize:
            return ""
        else:
            return s[start: start + length]
# @lc code=end

