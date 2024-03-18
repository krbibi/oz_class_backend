from multiprocessing import Process, Value, Lock

def counter1(snum, cnt, lock) :
    lock.acquire()
    try:
        for i in range(cnt) :
            snum.value += 1
    finally :
        lock.release()

def counter2(snum, cnt, lock) :
    lock.acquire()
    try:
        for i in range(cnt) :
            snum.value -= 1
    finally :
        lock.release()


if __name__ == '__main__' :

    lock = Lock()
    shared_number = Value('i',0)
    p1 = Process(target=counter1, args=(shared_number, 5000, lock))
    p1.start()

    p2 = Process(target=counter2, args=(shared_number, 5000, lock))
    p2.start()

    p1.join()
    p2.join()

    print('finally, number is', shared_number.value)

      # 동시 동작으로 충돌하여 0이 나오지 않았던 14.py 에서 lock을 사용하여 p1 을 동작할때 p2가 동작하지 않고
      # p2가 동작할 때 p1이 동작하지 않게 하여 충동을 없애 0이 나옴