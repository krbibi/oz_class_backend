import threading
from multiprocessing import Process, Value, Lock

def counter1(snum, cnt) :

    try:
        for i in range(cnt) :
            snum.value += 1
    finally :
        print('done')
def counter2(snum, cnt) :
    try:
        for i in range(cnt) :
            snum.value -= 1
    finally :
        print('done')


if __name__ == '__main__' :

    shared_number = Value('i',0)
    t1 = threading.Thread(target=counter1, args=(shared_number, 10000))
    t1.start()

    t2 = threading.Thread(target=counter2, args=(shared_number, 10000))
    t2.start()

    t1.join()
    t2.join()

    print('finally, number is', shared_number.value)

      # 동시 동작으로 충돌하여 0이 나오지 않았던 14.py 에서 lock을 사용하여 p1 을 동작할때 p2가 동작하지 않고
      # p2가 동작할 때 p1이 동작하지 않게 하여 충동을 없애 0이 나옴