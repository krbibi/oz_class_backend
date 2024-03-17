from multiprocessing import Process
import os

def func() :
    print('안녕, 나는 실험용으로 대충 만들어 본 함수야!')
    print('나의 프로세스 아이디 : ', os.getpid()) 
    print('나의 부모 프로세스 아이디 : ', os.getppid())  # ppid 부모프로세스 id 

if __name__ == '__main__':  # 메인프로세스 동작을 조건문으로 정의
    print('05.py 프로세스 아이디 : ', os.getpid()) # 05.py의 아이디
    child = Process(target=func).start() 


    # 즉 05.py에서 Process 를 불러와 함수를 만드니 05.py가 부모 그리고 Process가 하위
    # func 는 하위 프로세스를 불러와 만든 함수임, 즉 pid 는 하위 프로세스가 됨

    # if 에서 메인 프로세스를 불러왔고 pid는 05.py의 프로세스를 불러오는것임