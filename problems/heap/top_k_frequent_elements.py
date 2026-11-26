"""
문제: Top K Frequent Elements
난이도: 보통
출처: LeetCode 347
링크: https://leetcode.com/problems/top-k-frequent-elements/

문제 설명:
정수 배열 nums와 정수 k가 주어질 때, 가장 자주 등장하는 원소 k개를 리턴한다.
(LeetCode는 순서를 신경 쓰지 않지만, 여기서는 테스트를 위해
빈도가 높은 순서로, 빈도가 같으면 먼저 등장한 순서로 리턴한다.)

제약 조건:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k는 1 이상, 서로 다른 원소의 개수 이하이다.
- 답은 유일하게 정해진다.

추가 질문: 시간복잡도가 O(n log n)보다 좋아야 한다.

예제:
입력: nums = [1, 1, 1, 2, 2, 3], k = 2
출력: [1, 2]

입력: nums = [1], k = 1
출력: [1]
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


def solution(nums, k):
    """
    시간복잡도: O(n log k)
    공간복잡도: O(n)

    접근 방법:
    1. Counter로 원소별 등장 횟수를 센다. (Counter는 처음 등장한 순서를 유지한다.)
    2. heapq.nlargest로 횟수가 큰 원소 k개를 고른다. 내부적으로 크기 k인 힙을 쓰기 때문에
       전체를 정렬하는 O(n log n)보다 빠르다. 횟수가 같으면 먼저 들어온 원소가 앞에 온다.
    """
    count = Counter(nums)
    return heapq.nlargest(k, count, key=count.get)


test_cases = [
    TestCase(name="LeetCode 예제 1", input=([1, 1, 1, 2, 2, 3], 2), expected=[1, 2]),
    TestCase(name="LeetCode 예제 2", input=([1], 1), expected=[1]),
    TestCase(name="LeetCode 예제 3", input=([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), expected=[1, 2]),
    TestCase(name="음수 포함", input=([-1, -1, 4, 4, 4, 5], 2), expected=[4, -1]),
    TestCase(name="k가 원소 종류 수와 같음", input=([3, 3, 2, 1, 1, 1], 3), expected=[1, 3, 2]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
