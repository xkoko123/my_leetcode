#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (44.90%)
# Likes:    853
# Dislikes: 0
# Total Accepted:    122.4K
# Total Submissions: 272.4K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1] * len(nums)
        m = -float('inf')
        if len(nums) in (0,1):
            return len(nums)
            
        for i in range(len(nums)):
            for j in range(i-1, -1,-1):
                if nums[j] < nums[i]:
                    ans[i] = max(ans[i],ans[j] + 1)
                    # print(nums[j])
        return max(ans)
            

        
# @lc code=end

