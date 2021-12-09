class TreeNode:
    def __init__(self,key,value,leftChild = None,rightChild = None,parent=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def isLeaf(self):
        if self.leftChild == None and self.rightChild == None:
            return True
        else:
            return False
    def isLeftChild(self):
        if self.parent.leftChild == self:
            return True
        else:
            return False
    def isRightChild(self):
        if self.parent.rightChild == self:
            return True
        else:
            return False
    def isRoot(self):
        if self.parent == None:
            return True
        else:
            return False
    def hasAnyChildren(self):
        if self.leftChild != None or self.rightChild != None:
            return True
        else:
            return False
    def hasBothChildren(self):
        if self.leftChild != None and self.rightChild != None:
            return True
        else:
            return False

    def findMin(self, node):
        while node.leftChild:
            node = node.leftChild
        return node

    def findSuccessor(self):
        return self.findMin(self.rightChild)

    def spliceOut(self):
        self.parent.leftChild = None
        if self.rightChild:
            self.rightChild.parent=self.parent
            self.parent.leftChild=self.rightChild

    def replaceNodeData(self,key,value,leftChild,rightChild):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        if self.leftChild:
            self.leftChild.parent = self
        if self.rightChild:
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self,key,value):
        if self.root:
            self._put(key,value,self.root)
        else:
            self.root = TreeNode(key,value)
        self.size = self.size+1

    def _put(self,key,value,node):
        if key < node.key:
            if node.leftChild == None:
                node.leftChild = TreeNode(key,value,parent=node)
            else:
                self._put(key,value,node.leftChild)
        else:
            if node.rightChild == None:
                node.rithChild = TreeNode(key,value,parent=node)
            else:
                self._put(key,value,node.rightChild)

    def get(self,key):
        if self.root == None:
            return None
        else:
            return self._get(key,self.root)

    def _get(self,key,node):
        if not node:
            return None
        else:
            if node.key ==  key:
                return node
            else:
                if key < node.key:
                    self._get(key,node.leftChild)
                else:
                    self._get(key,node.rightChild)



    def delete(self,key):
        if self.size > 1:
            node  = self.get(key)
            if node == None:
                raise KeyError("Error, key not in tree")
            else:
                self.remove(node)
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("Error, key not in tree")


    def remove(self,node):
        if node.isLeaf():
            if node.isLeftChildren():
                node.parent.leftChild = None
            elif node.isRightChildren():
                node.parent.rightChild = None
        elif node.hasBothChildren():
            succ = node.findSuccessor()
            succ.spliceOut()
            node.key = succ.key
            node.value = succ.value
        else:
            # 判断node是左树还是右树
            if node.isLeftChildren():
                if node.leftChild:
                    node.parent.leftChild=node.leftChild
                    node.leftChild.parent = node.parent
                elif node.rightChild:
                    node.parent.leftChild=node.rightChild
                    node.rightChild.parent = node.parent

            elif node.isRightchildren():
                    if node.leftChild:
                        node.leftChild.parent = node.parent
                        node.parent.rightChild = node.leftChild
                    elif node.rightChild:
                        node.rightChild.parent = node.parent
                        node.parent.righChild = node.righChild
            else:
                if node.leftChild:
                    node.replaceNodeData(node.leftChild.key,node.leftChild.value,node.leftChild,node.rightChild)
                elif node.rightChild:
                    node.replaceNodeData(node.rightChild.key,node.rightChild.value, node.leftChild,node.rightChild)








