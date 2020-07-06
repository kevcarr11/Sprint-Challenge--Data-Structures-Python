class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.buffer = []

    def append(self, item):
        # check if the buffer is currently full
        if len(self.buffer) == self.capacity:
            # overwright the current head of buffer
            self.buffer[self.head] = item
            '''move the head to the next item
                each time we append
                loop back to the begining when we reach the end'''
            self.head = (self.head + 1) % self.capacity
        else:
            # if not full just add item to the end of buffer
            self.buffer.append(item)
            

    def get(self):
        return self.buffer
