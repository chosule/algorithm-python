"""
문제: Contains Duplicate
난이도: 쉬움
출처: LeetCode 217
링크: https://leetcode.com/problems/contains-duplicate/

문제 설명:
정수 배열 nums가 주어질 때, 어떤 값이 배열에 두 번 이상 나타나면 True,
모든 원소가 서로 다르면 False를 리턴한다.

제약 조건:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

예제:
입력: nums = [1, 2, 3, 1]
출력: True

입력: nums = [1, 2, 3, 4]
출력: False
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
    1. 지금까지 본 값을 set에 모아 둔다.
    2. 새 값이 이미 set에 있으면 중복이므로 바로 True를 리턴한다.
    3. 끝까지 중복이 없으면 False를 리턴한다.
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


test_cases = [
    TestCase(name="LeetCode 예제 1", input=([1, 2, 3, 1],), expected=True),
    TestCase(name="LeetCode 예제 2", input=([1, 2, 3, 4],), expected=False),
    TestCase(name="LeetCode 예제 3", input=([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), expected=True),
    TestCase(name="원소 하나", input=([1],), expected=False),
    TestCase(name="음수 중복", input=([-1, -1],), expected=True),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
