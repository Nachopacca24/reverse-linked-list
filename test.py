"""test

"""

from linked_list import Node, LinkedList

node_a=Node('A')
node_b=Node('b')
node_c=Node('c')

ll=LinkedList()
print(ll)

ll.insert_at_end(node_a)
ll.insert_at_end(node_b)
ll.insert_at_end(node_c)

print(ll)

ll.reverse()
print(ll)