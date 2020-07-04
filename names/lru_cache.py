from doubly_linked_list import DoublyLinkedList

class LRUCache:
    
    def __init__(self, limit):
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.dll = DoublyLinkedList()
        


    def get(self, key):
        if (key in self.storage):
            node = self.storage[key]
            self.dll.move_to_end(node)
            return node.value[1]
        else:
            return None

    
    def set(self, key, value):
        if (key in self.storage):
            # rtn_value = value
            # node = self.storage[key]
            # node.value = (key, value)
            # self.dll.move_to_end(node)
            # return rtn_value
            return key
        else:
            if (self.size == self.limit):
                del self.storage[self.dll.head.value[0]]
                self.dll.remove_from_head()
                self.size -= 1
            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail
            self.size += 1
