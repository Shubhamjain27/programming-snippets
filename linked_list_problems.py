#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.
#For example,
#Given 1->4->3->2->5->2 and x = 3,
#return 1->2->2->4->3->5.



def reorder(linkedlist):

    linkedlist.next


#Floyd Algo

def delectCycle(self):
    fastPtr = self.head
    slowPtr = self.head

    while(fastPtr and slowPtr):
        fastPtr = fastPtr.next
        if fastPtr==slowPtr:
            return True

        if fastPtr = None:
            return False

        fastPtr = fastPtr.next

        if fastPtr = slowPtr:
            return True
        slowPtr = slowPtr.next