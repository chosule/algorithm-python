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
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


class MyCircularDeque:
    """
    시간복잡도: 모든 연산 O(1)
    공간복잡도: O(k)

    접근 방법:
    1. 크기 k짜리 고정 배열 하나를 만들고, 맨 앞 위치(head)와 원소 개수(count)만 들고 간다.
       - 뒤쪽 위치는 (head + count) % k 로 언제든 계산되니 따로 저장하지 않는다.
       - count를 쓰면 "비었다"와 "꽉 찼다"를 head/tail만으로 구분하지 못하는 문제가 사라진다.
    2. 앞에 넣을 땐 head를 한 칸 뒤로 물린다: (head - 1) % k. 파이썬은 음수 나머지가
       양수로 나오므로 -1 % k == k - 1 이라 배열 끝으로 자연스럽게 감긴다.
    3. 뒤에 넣을 땐 (head + count) % k 자리에 쓴다.
    4. 삭제는 값을 지울 필요 없이 head/count만 조정하면 된다. 남은 값은 다음 삽입이 덮어쓴다.
    """

    def __init__(self, k: int):
        self.capacity = k
        self.buffer = [0] * k
        self.head = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.capacity
        self.buffer[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buffer[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.buffer[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


def solution(operations, arguments):
    """리트코드 설계 문제 형식(연산 이름 배열 + 인자 배열)을 그대로 재생해 결과 배열을 만든다."""
    deque = None
    results = []
    for name, args in zip(operations, arguments):
        if name == "MyCircularDeque":
            deque = MyCircularDeque(*args)
            results.append(None)
        else:
            results.append(getattr(deque, name)(*args))
    return results


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
        expected=[None, True, -1, -1, False, False],
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
