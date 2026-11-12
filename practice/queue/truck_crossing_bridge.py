"""
문제: 다리를 지나는 트럭
난이도: 레벨 2
출처: 프로그래머스 42583
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583

문제 설명:
트럭 여러 대가 일차선 다리를 정해진 순서대로 건넌다. 다리에는 bridge_length대까지
올라갈 수 있고, 다리 위 트럭 무게의 합은 weight 이하여야 한다. 트럭은 다리에 오른 뒤
bridge_length초가 지나야 다리를 완전히 건넌다(1초에 길이 1만큼 이동).
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 리턴하라.

제약 조건:
- bridge_length는 1 이상 10,000 이하
- weight는 1 이상 10,000 이하
- truck_weights의 길이는 1 이상 10,000 이하이고, 각 트럭 무게는 1 이상 weight 이하

예제:
입력: bridge_length = 2, weight = 10, truck_weights = [7, 4, 5, 6]
출력: 8

입력: bridge_length = 100, weight = 100, truck_weights = [10]
출력: 101
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


def solution(bridge_length, weight, truck_weights):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(name="프로그래머스 예제 1", input=(2, 10, [7, 4, 5, 6]), expected=8),
    TestCase(name="프로그래머스 예제 2", input=(100, 100, [10]), expected=101),
    TestCase(name="프로그래머스 예제 3", input=(100, 100, [10] * 10), expected=110),
    TestCase(name="다리 길이 1", input=(1, 5, [5, 5, 5]), expected=4),
    TestCase(name="무게 제한 때문에 한 대씩", input=(3, 5, [5, 5]), expected=7),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
