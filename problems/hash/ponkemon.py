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


def solution(nums):
    """
    시간복잡도: O(n)
    공간복잡도: O(n)

    접근 방법:
    1. set에 넣으면 중복이 사라지니까 len(set(nums))가 종류 수다.
    2. 고를 수 있는 건 N/2마리뿐이라, 종류가 아무리 많아도 N/2를 넘을 수 없다.
    3. 그래서 답은 min(종류 수, N/2).
    """
    return min(len(set(nums)), len(nums) // 2)


test_cases = [
    TestCase(name="프로그래머스 예제 1", input=([3, 1, 2, 3],), expected=2),
    TestCase(name="프로그래머스 예제 2", input=([3, 3, 3, 2, 2, 4],), expected=3),
    TestCase(name="프로그래머스 예제 3", input=([3, 3, 3, 2, 2, 2],), expected=2),
    TestCase(name="전부 같은 종류", input=([7, 7, 7, 7],), expected=1),
    TestCase(name="전부 다른 종류", input=([1, 2, 3, 4, 5, 6],), expected=3),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
