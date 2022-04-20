from ll import LinkedList

def kth_to_last(ll, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next
    while runner:
        current = current.next
        runner = runner.next
    return current

ll = LinkedList()
ll.generate(n=10, min_value=0, max_value=99)
print(ll)
print(kth_to_last(ll, 3))