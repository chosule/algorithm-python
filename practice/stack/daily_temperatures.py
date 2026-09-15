"""
문제: Daily Temperatures
난이도: 보통
출처: LeetCode 739
링크: https://leetcode.com/problems/daily-temperatures/

문제 설명:
일별 기온 배열 temperatures가 주어질 때, answer[i]는 i번째 날 이후
더 따뜻해지기까지 기다려야 하는 날의 수다. 그런 날이 없으면 0.

제약 조건:
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

예제:
입력: [73,74,75,71,69,72,76,73]
출력: [1,1,4,2,1,1,0,0]
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(temperatures):
    # 하나씩 순회하면서 해당 값보다 큰게 나오면 해당 인덱스 넣기
    result = []

    for index,v in enumerate(temperatures):
        flag = False
        for i in range(index+1,len(temperatures)):
            t = temperatures
            # print("v 뭐나오나?",v)
            # print("value -->",value)
            if t[i] > v and flag == False:
                # print("뒤에께 더 큼 ->", value, "value값 인덱스 ->",i)
                flag = True
                result.append(i-index)
            else:
                pass
                # print("비교기준이 더크거나 같을경우 ->","v->",v,"value->",value)
        
        if flag == False:
            result.append(0)
    
    print("result 결과 ->",result)

test_cases = [
    TestCase(name="기본 케이스", input=([73, 74, 75, 71, 69, 72, 76, 73],),
             expected=[1, 1, 4, 2, 1, 1, 0, 0]),
    TestCase(name="계속 상승", input=([30, 40, 50, 60],), expected=[1, 1, 1, 0]),
    TestCase(name="짧은 상승", input=([30, 60, 90],), expected=[1, 1, 0]),
    TestCase(name="계속 하강", input=([90, 80, 70],), expected=[0, 0, 0]),
    TestCase(name="같은 기온", input=([50, 50, 50],), expected=[0, 0, 0]),
    TestCase(name="원소 하나", input=([30],), expected=[0]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
