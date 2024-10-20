from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size(self.table_size)
        new_params = list(self.params)
        new_params[-1] = new_size
        new_params = tuple(new_params)
        new_hashset = HashSet(self.collision_type, new_params)
        if self.collision_type == "Chain":
            for i in range(len(self.table)):
                if self.table[i] != None:
                    for j in range(len(self.table[i])):
                        new_hashset.insert(self.table[i][j])
        else:
            for i in range(len(self.table)):
                if self.table[i] != None:
                    new_hashset.insert(self.table[i]) 
        self.table_size = new_size
        self.table = new_hashset.table                           
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size(self.table_size)
        new_params = list(self.params)
        new_params[-1] = new_size
        new_params = tuple(new_params)
        new_hashmap = HashMap(self.collision_type,new_params)
        if self.collision_type == "Chain":
            for i in range(len(self.table)):
                if self.table[i] != None:
                    for j in range(len(self.table[i])):
                        new_hashmap.insert((self.table[i][j],self.value_table[i][j]))
        else:
            for i in range(len(self.table)):
                if self.table[i] != None:
                    new_hashmap.insert(self.table[i],self.value_table[i]) 
        self.table_size = new_size
        self.table = new_hashmap.table
        self.value_table = new_hashmap.value_table
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()