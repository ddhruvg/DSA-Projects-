import hash_table as ht
import dynamic_hash_table as dht

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
        self.book_titles = book_titles
        self.texts = texts
        self.library = []
        for i in range(len(self.book_titles)):
            self.library.append([self.book_titles[i],self.texts[i]])

        def merge_sort(arr):
            
            if len(arr) <= 1:
                return arr

            
            mid = len(arr) // 2

            
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            
            return merge(left, right)

        def merge(left, right):
            
            sorted_array = []
            i = j = 0

            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    
                    if not sorted_array or sorted_array[-1] != left[i]:
                        sorted_array.append(left[i])
                    i += 1
                elif left[i] > right[j]:
                    
                    if not sorted_array or sorted_array[-1] != right[j]:
                        sorted_array.append(right[j])
                    j += 1
                else:
                    
                    if not sorted_array or sorted_array[-1] != left[i]:
                        sorted_array.append(left[i])
                    i += 1
                    j += 1

            
            while i < len(left):
                if not sorted_array or sorted_array[-1] != left[i]:
                    sorted_array.append(left[i])
                i += 1

            
            while j < len(right):
                if not sorted_array or sorted_array[-1] != right[j]:
                    sorted_array.append(right[j])
                j += 1

            return sorted_array

        self.library = merge_sort(self.library)    
        for i in range(len(self.library)):
            self.library[i][1] = merge_sort(self.library[i][1])


    
    def distinct_words(self, book_title):

        idx = self.binary_search(self.library,book_title,True)
        distinct_words = self.library[idx][1][:]
       
        return distinct_words
    
    def count_distinct_words(self, book_title):

        idx = self.binary_search(self.library,book_title,True)
        distint_words = len(self.library[idx][1])
        return distint_words
     
    
    def search_keyword(self, keyword):

        ans = []
        for i in range(len(self.library)):
            if self.binary_search(self.library[i][1],keyword) != -1:
                ans.append(self.library[i][0])
        return ans         
        
    
    def print_books(self):
        for i in range(len(self.library)):
            ans = f"{self.library[i][0]}: "
            ans += " | ".join(self.library[i][1])
            print(ans)

    def binary_search(self,arr,x,flag=False):
        low = 0
        high = len(arr) - 1
        mid = 0
        if flag:
            while low <= high:
                mid = (high + low) // 2
                if arr[mid][0] < x:
                    low = mid + 1
                elif arr[mid][0] > x:
                    high = mid - 1
                else:
                    return mid
        else:
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return mid

        return -1        
        

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
        if name == "Jobs":
            self.collision_type = "Chain"
        elif name == "Gates":
            self.collision_type = "Linear"
        else:
            self.collision_type = "Double"    

        self.book_map = ht.HashMap(self.collision_type, params)
        self.params = params
        self.added_books = []

        pass
    
    def add_book(self, book_title, text):
        key = book_title
        value = ht.HashSet(self.collision_type,self.params)

        for word in text:
            value.insert(word)
            
            
        self.book_map.insert((key,value))  
        
        self.added_books.append(book_title) 
        
        pass
    
    def distinct_words(self, book_title):

        value_set = self.book_map.find(book_title)
        ans = []
        if self.collision_type !="Chain":
            for i in range(len(value_set.table)):
                if value_set.table[i] is not None:
                    ans.append(value_set.table[i])
        else:
            for i in range(len(value_set.table)):
                if value_set.table[i] is not None:
                    for key in value_set.table[i]:
                        ans.append(key)
        
        return ans
        
    
    def count_distinct_words(self, book_title):
        value_set = self.book_map.find(book_title)
        load = value_set.get_load()
        distint_words = load * value_set.table_size
        return int(distint_words) 
        
    
    def search_keyword(self, keyword):
        ans = []
        for book in self.added_books:
            value_set = self.book_map.find(book)
            if value_set.find(keyword):
                ans.append(book)
        return ans                      
        
        
    
    def print_books(self):
        

        for book in self.added_books:
            ans =""
            if book is not None:

                ans = book + ": "
                value_set = self.book_map.find(book)

                if self.collision_type != "Chain":
                    ans1 = []
                    for key in value_set.table:
                        if key is not None:
                            ans1.append(key)
                        else:
                            ans1.append("<EMPTY>")
                else:
                    ans1 = []
                    for key in value_set.table:
                        if key is not None:
                            ans1.append(" ; ".join(key))
                        else:
                            ans1.append("<EMPTY>")
                print(ans + " | ".join(ans1))

        