import threading
import os

def func():
    print('안녕, 나는 실험용응로 대충 만들어 본 함수야!')
    print('나의 프로세스 아이디 : ', os.getpid())
    print('스레드 아이디 : ', threading.get_native_id())


if __name__ == '__main__':
    print('기존 프로세스 아이디 : ',os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()