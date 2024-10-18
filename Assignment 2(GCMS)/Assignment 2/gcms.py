from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bins_cap = None
        self.objects_tree = None
        self.bins_id = None
        self.AVLTree = AVLTree()
        pass

    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id=bin_id,capacity=capacity)
        key_cap = (new_bin.capacity,new_bin.id,new_bin)
        key_id = (new_bin.id,new_bin.capacity,new_bin)

        self.bins_id=self.AVLTree.insert(self.bins_id,key_id)
        self.bins_cap=self.AVLTree.mul_key_insert(self.bins_cap,key_cap)
        # if self.bins_cap:
        #     print(self.bins_cap.key)
        # else:
        #     print("BT")
        # print("bin added with key ",key_cap)
        pass

    def add_object(self, object_id, size, color):
        # here color will be passed as an integer to the object
        color = color.value
        object = Object(object_id=object_id,size=size,color=color)
        if color <=2:
            if color == 1:
                bin_node = self.AVLTree.compact_fit(node=self.bins_cap,target=size,largest=False)
                if bin_node is None:
                    raise NoBinFoundException
                bin_id = bin_node.key[1]
                bin_capacity = bin_node.key[0]
                bin = bin_node.key[2]

            else:
                bin_node = self.AVLTree.compact_fit(node=self.bins_cap,target=size,largest=True)
                if bin_node is None:
                    raise NoBinFoundException
                bin_id = bin_node.key[1]
                bin_capacity = bin_node.key[0]
                bin = bin_node.key[2]
        else:
            if color == 3:
                bin_node = self.AVLTree.largest_fit(node=self.bins_cap,target=size,largest=False)
                if bin_node is None:
                    raise NoBinFoundException
                bin_id = bin_node.key[1]
                bin_capacity = bin_node.key[0]
                bin = bin_node.key[2]
            else:
                bin_node = self.AVLTree.largest_fit(node=self.bins_cap,target=size,largest=True)
                if bin_node is None:
                    raise NoBinFoundException
                bin_id = bin_node.key[1]
                bin_capacity = bin_node.key[0]
                bin = bin_node.key[2]
        key_cap = (bin_capacity,bin_id,bin)
        self.bins_cap = self.AVLTree.mul_key_delet(self.bins_cap,key_cap)
        bin.add_object(object)
        new_capcity = bin.capacity
        new_key_cap = (new_capcity,bin_id,bin)
        self.bins_cap = self.AVLTree.mul_key_insert(node=self.bins_cap,key=new_key_cap)
        object_key = (object_id,object,bin_id)
        self.objects_tree = self.AVLTree.insert(node=self.objects_tree,key=object_key)
        # print("object added with id ",object_key)
        # handel the below exception
        # raise NoBinFoundException

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        try:
            object_node = self.AVLTree.search(node=self.objects_tree,target=object_id)
            object = object_node.key[1]
            bin_id = object_node.key[2]
            bin_node = self.AVLTree.search(node=self.bins_id,target=bin_id)
            bin = bin_node.key[2]
            bin_key = (bin.capacity,bin.id,bin)
            self.bins_cap = self.AVLTree.mul_key_delet(node=self.bins_cap,key=bin_key)
            bin.remove_object(object_id=object_id,object_size = object.size)
            new_bin_key = (bin.capacity,bin.id,bin)
            self.bins_cap = self.AVLTree.mul_key_insert(node=self.bins_cap,key=new_bin_key)
            self.objects_tree = self.AVLTree.delet(node=self.objects_tree,key =(object.object_id,object,bin))
            pass
        except:
            return None

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bin_node = self.AVLTree.search(self.bins_id,bin_id)
        bin = bin_node.key[2]
        capacity = bin_node.key[1]
        bin_id = bin_node.key[0]
        return (bin.capacity,bin.show_objects())
        # return (bin.capacity,bin.cargos)
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        try:
            object_node = self.AVLTree.search(node=self.objects_tree,target = object_id)
            bin_id = object_node.key[2]
            return bin_id
        except:
            return None
