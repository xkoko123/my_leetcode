#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (54.08%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 56.2K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        # 双指针一个走两步一个走一步，找到中间节点
        first = head
        secend = head
        while first:
            if first.next:
                first = first.next.next
                secend = secend.next
            else:
                first = first.next

        mid = secend
        secend = self.reverseList(secend)
        
        pre = ListNode(-1)
        p = head
        while p!=mid and secend != None:
            temp_secend = secend.next
            temp_p = p.next
            print(p.val)
            print(secend.val)

            pre.next = p
            p.next = secend
            pre = secend

            p = temp_p
            secend = temp_secend

        if p != mid:
            pre.next = mid

        if secend != None:
            pre.next=secend

            

            

        


            


        
    
    def reverseList(self, head:ListNode):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
            
        
# @lc code=end

