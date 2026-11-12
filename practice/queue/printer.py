"""
문제: 프린터
난이도: 레벨 2
출처: 프로그래머스 42587
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587

문제 설명:
대기목록의 맨 앞 문서(J)를 꺼냈을 때, 나머지 대기목록에 J보다 중요도가 높은 문서가
하나라도 있으면 J를 맨 뒤로 보낸다. 없으면 J를 인쇄한다.
priorities(각 문서의 중요도)와 location(내가 요청한 문서의 현재 위치)이 주어질 때,
내 문서가 몇 번째로 인쇄되는지 리턴하라.

제약 조건:
- 현재 대기목록에는 1개 이상 100개 이하의 문서가 있다.
- 중요도는 1 이상 9 이하의 정수이고, 숫자가 클수록 중요하다.
- location은 0 이상 (대기목록 길이 - 1) 이하이다. 맨 앞이 0이다.

예제:
입력: priorities = [2, 1, 3, 2], location = 2
출력: 1

입력: priorities = [1, 1, 9, 1, 1, 1], location = 0
출력: 5
"""

import sys
from collections import deque
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(priorities, location):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(name="프로그래머스 예제 1", input=([2, 1, 3, 2], 2), expected=1),
    TestCase(name="프로그래머스 예제 2", input=([1, 1, 9, 1, 1, 1], 0), expected=5),
    TestCase(name="문서 하나뿐", input=([5], 0), expected=1),
    TestCase(name="전부 같은 중요도", input=([3, 3, 3], 2), expected=3),
    TestCase(name="내 문서가 가장 중요", input=([1, 2, 3, 9], 3), expected=1),
    TestCase(name="내 문서가 가장 덜 중요", input=([9, 8, 7, 1], 3), expected=4),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
