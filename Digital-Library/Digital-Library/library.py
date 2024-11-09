import hash_table as ht

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

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.library=[]
        for i in range(len(book_titles)):
            self.library.append([book_titles[i],texts[i]])
        self.library=self.mergeSort(0,len(self.library)-1,self.library,True)
        for i in range(len(book_titles)):
            self.library[i][1]=self.mergeSort(0,len(self.library[i][1])-1,self.library[i][1])

    def merge(self,left,right,books):
        i=0
        j=0
        ans=[]
        while i<len(left) and j<len(right):
            if books:
                if left[i][0]<right[j][0]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
            else:
                if left[i]==right[j]:
                    i+=1
                elif left[i]<right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
        while i<len(left):
            ans.append(left[i])
            i+=1
        while j<len(right):
            ans.append(right[j])
            j+=1
        return ans

    def mergeSort(self,low,high,arr,books=False):
        if low==high:
            return [arr[low]]
        else:
            mid=(low+high)//2
            left=self.mergeSort(low,mid,arr)
            right=self.mergeSort(mid+1,high,arr)
            return self.merge(left,right,books)
        
    
    def search(self,arr,key,books=True):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if books:
                if arr[mid][0]==key:
                    return mid
                elif arr[mid][0]<key:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if arr[mid]==key:
                    return mid
                elif arr[mid]<key:
                    low=mid+1
                else:
                    high=mid-1
        return None

    def distinct_words(self, book_title):
        i=self.search(self.library,book_title)
        if i==None:
            raise Exception("Book not found")
        else:
            return self.library[i][1]
    
    def count_distinct_words(self, book_title):
        i=self.search(self.library,book_title)
        if i==None:
            raise Exception("Book not found")
        else:
            return len(self.library[i][1])
    
    def search_keyword(self, keyword):
        ans=[]
        for i in range(len(self.library)):
            if self.search(self.library[i][1],keyword,False)!=None:
                ans.append(self.library[i][0])
        return ans
    
    def print_books(self):
        for i in range(len(self.library)):
            temp=self.library[i][0]+": "
            for j in self.library[i][1]:
                temp+=j+" | "
            temp=temp[:-3]
            print(temp)
        return

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.library=None
        self.name=name
        self.params=params
        self.books=[]
        if name=="Jobs":
            self.library=ht.HashMap("Chain",params)
        elif name=="Gates":
            self.library=ht.HashMap("Linear",params)
        elif name=="Bezos":
            self.library=ht.HashMap("Double",params)
        else:
            raise Exception("Invalid name")
    
    def add_book(self, book_title, text):
        words=None
        if self.name=="Jobs":
            words=ht.HashSet("Chain",self.params)
        elif self.name=="Gates":
            words=ht.HashSet("Linear",self.params)
        else:
            words=ht.HashSet("Double",self.params)
        for word in text:
            words.insert(word)
        self.library.insert((book_title,words))
        self.books.append(book_title)
        return

    def distinct_words(self, book_title):
        ans=[]
        words=self.library.find(book_title)
        radixSort(words.occupied)
        for i in words.occupied:
            if self.name=="Jobs":
                ans+=words.table[i]
            else:
                ans.append(words.table[i])
        return ans
    
    def count_distinct_words(self, book_title):
        words=self.library.find(book_title)
        return words.n
    
    def search_keyword(self, keyword):
        ans=[]
        for i in self.books:
            words=self.library.find(i)
            if words.find(keyword):
                ans.append(i)
        return ans
    
    def print_books(self):
        if self.name=="Jobs":
            for i in self.library.occupied:
                for j in self.library.table[i]:
                    print(j[0]+": "+j[1].__str__())
        else:
            for i in self.library.occupied:
                print(self.library.table[i][0]+": "+self.library.table[i][1].__str__())