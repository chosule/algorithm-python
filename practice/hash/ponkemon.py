"""
문제: 폰켓몬
난이도: 레벨 1
출처: 프로그래머스 1845
링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845

문제 설명:
연구실에 있는 폰켓몬 N마리 중 N/2마리를 가져갈 수 있다. 같은 종류의 폰켓몬은
같은 번호를 가진다. 가져갈 N/2마리의 종류(번호) 수가 최대가 되도록 고를 때,
그 최대 종류 수를 리턴하라.

제약 조건:
- nums의 길이 N은 1 이상 10,000 이하의 자연수이고, 항상 짝수
- 폰켓몬 종류 번호는 1 이상 200,000 이하의 자연수

예제:
입력: nums = [3, 1, 2, 3]
출력: 2  (4마리 중 2마리를 고름. 종류는 1, 2, 3 세 가지지만 2마리만 고를 수 있음)

입력: nums = [3, 3, 3, 2, 2, 4]
출력: 3
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402
from collections import Counter
import math

def solution(nums):
    count = Counter(nums)
    print("count?",count)
    get = math.ceil(len(nums)/2)
    print("몇마리겟할수있음?",get)

    countLen = len(count.values())

    print("값의 총합",sum(count.values()))
    # if get < countLen:
    #     return countLen -1
    # else:
    #     return countLen



test_cases = [
    TestCase(name="프로그래머스 예제 1", input=([3, 1, 2, 3],), expected=2),
    TestCase(name="프로그래머스 예제 2", input=([3, 3, 3, 2, 2, 4],), expected=3),
    TestCase(name="프로그래머스 예제 3", input=([3, 3, 3, 2, 2, 2],), expected=2),
    TestCase(name="전부 같은 종류", input=([7, 7, 7, 7],), expected=1),
    TestCase(name="전부 다른 종류", input=([1, 2, 3, 4, 5, 6],), expected=3),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
