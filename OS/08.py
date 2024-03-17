# 과제 : 프로세스 생성
# 내 파이썬 프로그램의 이름을 알아보자.
# 1. 실행중인 프로세스에 순차적으로 접근
# 2. 만일 프로세스의 pid가 내 파이썬 프로그램의 pid와 같으면
# 3. 해당 프로세스의 이름을 출력한다.

import psutil
import os

if __name__ == '__main__':
    py08_pid = os.getpid()  #현재 실행중인 08.py의 pid 를 py08_pid 선언

for proc in psutil.process_iter():

    ps_pid = proc.pid # 현재 실행중인 프로세스 pid 나열
    ps_name = proc.name() # 실행중인 프로세스 이름

    if ps_pid == py08_pid :  # 실행중인 pid 와 08.py pid 가 같으면 출력
        print(f'08.py의 pid : {py08_pid}')
        print(f'프로세스 이름 : {ps_name}')
        print(f'프로세스 pid : {ps_pid}')
        

    
    

