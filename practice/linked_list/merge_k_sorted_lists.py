"""
문제: Merge k Sorted Lists
난이도: 어려움
출처: LeetCode 23
링크: https://leetcode.com/problems/merge-k-sorted-lists/

문제 설명:
오름차순으로 정렬된 연결 리스트 k개가 배열로 주어진다.
전부 합쳐서 하나의 정렬된 연결 리스트로 만들어 반환한다.

제약 조건:
- 0 <= k <= 10^4
- 0 <= 각 리스트의 길이 <= 500
- -10^4 <= 노드 값 <= 10^4
- 각 리스트는 오름차순 정렬되어 있다.
- 전체 노드 수는 10^4 이하다.

예제:
입력: [[1,4,5],[1,3,4],[2,6]]
출력: [1,1,2,3,4,4,5,6]
"""

import heapq
import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.linked_list import ListNode, from_list, to_list  # noqa: E402
from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(lists):
    heap = []
    for i,node in enumerate(lists):
        if node:
            # [1,4,5],[1,3,4],[2,6] 에서 heap에 1,1,2 head 가 들어감
            heapq.heappush(heap,(node.val,i,node))
    
    dummy = tail = ListNode()

    # 힙이 있을때까지
    while heap:
        val,i,node = heapq.heappop(heap)

        tail.next = node
        tail = node

        if node.next:
            heapq.heappush(heap,(node.next.val,i,val))
    
    return dummy.next









def run(arrays):
    """테스트는 파이썬 리스트로 적고, 연결 리스트로 바꿔 solution에 넘긴다."""
    return to_list(solution([from_list(values) for values in arrays]))


test_cases = [
    TestCase(name="리트코드 예제", input=([[1, 4, 5], [1, 3, 4], [2, 6]],),
             expected=[1, 1, 2, 3, 4, 4, 5, 6]),
    TestCase(name="리스트가 없음", input=([],), expected=[]),
    TestCase(name="빈 리스트 하나", input=([[]],), expected=[]),
    TestCase(name="빈 리스트 섞임", input=([[], [2], [], [1, 3]],), expected=[1, 2, 3]),
    TestCase(name="같은 값만", input=([[1, 1], [1], [1, 1]],), expected=[1, 1, 1, 1, 1]),
    TestCase(name="음수 포함", input=([[-3, 0], [-5, 10]],), expected=[-5, -3, 0, 10]),
]

if __name__ == "__main__":
    run_tests(run, test_cases)
