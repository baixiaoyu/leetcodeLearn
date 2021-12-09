class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def getData(self):
        return self.item

    def setData(self, item):
        self.item = item

    def getNext(self):
        return self.next

    def setNext(self,nextNode):
        self.next = nextNode

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self,item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def isEmpty(self):
        return self.head == None

    def length(self):
        count =0
        current = self.head
        while(current):
            count = count +1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        previous = None
        current = self.head

        while current != None:
            if current.getData() == item:
                print("found it")
                if previous == None:
                    self.head=current.getNext()
                else:
                    previous.setNext(current.getNext())
                current.setData(None)
            else:
                previous = current
                current = current.getNext()


    def print(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.print()
print(mylist.length())
print(mylist.search(93))


mylist.remove(54)
mylist.print()
print(mylist.length())




