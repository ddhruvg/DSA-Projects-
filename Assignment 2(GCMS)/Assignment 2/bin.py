from avl import AVLTree
from node import Node
class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.cargos = None
        self.AVLTree = AVLTree()
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.capacity -= object.size
        
        self.cargos = self.AVLTree.insert(self.cargos,[object.object_id])
        pass

    def remove_object(self, object_id,object_size):
        # Implement logic to remove an object by ID
        self.capacity += object_size
        self.cargos = self.AVLTree.delet(self.cargos,[object_id])
        pass
    
    def show_objects(self):
        ans = []
        root = self.cargos
        def dfs_inorder(root):
            if root==None:
                return 
            dfs_inorder(root.left)
            ans.append(root.key[0])
            dfs_inorder(root.right)
        dfs_inorder(root)
        return ans    
            

