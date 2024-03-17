from multiprocessing import Process
import os

def coke() :
    while True:
        try :
            print( "콜라 프로세스 아이디 : ", os.getpid())
            print( "부모 프로세스 아이디 : ", os.getppid())
        except KeyboardInterrupt :
            break
             
def cider() :
    while True:
        try :
            print( "사이다 프로세스 아이디 : ", os.getpid())
            print( "부모 프로세스 아이디 : ", os.getppid())
        except KeyboardInterrupt :
            break

def juice() :
        while True:
            try :
                print( "사이다 프로세스 아이디 : ", os.getpid())
                print( "부모 프로세스 아이디 : ", os.getppid())
            except KeyboardInterrupt :
                break


if __name__ == '__main__':  # 메인프로세스 동작을 조건문으로 정의
    print('11.py 프로세스 아이디 : ', os.getpid()) # 05.py의 아이디
    child1 = Process(target=coke)
    child1.start()
    child2 = Process(target=cider)
    child2.start()
    child3 = Process(target=juice)
    child3.start()
