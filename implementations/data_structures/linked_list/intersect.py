from numpy import short
from ll import LinkedList

def isIntersect(ll1, ll2):
    nodes1 = []
    nodes2 = []
    n = ll1.head
    while n != None:
        nodes1.append(n)
        n = n.next
    n = ll2.head
    while n != None:
        nodes2.append(n)
        n = n.next
    ans = None
    i = 1
    while nodes1[-i] == nodes2[-i]:
        ans = nodes1[-1]
        i += 1
    return ans != None

def isIntersectSol(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False
    short, long = ll1, ll2 if len(ll1) < len(ll2) else ll2, ll1
    diff = len(long) - len(short)
    shorterNode, longerNode = short.head, long.head
    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode