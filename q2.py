from dataclasses import dataclass

@dataclass
class Node:
    """Implements a (singly) linked-list node 

    For a Node n:
        n.data holds an integer value
        n.next refers to the next Node in the linked list, or None

    You must not modify this code.
    """
    data: int
    next: 'Node' = None

@dataclass
class LinkedList:
    """Implements a (singly) linked-list 

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    size: int = 0

@dataclass
class LinkedListWithTail:
    """Implements a (singly) linked-list 

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.tail refers to a Node that is the tail of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    tail: Node = None
    size: int = 0


def show(linked_list):
    """Prints values in the order they appear in the linked list.

    Each value should be separated by a newline and no other character. 
    """
    nextNode = linked_list.head
    while nextNode!=None:
        print(nextNode.data)
        nextNode = nextNode.next

def cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists.

    Returns a LinkedList which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    nodeToCheck=linked_list_a.head
    while nodeToCheck.next!=None:
        nodeToCheck = nodeToCheck.next
    nodeToCheck.next = linked_list_b.head

    linked_list_a.size += linked_list_b.size
    return(linked_list_a)
    

def smart_cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists, both with tail references.

    Returns a LinkedListWithTail which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    linked_list_a.tail.next = linked_list_b.head
    linked_list_a.size += linked_list_b.size
    linked_list_a.tail = linked_list_b.tail
    return(linked_list_a)

def make_queue():
    """Creates a linked list with the required structure.

    Returns a LinkedListWithTail containing the contents of Q as described in the 
    question.
    """
    N1 = Node(data=4)
    N2 = Node(data=9)
    N3 = Node(data=18)
    N4 = Node(data=3)
    N5 = Node(data=21)
    N1.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5
    N5.next = None
    linked_list_with_tail = LinkedListWithTail(head=N1,tail=N5,size=5)
    return(linked_list_with_tail)

def enqueue(ll_queue, value):
    """Returns a linked list representing a queue, after a new value has been
    enqueued.

    Returns a LinkedListWithTail containing the contents of a queue held in the
    LinkedListWithTail ll_queue, after a new value has been enqueued.
    """
    enqueueNode = Node(data=value)
    enqueueNode.next = None
    ll_queue.tail.next = enqueueNode
    ll_queue.tail = enqueueNode
    ll_queue.size += 1
    return(ll_queue)

def convert_to_array_queue(ll_queue):
    """
    "Converts" a LinkedList to an array-backed queue.

    Given a LinkedList ll_queue containing a tuple (A, f, r) where: 

    A is a list of length 10, backing the queue
    f is an int with a value facilitating access to the front of the queue
    r is an int with a value facilitating access to the rear of the queue.
    """
    A = []
    nextNode = ll_queue.head
    while nextNode!=None:
        A.append(nextNode.data)
        nextNode = nextNode.next
    while len(A)!=10:
        A.append(None)
    f = ll_queue.head.data
    r = ll_queue.tail.data
    return(A,f,r)

# test data
N1 = Node(3)
N2 = Node(7)
N1.next = N2
N2.next = None
LL1 = LinkedList(head=N1, size=2)

N3 = Node(2)
N4 = Node(8)
N3.next = N4
N4.next = None
LL2 = LinkedList(head=N3, size=2)

N5 = Node(1)
N6 = Node(9)
N5.next = N6
N6.next = None
LLWT1 = LinkedListWithTail(head=N5, tail=N6, size=2)

N7 = Node(0)
N8 = Node(4)
N7.next = N8
N8.next = None
LLWT2 = LinkedListWithTail(head=N7, tail=N8, size=2)

# selected simple tests
Lcat = cat(LL1, LL2)
assert(Lcat.head == N1)
assert(Lcat.head.next.next== N3)

Lsmcat = smart_cat(LLWT1, LLWT2)
assert(Lsmcat.head == N5)
assert(Lsmcat.tail == N8)

assert(make_queue().head.next.next.data == 18)

# there is no simple test for convert_to_array_queue(ll_queue)

assert(enqueue(make_queue(), 3).size > make_queue().size)