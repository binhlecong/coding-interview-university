from ll import LinkedList


def partition(head, x):
    runner = curr = head
    while curr is not None:
        if curr.value < x:
            runner.value, curr.value = curr.value, runner.value
            runner = runner.next
        curr = curr.next


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll.head, 50)
print(ll)
