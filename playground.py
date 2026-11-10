# 자유 연습장: 써보고 싶은 코드를 넣고 `python3 playground.py`로 실행
import heapq
from utils.linked_list import from_list
from collections import deque


t = [1,2,3,4,5]
queue = deque(t)

for i in range(len(t)):
  v = t.pop()
  print("지워진값이뭐지?",v)
    


print(t)