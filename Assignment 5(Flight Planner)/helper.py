class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, init_array,comparison):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        # Write your code here
        self.compariosn_function = comparison
        self.heap = init_array
        self.heapify()
        pass
    def left_child(self,i):
        index = 2*i+1
        return index
        
    def right_child(self,i):
        index = 2*i+2
        
        return index
        
    def parent(self,i):
        return (i-1)//2 
          
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def upheap(self,idx):
        parent_idx = self.parent(idx)
        if idx >0 and self.compariosn_function(self.heap[idx],self.heap[parent_idx]):
            self.swap(idx,parent_idx)
            self.upheap(parent_idx)

    def downheap(self,idx):
        left_child_idx = self.left_child(idx)
        right_child_idx = self.right_child(idx)
        smallest = idx
        if left_child_idx < len(self.heap) and self.compariosn_function(self.heap[left_child_idx],self.heap[smallest]):
            smallest = left_child_idx
        if right_child_idx < len(self.heap) and self.compariosn_function(self.heap[right_child_idx],self.heap[smallest]):
            smallest = right_child_idx
        if smallest != idx:
            self.swap(idx,smallest)
            self.downheap(smallest)
        return     
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.heap.append(value)
        self.upheap(len(self.heap)-1)

        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        
        if not self.heap:
            return None
    
        if len(self.heap) == 1:
            return self.heap.pop()
        
        self.swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self.downheap(0)
        
        return min_value  

    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if self.heap:
            return self.heap[0]
        return None
        # Write your code here
    
    def heapify(self):
        # self.heap = arr[:]
        for i in range(len(self.heap)//2-1,-1,-1):
            self.downheap(i)
    def is_empty(self):
        return len(self.heap) == 0       
        
class Queue:
    def __init__(self):
        self.queue = []
        self.index = 0 

    def append(self, value):
        self.queue.append(value)
    def pop(self):
        if self.index <len(self.queue):
            ans = self.queue[self.index]
            self.index+=1
            return ans
        return None
    def is_empty(self):
        return self.index == len(self.queue)
    def top(self):
        if self.index < len(self.queue):
            return self.queue[self.index]
        return None               
    
def comparison(a,b):
    return a[0]<b[0]    