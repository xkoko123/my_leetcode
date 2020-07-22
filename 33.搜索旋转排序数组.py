#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.28%)
# Likes:    826
# Dislikes: 0
# Total Accepted:    144.3K
# Total Submissions: 377K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.search2(nums, 0,len(nums)-1,target)
        
    def search2(self,nums,start,end,target):
        print("%d %d"%(start,end))
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if start > end:
            return -1
        if nums[start] <= nums[mid]:#前边是有序
            if target>=nums[start] and nums[mid] >= target:
                return self.search2(nums,start, mid-1, target)
            else:
                return self.search2(nums,mid+1, end, target)
        else: #后边是有序的
            if target>=nums[mid] and nums[end] >= target:
                return self.search2(nums,mid+1, end, target)
            else:
                return self.search2(nums, start, mid-1, target)


# 4 5 6 7 8 9 0 1 2
# 2 3 1
# 1 3     0
# 6 7 1 2 3 4 5      6
# 6 7 1
# 6
# @lc code=end

