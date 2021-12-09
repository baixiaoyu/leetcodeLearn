class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def printList(self, head):
        while(head):
            print(head.val)
            head = head.next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fake_head = ListNode()
        # fake_head.next=head

        while(head):
            temp = head
            head = head.next
            temp.next=fake_head.next
            fake_head.next=temp


        return fake_head.next

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None or head.next == None):
            return False
        while(head):
            temp = head.next
            while(temp):
                if head.next==temp.next:
                    return True
                temp=temp.next
            head = head.next

        return False

    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head
        cnt = 0
        tmp = head
        tmp2 = head
        while (tmp):

            if cnt == k - 1:
                swap1 = tmp
                print(swap1.val)
            tmp = tmp.next
            cnt = cnt + 1
        print(cnt)
        pos = cnt - k
        j = 0
        while (tmp2):
            if j == pos:
                swap2 = tmp2
                print(swap2.val)
            tmp2 = tmp2.next
            j = j + 1

        temp = swap2.val

        swap2.val = swap1.val
        swap1.val = temp

        return head

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None or head.next.next == None:
            return head

        pos=1
        tmp = head
        tmp2 = head
        while(tmp2):
            tmp=tmp.next
            pos = pos + 1
            if pos%2 == 1:

                tmp2 = tmp2.next.next
                tmp.next.next = tmp2.next
                tmp2.next=tmp.next
                tmp.next=tmp2
        return head

    def clone(self, head):
        clone_head =head
        fak_head = ListNode()
        e_head = ListNode()
        p = fak_head
        e = e_head
        i = 1
        while(clone_head):
            node = ListNode(clone_head.val)
            if i%2==1:
                p.next = node
                p=p.next
            else:
                e.next = node
                e=e.next

            clone_head = clone_head.next
            i = i+1
        p.next=e_head.next
        return fak_head.next

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None or head.next.next == None:
            return head
        #self.printList(head)

        if head == None: return head
        odd_head = head
        even_head = head.next
        p1 = odd_head
        p2 = even_head
        while (p2 and p2.next):
            p1.next = p1.next.next
            p2.next = p2.next.next

            p1 = p1.next
            p2 = p2.next

        p1.next = even_head

        return odd_head

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or head.next == None or k == 0:
            return head
        i = 1;
        new = head
        fak = head
        c = head
        cnt = 0
        while (c):
            c = c.next
            cnt = cnt + 1
        print(cnt)
        if k % cnt == 0:
            return head
        if k > cnt:
            k = k % cnt
        while (i < cnt - k):
            fak = fak.next
            new = new.next
            i = i + 1
        print(fak.val)
        # fak.next=None
        real_new = fak.next
        while (new.next):
            print(new.val)
            new = new.next
        new.next = head
        fak.next = None
        return real_new






