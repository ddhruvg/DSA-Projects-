from prime_generator import get_next_size

def radixSort(arr):
    def countingSort(arr,exp):
        ans=[[] for i in range(10)]
        for i in arr:
            ans[(i//exp)%10].append(i)
        arr.clear()
        for i in ans:
            arr+=i
        return
    max1=max(arr)
    exp=1
    while max1//exp>0:
        countingSort(arr,exp)
        exp*=10
    return arr

#TODO check the use of super() and self
class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type=collision_type
        self.params=params
        self.n=0
        if collision_type=="Chain" or collision_type=="Linear":
            self.size=params[1]
        else:
            self.size=params[3]
        self.table=[None]*self.size
    
    def hash1(self,key,z1):
        position=0
        power=0
        for c in key:
            if ord(c)>96:
                position+=(ord(c)-ord('a'))*pow(z1,power)
            else:
                position+=(ord(c)-ord('A')+26)*pow(z1,power)
            power+=1
        return position%self.size

    def hash2(self,key,z2,c1):
        position=0
        power=0
        for c in key:
            if ord(c)>96:
                position+=(ord(c)-ord('a'))*pow(z2,power)
            else:
                position+=(ord(c)-ord('A')+26)*pow(z2,power)
            power+=1
        return c1-(position%c1)

    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        return self.hash1(key,self.params[0])
    
    def get_load(self):
        pass
    
    def __str__(self):
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
        self.occupied=[]

    def insert(self, key):
        if len(self.occupied)==self.size:
            raise Exception("Table is Full")
        position=super().hash1(key,self.params[0])
        if self.table[position]==None:
            if self.collision_type=="Chain":
                self.table[position]=[key]
            else:
                self.table[position]=key
            self.occupied.append(position)
        else:
            if self.collision_type=="Chain":
                for i in self.table[position]:
                    if i==key:
                        return
                self.table[position].append(key)
            elif self.collision_type=="Linear":
                while self.table[position]!=None:
                    if self.table[position]==key:
                        return
                    position+=1
                    position=position%self.size
                self.table[position]=key
                self.occupied.append(position)
            elif self.collision_type=="Double":
                position2=super().hash2(key,self.params[1],self.params[2])
                for i in range(self.size):
                    temp=(position+i*position2)%self.size
                    if self.table[temp]==key:
                        return
                    elif self.table[temp]==None:
                        self.table[temp]=key
                        self.occupied.append(temp)
                        break
        self.n+=1

#TODO the find for linear chaining can run infite time so check this code while debugging
    def find(self, key):
        position=super().hash1(key,self.params[0])
        if self.table[position]==key:
            return True
        if self.collision_type=="Chain":
            if self.table[position] and key in self.table[position]:
                return True
        elif self.collision_type=="Linear":
            temp=position
            while self.table[position]!=None:
                if self.table[position]==key:
                    return True
                position+=1
                if position==temp:
                    return False
                position=position%self.size
        elif self.collision_type=="Double":
            position2=super().hash2(key,self.params[1],self.params[2])
            for i in range(self.size):
                if self.table[(position+i*position2)%self.size]==key:
                    return True
        return False
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return self.n/self.size
    
    def __str__(self):
        ans=""
        if self.collision_type=="Chain":
            for i in range(self.size):
                if self.table[i]!=None:
                    for j in self.table[i]:
                        ans+=j+" ; "
                    ans=ans[:-3]
                else:
                    ans+="<EMPTY>"
                ans+=" | "
            ans=ans[:-3]
        else:
            for i in range(self.size):
                if self.table[i]!=None:
                    ans+=self.table[i]
                else:
                    ans+="<EMPTY>"
                ans+=" | "
            ans=ans[:-3]
        return ans

    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        self.occupied=[]
    
    def insert(self, x):
        # x = (key, value)
        if len(self.occupied)==self.size:
            raise Exception("Table is Full")
        key, value = x
        position=super().hash1(key,self.params[0])
        if self.table[position]==None:
            if self.collision_type=="Chain":
                self.table[position]=[(key,value)]
            else:
                self.table[position]=(key,value)
            self.occupied.append(position)
        else:
            if self.collision_type=="Chain":
                for i in self.table[position]:
                    if i[0]==key:
                        i[1]=value
                        return
                self.table[position].append((key,value))
            elif self.collision_type=="Linear":
                while self.table[position]!=None:
                    if self.table[position][0]==key:
                        self.table[position]=(key,value)
                        return
                    position+=1
                    position=position%self.size
                self.table[position]=(key,value)
                self.occupied.append(position)
            elif self.collision_type=="Double":
                position2=super().hash2(key,self.params[1],self.params[2])
                for i in range(self.size):
                    temp=(position+i*position2)%self.size
                    if self.table[temp]==None:
                        self.table[temp]=(key,value)
                        self.occupied.append(temp)
                        break
                    elif self.table[temp][0]==key:
                        self.table[temp]=(key,value)
                        return
        self.n+=1
        return
    
    def find(self, key):
        position=super().hash1(key,self.params[0])
        if self.table[position]!=None and self.table[position][0]==key:
            return self.table[position][1]
        if self.collision_type=="Chain":
            for i in self.table[position]:
                if i[0]==key:
                    return i[1]
        elif self.collision_type=="Linear":
            while self.table[position]!=None:
                if self.table[position][0]==key:
                    return self.table[position][1]
                position+=1
                position=position%self.size
        elif self.collision_type=="Double":
            position2=super().hash2(key,self.params[1],self.params[2])
            for i in range(self.size):
                if self.table[(position+i*position2)%self.size]!=None and self.table[(position+i*position2)%self.size][0]==key:
                    return self.table[(position+i*position2)%self.size][1]
        return None
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return self.n/self.size
    
    def __str__(self):
        radixSort(self.occupied)
        ans=""
        if self.collision_type=="Chain":
            for i in self.occupied:
                for j in self.table[i]:
                    ans+=j[0]+": "+j[1].__str__()+" ; "
                ans=ans[:-3]
                ans+=" | "
        else:
            for i in self.occupied:
                ans+=self.table[i][0]+": "+self.table[i][1].__str__()+" | "
        ans=ans[:-3]
        return ans