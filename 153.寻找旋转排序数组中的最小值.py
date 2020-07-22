#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (50.16%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    60.2K
# Total Submissions: 117.8K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 你可以假设数组中不存在重复元素。
# 
# 示例 1:
# 
# 输入: [3,4,5,1,2]
# 输出: 1
# 
# 示例 2:
# 
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# 
#

# @lc code=start

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         min = nums[0]
#         for num in nums:
#             if num < min:
#                 min = num
#                 return num
#         return min


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1]>nums[0]:
            return nums[0]
        return self.find_min(nums, 0, len(nums)-1)
        
    def find_min(self, nums, start, end):
        mid = (end + start)//2
        if nums[mid] > nums[mid+1] :
            return nums[mid+1]
        if nums[mid] < nums[mid-1] :
            return nums[mid]
        if nums[mid]>nums[0]:
            return self.find_min(nums, mid, end)
        else:
            return self.find_min(nums, start, mid-1)


# @lc code=end

