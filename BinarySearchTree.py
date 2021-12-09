class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res == None:
                return None
            else:
                return res
        else:
            return None

    def _get(self, key, Node):
        if not Node:
            return None
        elif Node.key == key:
            return Node.payload

        elif key < Node.key:
            return self._get(key, Node.leftChild)
        else:
            return self._get(key, Node.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemve = self._get(key, self.root)
            if nodeToRemve:
                self.remove(nodeToRemve)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.righChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.paload = succ.payload
        else:#下面的判断逻辑不是很好，应该先判断当前节点是左还是右子树，然后在判断当前节点是否有左孩子，或有右孩子
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.righChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChiild, currentNode.leftChild.rightChild)

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.righChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.leftChild.rightChild, currentNode.rightChild.rightChild)

    def printTree(self,node):
        if node == None:
            return

        self.printTree(node.leftChild)
        print(node.key)
        self.printTree(node.rightChild)

class TreeNode:
    def __init__(self,key,val,left=None, right = None, parent=None):
        self.key =key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.righChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not(self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBoathChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccesor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        # else:
        #     if self.parent:
        #         if self.isLeftChild():
        #             succ = self.parent
        #         else:
        #             self.parent.rightChild=None
        #             succ = self.parent.findSuccessor()
        #             self.parent.righChild=self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):#简单一些，只考虑在有子树中挑选继承者
        if self.isLeaf():
            if self.isLeftChild():#从右边找的继任者，肯定是做孩子了。
                self.parent.leftChild = None
            else:
                self.parent.righChild = None
        elif self.hasAnyChildren():
            # if self.hasLeftChild():#从右边找的继任者，继任者肯定是左孩子，并肯定只有右孩子
            #     if self.isLeftChild():
            #         self.parent.leftChild = self.leftChild
            #     else:
            #         self.parent.righChild = self.leftChild
            #     self.leftChild.parent = self.parent
            # else:

            self.parent.leftChild = self.rightChild

            self.rightChild.parent = self.parent



tree = BinarySearchTree()

#这个数是倾斜的，单向的。
tree.put(1,"aa")
tree.put(2,"bb")
tree.put(3,"cc")
tree.put(4,"dd")
tree.printTree(tree.root)
# print(tree.length())
# print(tree.root.key)
# print(tree.get(2))


