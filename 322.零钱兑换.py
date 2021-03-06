#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (40.56%)
# Likes:    723
# Dislikes: 0
# Total Accepted:    111.1K
# Total Submissions: 273.5K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import sys
        book = [-1]*(amount+1)
        book[0] = 0
        for money in range(1, amount+1):
            pass
            for c in coins:
                if money - c >=0:
                    if book[money-c] != -1:
                        if book[money] == -1:
                            book[money] = book[money-c] + 1
                        else:
                            book[money] = min(book[money-c] + 1, book[money])
        return book[amount]



# @lc code=end

