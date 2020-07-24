#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (48.48%)
# Likes:    804
# Dislikes: 0
# Total Accepted:    146.1K
# Total Submissions: 278.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 分治
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        if k == 2:
            return self.merge2lists(lists[0], lists[1])
        mid = k//2
        return self.merge2lists(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))

            
    def merge2lists(self, list1, list2):
        head = ListNode(-1)
        pre = head
        while list1 and list2:
            if list1.val >= list2.val:
                pre.next = list2
                pre = list2
                list2 = list2.next
            else:
                pre.next = list1
                pre = list1
                list1 = list1.next
        if list1 == None:
            pre.next = list2
        if list2 == None:
            pre.next = list1
        return head.next
        

# @lc code=end

