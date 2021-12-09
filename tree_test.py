import operator


class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            t = BinaryTree(newNode)
            self.leftChild = t
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            t = BinaryTree(newNode)
            self.rightChild = t
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self,obj):
        self.key = obj
    def getRootValue(self):
        return self.key

    def preorder(self,node):
        if node:
            print(node.key)
        if node.leftChild:
            self.preorder(node.leftChild)
        if node.rightChild:
            self.preorder(node.rightChild)
    def midorder(self,node):
        stack = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.leftChild
            current = stack.pop()
            print(current.key)
            node = current.rightChild


r = BinaryTree("a")
r.getRootValue()
r.insertLeft("b")
r.insertRight("c")
r.insertRight("d")
print("preorder")
print(r.preorder(r))
print("midorder")
print(r.midorder(r))


from stack import *

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree("")
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft("")
            pStack.push((currentTree))
            currentTree = currentTree.getLeftChild()
        elif i not in "+-*/)":
            currentTree.setRootValue(eval(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in "+-*/":
            currentTree.setRootValue(i)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            currentTree = pStack.pop()
        else:
            raise ValueError("unknown operation:" +i)
    return eTree

def evaluate(parseTree):
    opers = {"+":operator.add, "-":operator.sub,"*":operator.mul,"/":operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate((rightC)))
    else:
        return parseTree.getRootVal()
