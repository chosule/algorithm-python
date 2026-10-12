"""
문제: Reverse Linked List
난이도: 쉬움
출처: LeetCode 206
링크: https://leetcode.com/problems/reverse-linked-list/

문제 설명:
단일 연결 리스트의 head가 주어진다.
리스트를 뒤집은 뒤, 뒤집힌 리스트의 head를 반환한다.

제약 조건:
- 0 <= 노드 수 <= 5000
- -5000 <= 노드 값 <= 5000

예제:
입력: [1,2,3,4,5]
출력: [5,4,3,2,1]
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.linked_list import ListNode, from_list, to_list  # noqa: E402,F401
from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(head):
    prev, curr = None, head
    while curr:
        node_next = curr.next
        curr.next = prev
        prev = curr
        curr = node_next
    return prev



def run(values):
    """테스트는 파이썬 리스트로 적고, 연결 리스트로 바꿔 solution에 넘긴다."""
    return to_list(solution(from_list(values)))


test_cases = [
    TestCase(name="리트코드 예제 1", input=([1, 2, 3, 4, 5],), expected=[5, 4, 3, 2, 1]),
    TestCase(name="리트코드 예제 2", input=([1, 2],), expected=[2, 1]),
    TestCase(name="빈 리스트", input=([],), expected=[]),
    TestCase(name="노드 하나", input=([7],), expected=[7]),
    TestCase(name="음수와 중복", input=([-1, 0, 0, 5000],), expected=[5000, 0, 0, -1]),
]

if __name__ == "__main__":
    run_tests(run, test_cases)
