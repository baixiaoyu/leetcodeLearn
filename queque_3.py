# coding=utf-8
from Queue import Queue
import threading

Thread_id = 1
Thread_num = 3


class MyThread(threading.Thread):
    def __init__(self, q):
        global Thread_id
        super(MyThread, self).__init__()
        self.q = q
        self.Thread_id = Thread_id
        Thread_id = Thread_id + 1

    def run(self):
        while True:
            try:
                # 不设置阻塞的话会一直去尝试获取资源
                task = self.q.get(block=True, timeout=1)
            except Exception as e:
                info_e = 'Thread ' + str(self.Thread_id) + ' end'
                print(info_e)
                break
            # 取到数据，开始处理（依据需求加处理代码）
            info_d = "Starting " + str(self.Thread_id)
            print(info_d)
            print(task)
            self.q.task_done()
            info_end = "Ending " + str(self.Thread_id)
            print(info_end)


q_test = Queue(10)

# 向资源池里面放10个数用作测试
for i in range(10):
    q_test.put(i)

# 开Thread_num个线程
for i in range(0, Thread_num):
    worker = MyThread(q_test)
    worker.start()

# 等待所有的队列资源都用完
q_test.join()

print("Exiting Main Thread")
