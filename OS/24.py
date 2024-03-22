# 팡리 관련 예외는 운영체제와 관계가 있다!

try :
    f = open('none.txt','r')
    print(f.read())
    f.close()
except FileNotFoundError as e :
    print(e)
    print(issubclass(FileNotFoundError, OSError))