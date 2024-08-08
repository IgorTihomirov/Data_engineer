class Node:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


node_last_last = Node(value='Точно последний элемент')
node_last = Node(value='Последний элемент', next_item=node_last_last)
node_1 = Node(value='Второй элемент за головой', next_item=node_last)
node_middle = Node(value='Первый элемент за головой', next_item=node_1)
node_head = Node(value='Голова', next_item=node_middle)

temp_node = node_head
while temp_node is not None:
    print(temp_node.value)
    temp_node = temp_node.next_item
