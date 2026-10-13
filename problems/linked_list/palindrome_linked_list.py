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


def solution(head):
    """
    시간복잡도: O(n)
    공간복잡도: O(1)

    접근 방법:
    1. slow는 한 칸, fast는 두 칸씩 움직인다. fast가 끝에 닿으면 slow는 가운데에 있다.
    2. slow부터 끝까지(뒤쪽 절반)를 뒤집는다. (206번 Reverse Linked List와 같은 코드)
    3. head와 뒤집힌 뒤쪽 절반의 head에서 동시에 출발해 값을 비교한다.
       뒤쪽 절반이 끝날 때까지 전부 같으면 팰린드롬이다.

    주의: 노드 수가 홀수면 가운데 노드는 뒤쪽 절반에 들어간다. 앞쪽 절반은 여전히
    가운데 노드를 next로 가리키고 있어서 앞쪽이 한 칸 더 길지만, 비교는 뒤쪽 절반
    길이만큼만 하므로 가운데 노드는 자기 자신과 비교되고 끝난다.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
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
