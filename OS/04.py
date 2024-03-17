import psutil

for proc in psutil.process_iter(): # 전체 프로세스에 대해서 반복 접근할 수 있는 객체
    ps_name = proc.name()

    if "Chrome" in ps_name :
        child = proc.children()
        print(ps_name,proc.status(), proc.parent(), child)

        if child :
            print(f'{ps_name}의 자식 프로세스', child)