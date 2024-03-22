# 파일 경로를 문자열이 아닌 객체로 다루기

import os
import pathlib

for p in pathlib.Path.cwd().glob('*.txt') :
    new_p = os.path.join(p.parent, p.name)
    print(new_p)