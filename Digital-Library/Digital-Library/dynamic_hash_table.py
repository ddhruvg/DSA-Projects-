from hash_table import HashSet, HashMap
from prime_generator import get_next_size
from library import radixSort

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        newSize=get_next_size()
        new_set=DynamicHashSet()
        self.size=get_next_size()
        new_table=[None]*self.size
        temp=[]
        if self.collision_type=="Chain":
            for i in range(len(self.table)):
                if self.table[i]!=None:
                    for j in self.table[i]:
                        position=self.hash1(j,self.params[0])
                        if new_table[position]==None:
                            temp.append(position)
                            new_table[position]=[j]
                        else:
                            new_table[position].append(j)
        else:
            for i in range(len(self.table)):
                if self.table[i]!=None:
                    position=self.hash1(self.table[i],self.params[0])
                    if new_table[position]==None:
                        new_table[position]=self.table[i]
                        temp.append(position)
                    else:
                        if self.collision_type=="Linear":
                            while new_table[position]!=None:
                                position+=1
                                position=position%self.size
                            new_table[position]=self.table[i]
                            temp.append(position)
                        elif self.collision_type=="Double":
                            position2=self.hash2(self.table[i],self.params[1],self.params[2])
                            for j in range(self.size):
                                if new_table[(position+j*position2)%self.size]==None:
                                    new_table[(position+j*position2)%self.size]=self.table[i]
                                    temp.append((position+j*position2)%self.size)
                                    break
        self.table=new_table
        self.occupied=temp
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        self.size=get_next_size()
        new_table=[None]*self.size   
        temp=[]
        if self.collision_type=="Chain":
            for i in range(len(self.table)):
                if self.table[i]!=None:
                    for j in self.table[i]:
                        position=self.hash1(j[0],self.params[0])
                        if new_table[position]==None:
                            new_table[position]=[j]
                            temp.append(position)
                        else:
                            new_table[position].append(j)
        else:
            for i in range(len(self.table)):
                if self.table[i]!=None:
                    position=self.hash1(self.table[i][0],self.params[0])
                    if new_table[position]==None:
                        new_table[position]=self.table[i]
                        temp.append(position)
                    else:
                        if self.collision_type=="Linear":
                            while new_table[position]!=None:
                                position+=1
                                position=position%self.size
                            new_table[position]=self.table[i]
                            temp.append(position)
                        elif self.collision_type=="Double":
                            position2=self.hash2(self.table[i][0],self.params[1],self.params[2])
                            for j in range(len(new_table)):
                                if new_table[(position+j*position2)%self.size]==None:
                                    new_table[(position+j*position2)%self.size]=self.table[i]
                                    temp.append((position+j*position2)%self.size)
                                    break

        self.table=new_table
        self.occupied=temp
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()