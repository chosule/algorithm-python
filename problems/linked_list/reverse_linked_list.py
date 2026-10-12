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
    """
    시간복잡도: O(n)
    공간복잡도: O(1)

    접근 방법:
    1. prev(뒤집힌 부분의 head)는 None, curr는 head에서 시작한다.
    2. curr.next를 prev 쪽으로 돌려놓고, prev와 curr를 한 칸씩 앞으로 옮긴다.
    3. curr가 None이 되면 prev가 뒤집힌 리스트의 head다.

    주의: curr.next를 바꾸기 전에 원래 다음 노드를 저장해 두지 않으면 나머지 리스트를 잃는다.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # ① 다음 노드 저장
        curr.next = prev  # ② 화살표 뒤집기 (노드가 실제로 바뀌는 줄)
        prev = curr  # ③ prev 한 칸 이동
        curr = next_node  # ④ curr 한 칸 이동
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
