"""
문제: Find First and Last Position of Element in Sorted Array
난이도: 보통
출처: LeetCode 34
링크: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

문제 설명:
오름차순으로 정렬된 정수 배열 nums와 정수 target이 주어진다.
target이 처음 등장하는 인덱스와 마지막으로 등장하는 인덱스를 [first, last] 형태로 리턴한다.
target이 배열에 없으면 [-1, -1]을 리턴한다.

제약 조건:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i], target <= 10^9
- nums는 오름차순으로 정렬되어 있다.
- 시간복잡도 O(log n)으로 풀어야 한다.

예제:
입력: nums = [5, 7, 7, 8, 8, 10], target = 8
출력: [3, 4]

입력: nums = [5, 7, 7, 8, 8, 10], target = 6
출력: [-1, -1]
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
    TestCase(name="LeetCode 예제 1", input=([5, 7, 7, 8, 8, 10], 8), expected=[3, 4]),
    TestCase(name="LeetCode 예제 2", input=([5, 7, 7, 8, 8, 10], 6), expected=[-1, -1]),
    TestCase(name="빈 배열", input=([], 0), expected=[-1, -1]),
    TestCase(name="원소 하나, 일치", input=([1], 1), expected=[0, 0]),
    TestCase(name="전부 target", input=([2, 2, 2, 2], 2), expected=[0, 3]),
    TestCase(name="target이 맨 앞", input=([1, 1, 2, 3], 1), expected=[0, 1]),
    TestCase(name="target이 맨 뒤", input=([1, 2, 3, 3], 3), expected=[2, 3]),
    TestCase(name="target이 모든 값보다 큼", input=([1, 2, 3], 9), expected=[-1, -1]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
