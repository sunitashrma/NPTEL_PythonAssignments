class Tree:
    
 def __init__(self,value = None):
    self.leftchild  = None
    self.rightchild = None
    self.value = value

# inserting the values

def insert(self,value):
        if self is None:
            self.value = value
            self.leftchild = Tree()
            self.rightchild = Tree()

        if self.value == value:
            return

        if v < self.value:
            self.leftchild.insert(value)
            return

        if v > self.value:
            self.rightchild.insert(value)
            return





    



