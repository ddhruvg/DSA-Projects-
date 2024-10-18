from heap import Heap
def comparison(i,j):
    return i < j

arr = []

heap = Heap(comparison,arr)
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(100)
heap.insert(5)
heap.insert(25)
print(heap.extract())
print(heap.extract())