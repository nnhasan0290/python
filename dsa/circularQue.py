class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.tail