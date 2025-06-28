# BINARY SEARCH TREE:
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
#INSERTION
    def insert(self,root,key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left=self.insert(root.left,key)   #recursive calling function
        else:
            root.right=self.insert(root.right,key)
        return root
# INORDER TRAVERSAL(Sorted order):
    def inorder(self,root):   #Inorder Traversal=left-root-right
        if root:
            self.inorder(root.left)      #recursive
            print(root.key,end=' ')
            self.inorder(root.right)

# SEARCH:
    def search(self,root,key):
        if root is None or root.key==key:
            return root
        if key < root.key:
            return self.search(root.left,key)  
        return self.search(root.right,key)
   
# Find minimum value node
    def minvalueNode(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current
   
# DELETION
    def delete(self,root,key):
        if root is None:
            return root
        if key < root.key:
            root.left=self.delete(root.left,key)   #recursive calling function
        elif key > root.key:
            root.right=self.delete(root.right,key)
        else:
            #Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp=self.minvalueNode(root.right)
            root.key=temp.key
            root.right=self.delete(root.right,temp.key)
        return root
    
#test the BST Implementation    
tree=BST()
keys=[50,30,70,20,40,60,80]
for key in keys:
    tree.root=tree.insert(tree.root,key)
print("Inorder transversal of the BST:")
tree.inorder(tree.root)
#search for a key:
key=60
found=tree.search(tree.root,key) 
print(f"\n\nSearch for {key}:",'Found' if found else "Not Found")

# Delete a node:
tree.root=tree.delete(tree.root,20)
print("\nInorder after deleting 20:")
tree.inorder(tree.root)       

tree.root=tree.delete(tree.root,30)
print("\nInorder after deleting 30:")
tree.inorder(tree.root)       

tree.root=tree.delete(tree.root,50)
print("\nInorder after deleting 50:")
tree.inorder(tree.root)       