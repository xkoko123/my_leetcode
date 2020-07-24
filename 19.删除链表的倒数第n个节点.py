#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (37.10%)
# Likes:    898
# Dislikes: 0
# Total Accepted:    201.4K
# Total Submissions: 515.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        p = head
        ll = []
        i=0
        while p:
            i=i+1
            ll.append(p)
            if len(ll) > n+1:
                ll.pop(0)
            p = p.next
            print([x.val for x in ll])
        if i==n:
            return head.next
        ll[0].next = ll[1].next
        return head

    #双指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        secend = dummy
        for i in range(n+1):
            print(first.val)
            first = first.next
            
        
        while first:
            first = first.next
            secend = secend.next

        secend.next = secend.next.next
        return dummy.next
                    

        
# @lc code=end

