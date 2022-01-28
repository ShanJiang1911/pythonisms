class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class LinkedList():
    def __init__(self, values=None):
        self.head = None
        if values:
            for item in reversed(values):
                self.insert(item)

    def __str__(self):
        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"

    def insert(self, value):
        self.head = Node(value, self.head)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        ct = 0
        for item in self:
            ct += 1
        return ct

    def __eq__(self, target):
        return str(self) == str(target)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def __setitem__(self, index, value):
        current = self.head
        ct = 0
        while ct < index:
            current = current.next
            ct += 1
        current.value = value








