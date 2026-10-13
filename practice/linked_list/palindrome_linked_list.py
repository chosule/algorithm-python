"""
문제: Palindrome Linked List
난이도: 쉬움
출처: LeetCode 234
링크: https://leetcode.com/problems/palindrome-linked-list/

문제 설명:
단일 연결 리스트의 head가 주어진다.
앞에서 읽어도 뒤에서 읽어도 같은 팰린드롬이면 True, 아니면 False를 반환한다.

제약 조건:
- 1 <= 노드 수 <= 10^5
- 0 <= 노드 값 <= 9

예제:
입력: [1,2,2,1]
출력: True
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.linked_list import ListNode, from_list  # noqa: E402,F401
from utils.test_helper import TestCase, run_tests  # noqa: E402
from collections import deque

def solution(head):
    q = deque()
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    
    while len(q) > 1:
        print(q)
        if q.popleft() != q.pop():
            return False

    return True    



def run(values):
    """테스트는 파이썬 리스트로 적고, 연결 리스트로 바꿔 solution에 넘긴다."""
    return solution(from_list(values))


test_cases = [
    TestCase(name="리트코드 예제 1", input=([1, 2, 2, 1],), expected=True),
    TestCase(name="리트코드 예제 2", input=([1, 2],), expected=False),
    TestCase(name="노드 하나", input=([7],), expected=True),
    TestCase(name="홀수 길이 팰린드롬", input=([1, 2, 3, 2, 1],), expected=True),
    TestCase(name="홀수 길이 아님", input=([1, 2, 3, 1, 1],), expected=False),
    TestCase(name="양 끝만 같음", input=([1, 2, 3, 3, 1],), expected=False),
    TestCase(name="전부 같은 값", input=([5, 5, 5, 5],), expected=True),
]

if __name__ == "__main__":
    run_tests(run, test_cases)
