#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (36.63%)
# Likes:    662
# Dislikes: 0
# Total Accepted:    79.8K
# Total Submissions: 199.9K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import sys
        pre_max = 1
        pre_min = 1
        answer = -sys.maxsize
        for i,num in enumerate(nums):
            pre_max_t = max(num, pre_max * num, pre_min * num)
            pre_min_t = min(num, pre_min * num, pre_max * num)
            pre_max = pre_max_t
            pre_min = pre_min_t
            answer = max(pre_max, pre_min, answer)
            # print("%d %d %d"%(pre_max, pre_min, answer))
        return answer
# -4 12 6 
# -4 -3 -24
# -4 12 12
# @lc code=end

