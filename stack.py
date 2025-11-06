class Node:
    def __init__(self, data, priority=None):
        self.data = data
        self.priority = priority
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def leng(self):
        cnt = 0
        current = self.top

        while current is not None:
            cnt+=1
            current = current.next

        return cnt
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.data
    
    def display(self):
        if self.is_empty():
            print("Стек пуст")
            return
        
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("""\n  |
  V
""".join(elements))
    
    def dop(self, nazv):
        if self.is_empty():
            raise IndexError("стек пуст")
        
        if self.top.data == nazv:
            self.top = self.top.next
            return 
        current  = self.top

        while current.next is not None:
            if current.next.data == nazv:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError(f"Элемент с данными '{nazv}' не найден")