
# 문자열 객체를 변수 my_name이 참조했다.
# 레퍼런스 카운트가 1인 상태
my_name = 'Gookhee'

# 레퍼런스 카운트가 2인 상태 
your_name = my_name

my_name = 1
your_name = 2

# 레퍼런스 카운트가 0이 되었다.
# 소멸 대상