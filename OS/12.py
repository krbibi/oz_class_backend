from multiprocessing import Process,Pipe
import os


def send(conn):
    print(f'{os.getpid()}가 {os.getppid()}에게 데이터를 보낸다')
    conn.send('hello parent!')
    conn.close()

if __name__ == '__main__' :
    praent,child = Pipe()
    p = Process(target=send,args=(child,))
    p.start()
    print('기존 프로세스 아이디 : ',os.getpid())
    print(praent.recv())  # hello parent 는 여기서 출력되는것
    p.join()
