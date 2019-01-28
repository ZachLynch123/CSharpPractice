# Linked List example

# Node only has one value and is a single linked list
# Since there is only a 'next' value
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count
    
    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        # TODO: find the first item with given value
        item = self.head
        while (item != None):
            if (item.get_data() == val):
                return item
            else:
                item = item.get_next()

        return None
    
    def deleteAt(self, index):
        # TODO: delete an item at an index
        if index > self.count - 1:
            return
        if index == 0:
            self.head = self.head.get_next()
        else: 
            tempIndex = 0
            node = self.head
            while (tempIndex < index - 1):
                node = node.get_next()
                tempIndex += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    # Dumps content of list
    def dump_list(self):
        tempNode = self.head
        while (tempNode != None):
            print("Node: ", tempNode.get_data())
            tempNode = tempNode.get_next()


# create a linked list and insert items
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
itemList.dump_list()

# try it out

print("Item count: ", itemList.get_count())
print("Finding item: ", itemList.find(13))
print("Finding item: ", itemList.find(445))

itemList.deleteAt(3)
itemList.dump_list()
print("Item count: ", itemList.get_count())
