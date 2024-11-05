import hash_table as ht
map = ht.HashSet('Chain',(1,11))
map.insert('of')
map.insert("name")
map.insert('a')
map.insert('The')
map.insert('number')

map.insert('this')
print(map.polynomial_accumulation('The',10)%37)
# print(map.ord_value('T'))
map.insert('contains')
map.insert('book')
map.insert('slice')
map.insert('happy')
map.insert('sad')
map.insert('good')

print(map) 


