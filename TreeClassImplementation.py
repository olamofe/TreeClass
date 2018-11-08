class node:
    
    def _init_(self, leftpointer = "NULL", rightpointer = "NULL", data = "NULL", parent = "NULL"):
        self.leftpointer = leftpointer
        self.rightpointer = rightpointer
        self.data = data
        self.parent = parent
        return self
        
    def setData(self, data):
        self.data = data
    def setparent(self, parent):
        self.parent = parent
        
    def setright(self, right):
        self.rightpointer = right
        
    def setleft(self, left):
        self.leftpointer = left
    def getData(self):
        return self.data
        
    def getright(self):
        return self.rightpointer
        
    def getleft(self):
        return self.leftpointer
        
    def printNode(self):
        print(self.data, " ", self.leftpointer, " ", self.rightpointer)
        

        
class tree(node):
    def _init_(self, root = "NULL", head = "NULL", position = "NULL", height = -1):
                
        return self
    def moveleft(self, node):
        return node.leftpointer
        
    def moveright(self, node):
        return node.rightpointer
        
    def setNode(self, node):
        if(root == "NULL"):
            createnode = node()
            createnode.setData(node)
            #root = node().setData(node)
            root = createnode
            head = root
            height = 0
            
        else:
            
            currentnode = head
            while True:
                if currentnode.getData < node.getData:
                    nextnode = moveleft(currentnode)
                    
                else:
                    nextnode = moveright(currentnode)
                
                if(nextnode == "NULL"):
                    #nextnode holds points to the currentnode.position value(where position can be left or right)
                    createnode = node().setData(node)
                    nextnode = createnode  
                    createnode.parent = currentnode
                    return
                else:
                    head = nextnode
                    return setNode(currentnode)