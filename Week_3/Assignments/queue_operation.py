class Queue:
    def __init__(self):
        self._lst = []

    def enqueue(self, item):
        print(f"Enqueued item is: {item}")
        self._lst.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        return self._lst.pop(0)

    def is_empty(self):
        return len(self._lst) == 0


queue_a = Queue()
queue_a.enqueue(10)
queue_a.enqueue(20)
queue_a.enqueue(30)
queue_a.enqueue(40)
queue_a.enqueue(50)
print("Current Queue: ", queue_a._lst)
print("Dequeued item is: ", queue_a.dequeue())
print("Dequeued item is: ", queue_a.dequeue())
print("Updated Queue: ", queue_a._lst)