from Queue import Queue
import random
import threading
import time


# Producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("%s: %s is producing %d to the queue!" % (time.ctime(), self.getName(), i))
            self.data.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s: %s finished!" % (time.ctime(), self.getName()))


# Consumer thread
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(), self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s: %s finished!" % (time.ctime(), self.getName()))


# Main thread
def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('All threads terminate!')


if __name__ == '__main__':
    main()




from multiprocessing import Process
from Queue import Queue


# import os

#
# def f():
#     q.put([3, None, 'dasda'])
#     print(q.get())
#
#
# if __name__ == '__main__':
#     q = queue.Queue()
#     p = Process(target=f, )
#     p.start()
#     print(q.get(block=False))
