"""
문제: k개 정렬된 연결 리스트 병합 (Merge k Sorted Lists)
난이도: 어려움
출처: LeetCode 23
링크: https://leetcode.com/problems/merge-k-sorted-lists/

문제 설명:
k개의 정렬된 연결 리스트가 주어질 때, 이들을 하나의 정렬된 연결 리스트로 합쳐서 반환하라.

제약 조건:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- lists[i]는 오름차순으로 정렬되어 있다.
- 전체 노드 개수는 최대 10^4개

예제:
입력: lists = [[1,4,5],[1,3,4],[2,6]]
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

from utils.test_helper import TestCase, run_tests  # noqa: E402


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def _linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def solution(lists):
    """
    시간복잡도: O(N log k) - N: 전체 노드 개수, k: 리스트 개수
    공간복잡도: O(k) - 힙에 최대 k개 노드만 들어있음

    접근 방법:
    1. 각 연결 리스트의 head 노드를 최소 힙에 넣는다 (첫 노드끼리 비교하면 되니까).
    2. 힙에서 가장 작은 값의 노드를 꺼내 결과 리스트 맨 뒤에 이어 붙인다.
    3. 방금 꺼낸 노드의 다음 노드가 있으면 그 노드를 다시 힙에 넣는다.
    4. 힙이 빌 때까지 2~3을 반복한다.
    """
    heads = [_build_linked_list(values) for values in lists]

    heap = []
    for index, head in enumerate(heads):
        if head:
            # 두 번째 원소(index)는 val이 같을 때 ListNode끼리 비교하다 에러나는 걸 막는 타이브레이커
            heapq.heappush(heap, (head.val, index, head))

    dummy = ListNode()
    current = dummy

    while heap:
        _, index, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))

    return _linked_list_to_list(dummy.next)


test_cases = [
    TestCase(
        name="기본 케이스",
        input=([[1, 4, 5], [1, 3, 4], [2, 6]],),
        expected=[1, 1, 2, 3, 4, 4, 5, 6],
    ),
    TestCase(name="빈 리스트들 자체가 없음", input=([],), expected=[]),
    TestCase(name="빈 배열 하나만 포함", input=([[]],), expected=[]),
    TestCase(name="일부만 빈 리스트", input=([[], [1]],), expected=[1]),
    TestCase(name="리스트가 하나뿐인 경우", input=([[1, 2, 3]],), expected=[1, 2, 3]),
    TestCase(
        name="중복 값이 여러 리스트에 걸쳐 있는 경우",
        input=([[1, 1, 1], [1, 1], [1]],),
        expected=[1, 1, 1, 1, 1, 1],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
