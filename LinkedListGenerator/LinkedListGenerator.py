class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generateLinkedListFromArray(arr):
    reversedLinkedList = [ListNode(arr[len(arr) - 1], None)]
    for i in range(len(arr) - 2, -1, -1):
        reversedLinkedList.append(ListNode(arr[i]))
    linkedList = reversedLinkedList[::-1]
    for i in range(len(linkedList) - 1):
        linkedList[i].next = linkedList[i + 1]
    return linkedList[0]


