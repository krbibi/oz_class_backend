import tracemalloc

tracemalloc.start()

# 메모리 할당이 진행되는 작업
data = [b'%d' % num for num in range(1,10001)]
joined_data = b' '.join(data)

current, peak =  tracemalloc.get_traced_memory()
print( f'현재 메모리 사용량 : {current / 10 ** 6} MB')
print( f'최대 메모리 사용량 : {peak / 10 ** 6} MB')

tracemalloc.stop()

traced = tracemalloc.get_tracemalloc_memory()
print(traced / 10 **6)