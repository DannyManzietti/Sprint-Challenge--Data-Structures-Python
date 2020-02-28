from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if list is at capacity
        # if it is
        if self.capacity == len(self.storage):
            # replace current with new item
            self.current.value = item

            # move to next item in list
            # if current item is tail
            if self.current == self.storage.tail:
                # next is head value
                self.current = self.storage.head
            else:
                self.current = self.current.next
        # not at capacity
        else:
            # add to end storage
            self.storage.add_to_tail(item)
            # if no items
            if len(self.storage) == 1:
                # set to new item
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node is not None:
            # add value to list
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
