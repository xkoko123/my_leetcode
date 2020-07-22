#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.14%)
# Likes:    2383
# Dislikes: 0
# Total Accepted:    278K
# Total Submissions: 972K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        answer = []
        for first,num in enumerate(nums):
            if first==0 or nums[first] != nums[first-1]:
                third = length - 1
                for secend in range(first+1,length):
                    if secend == first+1 or nums[secend] != nums[secend-1]:
                        while secend < third and  nums[first] + nums[secend] + nums[third] > 0:
                            third = third - 1
                        if secend >= third:
                            break

                        if nums[first] + nums[secend] + nums[third] == 0:
                            print("%d %d %d"%(nums[first], nums[secend], nums[third]))
                            answer.append([nums[first], nums[secend], nums[third]])
        return answer

                

# @lc code=end

