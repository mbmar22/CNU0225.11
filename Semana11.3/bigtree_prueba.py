from bigtree import Node

root = Node("a", age = 90)
b = Node("b", age = 65, parend = root)
c = Node("c", age = 65, parend = root)

root.show(attr_list=["age"])