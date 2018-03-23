class Queue(object):

    class _Node(object):

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
            
    def __init__(self):
        self.size = 0
        self.__header = self._Node(None)
        self.__trailer = self._Node(None)
        self.__header.prev = self.__trailer
        self.__trailer.next = self.__header

    def __str__(self):
        if self.size == 0:
            return "[ ]"
        current = self.__header
        string = "[ "
        for _ in range(self.size - 1):
            current = current.prev
            string += (str(current.data) + ", ")
        current = current.prev
        string += (str(current.data) + " ]")
        return string 

    def __len__(self):
        return self.size

    def push(self, data):
        new_node = self._Node(data)
        new_node.prev = self.__trailer
        new_node.next = self.__trailer.next
        self.__trailer.next.prev = new_node
        self.__trailer.next = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError
        ret_data = self.__header.prev.data
        self.__header.prev.prev.next = self.__header
        self.__header.prev = self.__header.prev.prev
        self.size -= 1
        return ret_data

    def peek(self):
        if self.size == 0:
            raise ValueError
        return self.__header.prev.data
        

def main():
    queue = Queue()
    for i in range(5):
        queue.push(i)

    print(queue)
    
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

if __name__ == '__main__':
    main()
