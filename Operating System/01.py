# 인터럽트 예제

import time
import signal

def handler(signum, frame):
    print('키보드 인터럽트 감지')
    print('신호 번호: ', signum)
    print('스택 프레임: ', frame)
    exit()

signal.signal(signal.SIGINT, handler)

while True:
    print('5초 간격으로 출력중...')
    time.sleep(5)