class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        if self.root == None:
            self.root = Node(newvalue)      
        else:
            putta(newvalue, self.root)

    def __contains__(self,value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")
            
        
def putta(newvalue, root):
    node = root
     
    if newvalue < node.value and root.left == None:
        root.left = Node(newvalue)
        #print("a")
        return root
      
    elif newvalue < node.value and root.left != None:
        putta(newvalue, node.left)
        #print("b")

    elif newvalue > node.value and root.right == None:
        root.right = Node(newvalue)
        #print("c")
        return root
    
    elif newvalue > node.value and root.right != None:
        putta(newvalue, node.right)
        #print("d")

    else:
        print("dubletter ej tillåtna")

    
def finns(root, value):
    
    
    if root == None:
        return False
    
    elif value == root.value:
        return True

    elif value < root.value:
        return finns(root.left,value)
    
    elif value > root.value:
        return finns(root.right,value)
    
    


def skriv(node):
    if node!=None:
        skriv(node.left)
        print(node.value)
        skriv(node.right)

#_______________________________ANROP_________________________________ANROP___________________________________________ANROP______________________________________________ANROP___________________________________________________________________________________________________________________________________________________________________________________________

# tree = Bintree()
# tree.put("e")
# tree.put("b")
# tree.put("a")
# tree.put("f")

# print("aa" in tree)



















