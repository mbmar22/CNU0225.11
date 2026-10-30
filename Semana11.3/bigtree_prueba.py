from bigtree import Node

root = Node("a", age = 90)
b = Node("b", age = 65, parent = root)
c = Node("c", age = 65, parent = root)

root.show(attr_list=["age"])