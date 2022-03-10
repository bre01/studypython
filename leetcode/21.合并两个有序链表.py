 #
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list=[]
        while list1 and list2:
            if list1[0]>list2[0]:
                list.append(list2[0])
                list2.remove(list2[0])
            else:
                list.append(list1[0])
                list1.remove(list1[0])
        for i in list1:
            list.apepnd(i)
        for i in list2:
            list.append(i)
        return
        

        # @lc code=end

