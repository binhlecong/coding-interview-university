from ll import LinkedListNode


def detect_loop(ll):
    head = ll.head
    seen = set()
    n = head
    while n != None:
        if n in seen:
            return n
        else:
            seen.add(n)
        n = n.next
    return None


def detect_loop_sol(ll):
    slow = fast = ll.head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast
