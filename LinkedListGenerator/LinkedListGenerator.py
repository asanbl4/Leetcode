class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generateLinkedListFromArray(arr):
    linkedList = [ListNode(arr[i]) for i in range(len(arr))]
    for i in range(len(linkedList) - 1):
        linkedList[i].next = linkedList[i + 1]
    return linkedList[0]


