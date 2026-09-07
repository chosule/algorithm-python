"""
문제: Two Sum
난이도: 쉬움
출처: LeetCode
링크: https://leetcode.com/problems/two-sum/

문제 설명:
정수 배열 nums와 정수 target이 주어질 때, 두 수를 더해서 target이 되는
인덱스 두 개를 반환한다.

제약 조건:
- 각 입력에 정확히 하나의 답이 존재한다고 가정한다.
- 같은 요소를 두 번 사용할 수 없다.

예제:
입력: nums = [2, 7, 11, 15], target = 9
출력: [0, 1]
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(nums, target):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(name="기본 케이스", input=([2, 7, 11, 15], 9), expected=[0, 1]),
    TestCase(name="중간에서 매칭", input=([3, 2, 4], 6), expected=[1, 2]),
    TestCase(name="같은 값 두 개", input=([3, 3], 6), expected=[0, 1]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
