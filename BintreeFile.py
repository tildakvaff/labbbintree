class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "noden är " + str(self.value) + ", left är " +str(self.left)+", right är "+str(self.right)


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
        


def putta(newvalue, root):
    node = root
    

    if newvalue < node.value and root.left == None:
        Node(newvalue)
        print("a")
            
    elif newvalue < node.value and root.left != None:
        putta(newvalue, node.left)
        print("b")

    elif newvalue > node.value and root.right == None:
        node = Node(newvalue)
        print("c")
    
    elif newvalue > node.value and root.right != None:
        putta(newvalue, node.right)
        print("d")

    else:
        print("dubletter ej tillåtna")




def finns(p,value):     




#_______________________________ANROP_________________________________ANROP___________________________________________ANROP______________________________________________ANROP___________________________________________________________________________________________________________________________________________________________________________________________

tree = Bintree()
tree.put("a")
tree.put("e")





print(tree.__contains__("e"))










