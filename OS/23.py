# 기본적인 파일 입출력 예제

with open('number_one.txt','w') as f :
    f.write('one!')

with open('number_two.txt','w') as f :
    f.write('two!')

with open('number_three.txt','w') as f :
    f.write('three!')

with open('number_four.txt','w') as f :
    f.write('four!')

import glob  # 파일네임의 패턴을 이용해 한꺼번에 접근 하는 모듈

for filename in glob.glob("*.txt", recursive=True) : #recursive 
    print(filename)

import fileinput # 
with fileinput.input(glob.glob('*.txt')) as fi :
    for line in fi :
        print(line)


import fnmatch
import os

for filename in os.listdir('.') :
    if fnmatch.fnmatch(filename, "??????_*.txt") :
        print(filename)
