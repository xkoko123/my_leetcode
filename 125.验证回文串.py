#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (45.94%)
# Likes:    256
# Dislikes: 0
# Total Accepted:    145.1K
# Total Submissions: 315.8K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        left = 0
        right = l-1
        while left<right:
            while left < l and s[left].isalnum() == False:
                left += 1
            while right > 0 and s[right].isalnum() == False :
                right -= 1
            if left >= l or right < 0 :
                return True
            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True
# @lc code=end

