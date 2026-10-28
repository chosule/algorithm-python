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
    """
    시간복잡도: O(N log k)  (N = 전체 노드 수, k = 리스트 개수)
    공간복잡도: O(k)  (힙에는 리스트마다 노드 하나씩만 들어간다)

    접근 방법:
    1. 각 리스트의 첫 노드만 최소 힙에 넣는다. 힙의 top이 곧 "남은 것 중 가장 작은 값"이다.
    2. top을 꺼내 결과 리스트 뒤에 붙이고, 꺼낸 노드의 다음 노드를 힙에 넣는다.
    3. 힙이 빌 때까지 반복한다.

    주의: 힙에 (값, 노드)만 넣으면 값이 같을 때 노드끼리 비교하다 TypeError가 난다.
    ListNode에는 < 연산이 없기 때문이다. 그래서 가운데에 리스트 번호 i를 끼워
    값이 같으면 i로 순서가 정해지게 한다.
    """
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
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
