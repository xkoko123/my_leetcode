#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (59.14%)
# Likes:    1152
# Dislikes: 0
# Total Accepted:    315.8K
# Total Submissions: 498.3K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        pre = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 != None and l2!=None:
            if l1.val <= l2.val:
                if head == None:
                    head = l1
                    pre = l1
                    l1 = l1.next
                else:
                    pre.next = l1
                    pre = l1
                    l1 = l1.next
            else:
                if head == None:
                    head = l2
                    pre = l2
                    l2 = l2.next
                else:
                    pre.next = l2
                    pre = l2
                    l2 = l2.next
        if l1 != None:
            pre.next = l1
        elif l2 != None:
            pre.next = l2
        return head




# @lc code=end

