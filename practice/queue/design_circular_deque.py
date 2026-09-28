"""
문제: Design Circular Deque
난이도: 보통
출처: LeetCode 641
링크: https://leetcode.com/problems/design-circular-deque/

문제 설명:
크기가 k로 고정된 원형 덱(deque)을 직접 구현한다. 앞/뒤 양쪽에서 삽입과
삭제가 가능하고, 꽉 찬 상태에서의 삽입과 빈 상태에서의 삭제는 실패한다.

구현할 연산:
- MyCircularDeque(k)  : 크기 k로 생성
- insertFront(value)  : 앞에 삽입, 성공하면 True
- insertLast(value)   : 뒤에 삽입, 성공하면 True
- deleteFront()       : 앞에서 삭제, 성공하면 True
- deleteLast()        : 뒤에서 삭제, 성공하면 True
- getFront()          : 맨 앞 값, 비었으면 -1
- getRear()           : 맨 뒤 값, 비었으면 -1
- isEmpty() / isFull()

제약 조건:
- 1 <= k <= 1000
- 0 <= value <= 1000
- 모든 연산은 합쳐서 최대 2000번 호출되고, 각각 O(1)이어야 한다.

예제:
입력: ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront",
       "getRear","isFull","deleteLast","insertFront","getFront"]
      [[3],[1],[2],[3],[4],[],[],[],[4],[]]
출력: [null,true,true,true,false,2,true,true,true,4]
"""

import sys
import collections
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402



class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None      # 이전 노드
        self.right = None     # 다음 노드


class MyCircularDeque:

    def __init__(self, k: int):
        
        self.head , self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail , self.head


    def insertFront(self, node, value: int) -> bool:
        # 연결리스트가 꽉차있으면 False 반환하기
        if self.k == self.len:
            return False

        self.len += 1
        
        new = value
        n = node 

        # 헤드오른쪽에 새로운 노드 넣기
        self.head.right = new

        # new 왼쪽에는 헤드 , 오른쪽에는 기존 에있던 노드 연결하기
        new.left, new.right = self.head, n

        # 기존 노드 왼쪽은 new 바라보게하기
        n.left = new

        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.len:
            return False

        self.len += 1

        # 새로들어온값
        new = value
        # 이전 값
        n = self.tail.left

        # 일단 tail의 왼쪽을 new랑 연결하기 
        self.tail.left = new

        # 새로 들어온 값 왼쪽 오른쪽을 연결하기
        new.left , new.right = n , self.tail

        # 이전값 오른쪽을 새로들어온 값으로 교체하기
        n.right = new 
        
        return True


    def deleteFront(self) -> bool:
        delete_node = self.head.right

        self.head.right  = self.head.right.right



    def deleteLast(self) -> bool:
        pass  # TODO: 여기에 코드를 작성하세요

    def getFront(self) -> int:
        pass  # TODO: 여기에 코드를 작성하세요

    def getRear(self) -> int:
        pass  # TODO: 여기에 코드를 작성하세요

    def isEmpty(self) -> bool:
        pass  # TODO: 여기에 코드를 작성하세요

    def isFull(self) -> bool:
        pass  # TODO: 여기에 코드를 작성하세요


def solution(operations, arguments):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(
        name="리트코드 예제",
        input=(
            ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
             "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
            [[3], [1], [2], [3], [4], [], [], [], [4], []],
        ),
        expected=[None, True, True, True, False, 2, True, True, True, 4],
    ),
    TestCase(
        name="빈 덱에서 조회/삭제",
        input=(
            ["MyCircularDeque", "isEmpty", "getFront", "getRear", "deleteFront", "deleteLast"],
            [[2], [], [], [], [], []],
        ),
        expected=[None, True, -1, -1, False, False],\
    ),
    TestCase(
        name="크기 1 덱",
        input=(
            ["MyCircularDeque", "insertFront", "isFull", "insertLast", "getRear",
             "deleteLast", "isEmpty"],
            [[1], [7], [], [8], [], [], []],
        ),
        expected=[None, True, True, False, 7, True, True],
    ),
    TestCase(
        name="앞뒤로 감아가며 재사용",
        input=(
            ["MyCircularDeque", "insertFront", "insertFront", "insertFront",
             "deleteLast", "deleteLast", "insertLast", "insertLast",
             "getFront", "getRear", "isFull"],
            [[3], [1], [2], [3], [], [], [9], [8], [], [], []],
        ),
        expected=[None, True, True, True, True, True, True, True, 3, 8, True],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
