from fastapi import APIRouter
import time
import asyncio

router = APIRouter()

@router.get('/slow-async-ping')
def slow_async_ping(): # 동기함수 메인 이벤트 루프를 차단하지않고 다른 요청을 계속 처리
     # async 비동기 함수 이벤트루프가 다른 작업을 수행할 수 없음, 함수 처리되는 동안 서버는 다른 요청처리 x
    time.sleep(10)
    
    return {'msg':'pong'}

@router.get('/fast-async-ping')
async def fast_async_ping():
    await asyncio.sleep(5) 
    # async await 쓸때 들어가는 작업
    # REST API 호출 (무거운 작업 X-> EventLoop를 잡아먹기 때문(성능저하))

    return {'msg':'pong'}

@router.get('/cpu-bound-async')
async def cpu_bound_async():
    result = await cpu_intensive_task()
    return {'msg':result}

def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1)+fibonacci(n-2)

    result = fibonacci(35)
    return result

from concurrent.futures import ProcessPoolExecutor
@router.get('/cpu-bound-task')
async def cpu_bound_task():
    with ProcessPoolExecutor() as excutor:
        result = await asyncio.get_event_loop().run_in_executor(
            excutor, cpu_intensive_task)

    return {'result':result}