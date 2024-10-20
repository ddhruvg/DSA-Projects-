from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        self.params = params
        self.elements = 0
        self.table_size = params[-1]
        self.table = [None]*self.table_size
        pass
    def insert(self, x):
        key = x
        flag,idx = self.hash(key)
        if not flag:
            return 
        
        if self.collision_type == "Chain":
            if self.table[idx] == None:
                self.table[idx] = [key]
            else:
                self.table[idx].append(key)
        else:
            self.table[idx] = key
        self.elements += 1          
        
    
    def find(self, key):
        flag,idx = self.hash(key)
        # print(flag,idx)
        
        if flag==False:
            return (True,idx)
        else:
            return (False,idx)
        
    
    def get_slot(self, key):
        
        return self.polynomial_accumulation(key,self.params[0]) % self.table_size
        
    
    def get_load(self):
        return self.elements/self.table_size
        
    
    def __str__(self):
        #considering a hash set 
        if self.collision_type == "Chain":
            ans = ""
            for i in range(self.table_size):
                if self.table[i] is not None:
                    buffer = " ; ".join(self.table[i])
                    ans = ans + buffer + " | "
                else:    
                    ans += "<EMPTY>" + " | "
             
        else:
            ans = ""
            for i in range(self.table_size):
                if self.table[i] is not None:
                    ans = ans + self.table[i] + " | "
                else:    
                    ans += "<EMPTY>" + " | "
                    
        return ans 
    
    def ord_value(self,s):
        if s.lower() == s:
            return ord(s) - 96
        else:
            return ord(s) - 64
        
    def polynomial_accumulation(self,s,z):
        result = self.ord_value(s[len(s)-1])
        for i in range(len(s)-2,-1,-1):
            result = result * z + self.ord_value(s[i])
        return result     
        pass    
    def double_hash(self,s,z2,c2):
        new_hash = c2-self.polynomial_accumulation(s,z2)%c2
        return new_hash
        pass

    def hash(self,key):
        if self.collision_type == "Chain":
            z = self.params[0]
            target = self.polynomial_accumulation(key,z) % self.table_size
            if self.table[target] == None:
                return (True,target)
            else:
                # print(self.table[target])
                for i in range(len(self.table[target])):
                    if self.table[target][i] == key:
                        return (False,target)
            return (True,self.polynomial_accumulation(key,z) % self.table_size)
        
        elif  self.collision_type == "Linear":
            z = self.params[0]
            hash_value = self.polynomial_accumulation(key,z)
            idx = hash_value % self.table_size
            while self.table[idx] != None:
                
                if self.table[idx] == key:
                    # print("######......#####")
                    return (False,idx)
                idx = (idx+1) % self.table_size
                if idx == hash_value % self.table_size:
                    # print(f"...........{self.table}..........")
                    raise Exception("Table is full")
                
            return (True,idx)
        
        else:
            z1 = self.params[0]
            z2 = self.params[1]
            c2 = self.params[2]
                
            
            original_hash = self.polynomial_accumulation(key,z1)
            new_hash = self.double_hash(key,z2,c2)
            for i in range(self.table_size):
                idx = (original_hash + i*new_hash) % self.table_size
                if self.table[idx] == None:
                    return (True,idx)
                if self.table[idx]==key:
                    return (False,idx)
            raise Exception("Table is full")    
            
        pass
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def insert(self, key):
        super().insert(key)
        pass
    
    def find(self, key):
        return super().find(key)[0]
  
    def get_slot(self, key):
        return super().get_slot(key)

   
    
    def get_load(self):
        return super().get_load()

    
    def __str__(self):
        return super().__str__()
        
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        self.value_table = [None]*self.table_size
        pass
    
    def insert(self, x):
        # x = (key, value)
        key = x[0]
        value = x[1]
        insert,idx = super().hash(key)
        if  insert is False:
            return 
        else:
            super().insert(key)
            if self.collision_type == "Chain":
                if self.value_table[idx] == None:
                    self.value_table[idx] = [value]
                else:
                    self.value_table[idx].append(value)
            else:
                self.value_table[idx] = value             
        pass
    
    def find(self, key):
        findings = super().find(key)
        # print(findings)
        if findings[0] == False:
            return None
        else:
            if self.collision_type == "Chain":
                index = 0
                for i in range(len(self.table[findings[1]])):
                    if self.table[findings[1]][i] == key:
                        index = i
                        break
                return self.value_table[findings[1]][index]    
            else:
                return self.value_table[findings[1]]
            
        
    
    def get_slot(self, key):
        return super().get_slot(key)
        
    
    def get_load(self):
        return super().get_load()
        
    
    def __str__(self):
        if self.collision_type == "Chain":
            ans = ""
            for i in range(self.table_size):
                if self.table[i] is not None:
                    for j in range(len(self.table[i])):
                        ans += f" ({self.table[i][j]} , {self.value_table[i][j]}) ;"
                    ans = ans[:-1]
                    ans += " |"
                else:
                    ans += " <EMPTY> |"   
        else:
            ans = ""
            for i in range(self.table_size):
                if self.table[i] is not None:
                    ans += f" ({self.table[i]} , {self.value_table[i]}) ;"
                    ans = ans[:-1]
                    ans += " |"
                else:
                    ans += " <EMPTY> |"
        ans = ans[:-1]            
        return ans                                