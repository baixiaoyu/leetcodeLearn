# coding=utf-8
from Queue import Queue
import threading

# 要开启 的 线程 数
num_worker_threads = 3
source = [100, 200, 300, 400, 500, 600, 700, 800, 900]


def do_work(*args):
    info = '[ thread id {0}]:{1}'.format(args[0], args[1])
    print(info)


def worker(t_id):
    while True:
        item = q.get()
        if item is None:
            break
        do_work(t_id, item)
        q.task_done()


q = Queue()
threads = []
for index in range(num_worker_threads):
    t = threading.Thread(target=worker, args=(index,))
    t.start()
    threads.append(t)

for item in source:
    q.put(item)

# block until all tasks are done, 队列所有的内容都被处理完成后，才执行下面的stop workers方法
q.join()

#stop workers
for i in range(num_worker_threads):
    q.put(None)
# for t in threads:
#     t.join()
