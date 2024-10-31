import dynamic_hash_table as ht
map = ht.DynamicHashSet('Linear',(1,11))
map.insert('of')
map.insert("name")
map.insert('a')
map.insert('The')
map.insert('number')

# map.insert('this')
print(map.polynomial_accumulation('The',10)%37)
# print(map.ord_value('T'))
map.insert('contains')
map.insert('book')
map.insert('name')
map.insert("")
print(map.find("You"))

print(map.table) 


