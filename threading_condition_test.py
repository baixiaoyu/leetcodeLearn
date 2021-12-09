# coding=utf-8
import threading

con = threading.Condition()


def job1():
    con.acquire()
    print("JOB1：床前明月光")
    con.notify()  # 唤醒正在等待(wait)的线程

    con.wait()  # 等待对方回应消息，使用wait阻塞线程，等待对方通过notify唤醒本线程
    print("JOB1：举头看明月")
    con.notify()  # 唤醒对方

    con.release()


def job2():
    con.acquire()

    con.wait()
    print("JOB2:疑似地上桑")
    con.notify()
    con.wait()
    print("JOB2:低头思故乡")
    con.notify()

    con.release()


def main():
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)

    t2.start()  # 此处注意顺序，先t2,否则双方都处于wait状态，程序卡死
    t1.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

