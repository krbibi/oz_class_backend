from multiprocessing import Process
import os

def func() :
    print('안녕, 나는 실험용으로 대충 만들어 본 함수야!')
    print('나의 프로세스 아이디 : ', os.getpid()) # pid 하위프로세스 id
    print('나의 부모 프로세스 아이디 : ', os.getppid())  # ppid 부모프로세스 id

if __name__ == '__main__':  # 메인프로세스 동작을 조건문으로 정의
    print('06.py 프로세스 아이디 : ', os.getpid()) # 05.py의 pid
    child1 = Process(target=func)
    child1.start()
    child2 = Process(target=func)
    child2.start()
    child3 = Process(target=func)
    child3.start()