"""
문제: 연결 리스트 뒤집기 (Reverse Linked List)
난이도: 쉬움
출처: LeetCode 206
링크: https://leetcode.com/problems/reverse-linked-list/

문제 설명:
단일 연결 리스트의 head가 주어질 때, 리스트를 뒤집어서 뒤집힌 리스트의 head를 리턴하라.

제약 조건:
- 노드 개수 범위: 0 <= n <= 5000
- -5000 <= Node.val <= 5000

예제:
입력: head = [1,2,3,4,5]
출력: [5,4,3,2,1]
"""

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


def solution(values):
    """
    시간복잡도: O(n)
    공간복잡도: O(1) - 추가 리스트 없이 포인터만 옮겨가며 뒤집음

    접근 방법:
    1. "이전 노드"를 가리킬 prev를 None으로 시작한다 (아직 아무도 없음).
    2. 현재 노드(curr)부터 끝까지 순회하면서:
       a. curr.next로 가기 전에 다음 노드를 next_node에 미리 저장해둔다 (안 하면 연결이 끊겨서 길을 잃음).
       b. curr.next를 prev로 돌려서 화살표 방향을 뒤집는다.
       c. prev와 curr를 한 칸씩 앞으로 민다.
    3. curr가 None이 되면 prev가 새로운 head가 되어 있다.
    """
    head = _build_linked_list(values)

    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return _linked_list_to_list(prev)


test_cases = [
    TestCase(name="기본 케이스", input=([1, 2, 3, 4, 5],), expected=[5, 4, 3, 2, 1]),
    TestCase(name="두 개짜리 리스트", input=([1, 2],), expected=[2, 1]),
    TestCase(name="빈 리스트", input=([],), expected=[]),
    TestCase(name="원소 하나", input=([1],), expected=[1]),
    TestCase(name="음수 포함", input=([-1, -2, -3],), expected=[-3, -2, -1]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
