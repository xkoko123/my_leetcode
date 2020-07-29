#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (45.92%)
# Likes:    415
# Dislikes: 0
# Total Accepted:    91.7K
# Total Submissions: 199.7K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = ListNode(-1)
        node.next = head
        pre = node
        while head != None:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return node.next
            
# @lc code=end

