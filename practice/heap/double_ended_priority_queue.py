"""
문제: 이중우선순위큐
난이도: 레벨 3
출처: 프로그래머스 42628
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42628

문제 설명:
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조이다.
- "I 숫자": 큐에 숫자를 삽입한다.
- "D 1": 큐에서 최댓값을 삭제한다.
- "D -1": 큐에서 최솟값을 삭제한다.
operations가 주어질 때, 모든 연산을 처리한 후 큐가 비어 있으면 [0, 0],
비어 있지 않으면 [최댓값, 최솟값]을 리턴하라. 빈 큐에 삭제 연산이 오면 무시한다.

제약 조건:
- operations의 길이는 1 이상 1,000,000 이하
- 삽입되는 숫자는 -2^31 이상 2^31 - 1 이하의 정수

예제:
입력: operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
출력: [0, 0]

입력: operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
출력: [333, -45]
"""

import heapq
import sys
from collections import Counter
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(operations):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(
        name="프로그래머스 예제 1",
        input=(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],),
        expected=[0, 0],
    ),
    TestCase(
        name="프로그래머스 예제 2",
        input=(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"],),
        expected=[333, -45],
    ),
    TestCase(name="빈 큐에서 삭제는 무시", input=(["D 1", "D -1", "I 5"],), expected=[5, 5]),
    TestCase(name="중복 값 처리", input=(["I 7", "I 7", "D 1"],), expected=[7, 7]),
    TestCase(name="중복 값을 전부 삭제", input=(["I 7", "I 7", "D 1", "D -1"],), expected=[0, 0]),
    TestCase(
        name="삭제 후 같은 값 재삽입",
        input=(["I 3", "D 1", "I 3", "I 1", "D -1"],),
        expected=[3, 3],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
