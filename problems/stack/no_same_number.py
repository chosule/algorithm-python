"""
문제: 같은 숫자는 싫어
난이도: 쉬움 (Lv.1)
출처: 프로그래머스 12906
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12906

문제 설명:
배열 arr의 각 원소는 0부터 9까지의 숫자다. 배열에서 연속으로 나타나는 숫자는 하나만 남기고 전부 제거하라.
제거한 뒤 남은 수들을 원래 순서대로 리턴한다.
- arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1]
- arr = [4, 4, 4, 3, 3] 이면 [4, 3]

제약 조건:
- 배열 arr의 크기: 1,000,000 이하의 자연수
- 배열 arr의 원소: 0 이상 9 이하의 정수

예제:
입력: arr = [1, 1, 3, 3, 0, 1, 1]
출력: [1, 3, 0, 1]

입력: arr = [4, 4, 4, 3, 3]
출력: [4, 3]
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(arr):
    """
    시간복잡도: O(n)
    공간복잡도: O(n)

    접근 방법:
    1. 결과를 담을 스택을 둔다.
    2. 원소마다 스택 맨 위와 비교해서, 다를 때만 넣는다.
    3. 스택이 비어 있으면 비교할 게 없으니 그냥 넣는다.
    """
    stack = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack


# ========================================
# 테스트 케이스
# ========================================

test_cases = [
    TestCase(name="프로그래머스 예제 1", input=([1, 1, 3, 3, 0, 1, 1],), expected=[1, 3, 0, 1]),
    TestCase(name="프로그래머스 예제 2", input=([4, 4, 4, 3, 3],), expected=[4, 3]),
    TestCase(name="원소 하나", input=([7],), expected=[7]),
    TestCase(name="전부 같은 숫자", input=([0, 0, 0, 0],), expected=[0]),
    TestCase(name="연속 중복 없음", input=([1, 2, 1, 2],), expected=[1, 2, 1, 2]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
