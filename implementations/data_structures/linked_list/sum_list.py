from audioop import add
from unittest import result
from ll import LinkedList
from ll import LinkedListNode


def sum_lists(ll1, ll2):
    head1 = ll1.head
    head2 = ll2.head
    ans = LinkedList()
    c1, c2 = head1, head2
    carry = 0
    while c1 != None and c2 != None:
        value = c1.value + c2.value + carry
        digit, carry = value % 10, value // 10
        ans.add(digit)
        c1 = c1.next
        c2 = c2.next

    if c1 != None:
        value = c1.value + carry
        digit, carry = value % 10, value // 10
        ans.add(digit)
        c1 = c1.next
    elif c2 != None:
        value = c2.value + carry
        digit, carry = value % 10, value // 10
        ans.add(digit)
        c2 = c2.next
    if carry > 0:
        ans.add(carry)
    return ans


def sum_lists_sol(ll1, ll2):
    n1, n2 = ll1.head, ll2.head
    ans = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ans.add(result % 10)
        carry = result // 10
    if carry > 0:
        ans.add(carry)
    return ans


ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))
print(sum_lists_sol(ll_a, ll_b))
