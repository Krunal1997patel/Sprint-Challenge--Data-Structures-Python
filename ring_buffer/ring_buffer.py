from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # LRU type
        # check if i can add items in the node

        if len(self.storage) < self.capacity:
            # if i can add, add it to the tails
            self.storage.add_to_tail(item)
            # make the pointer, point to tail
            self.current = self.storage.tail
            # if the capacity is full
            # the current will be on tail
        elif self.current == self.storage.tail:
            # replace the head with the new item
            self.storage.head.value = item
            # and make the current point to head, the new item that was added
            self.current = self.storage.head
            # if the current is no longer on tail
        else:
            # set the self.head,next to another new iteam
            self.current.next.value = item
            # and move current to next, untail it reach tail again
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed

        # TODO: Your code here

        # check if their is a list of iteams, if not return none
        # loop and add the iteam in the list_buffer_contents, one by one
        list_buffer_contents = []
        node = self.storage.head

        if not node:
            return None
        else:
            while node:
                list_buffer_contents.append(node.value)
                node = node.next

        # retuen that list
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
