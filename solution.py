class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
testList = ListNode()
head = testList
print("Right side up")
print(testList.val)
for i in range(1, 10):
    testList.next = ListNode(i)
    testList = testList.next
    print(testList.val)
current = head
prev = None
while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
print("Upside down")
for _ in range(0, 10):
    print(prev.val)
    prev = prev.next
