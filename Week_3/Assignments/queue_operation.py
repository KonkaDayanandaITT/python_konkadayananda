class Queue:
    def __init__(self):
        self.lst = []

    def enqueue(self, item):
        print(f"Enqueued item is: {item}")
        self.lst.append(item)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(f"Dequeued item is: {self.lst[0]}")
        self.lst.pop(0)

    def isEmpty(self):
        return len(self.lst) == 0


queue_a = Queue()
queue_a.enqueue(10)
queue_a.enqueue(20)
queue_a.enqueue(30)
queue_a.enqueue(40)
queue_a.enqueue(50)
print("Current Queue: ", queue_a.lst)
queue_a.dequeue()
queue_a.dequeue()
print("Updated Queue: ", queue_a.lst)