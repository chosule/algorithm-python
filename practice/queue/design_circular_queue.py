"""
문제: 원형 큐 설계 (Design Circular Queue)
난이도: 보통
출처: LeetCode 622
링크: https://leetcode.com/problems/design-circular-queue/

문제 설명:
크기가 k인 원형 큐를 설계하라.
- MyCircularQueue(k): 큐의 크기를 k로 초기화한다.
- enQueue(value): 큐가 가득 차지 않았으면 value를 넣고 true, 가득 찼으면 false를 리턴한다.
- deQueue(): 큐가 비어있지 않으면 맨 앞 요소를 제거하고 true, 비어있으면 false를 리턴한다.
- Front(): 큐의 맨 앞 요소를 리턴한다. 비어있으면 -1.
- Rear(): 큐의 맨 뒤 요소를 리턴한다. 비어있으면 -1.
- isEmpty(): 큐가 비어있는지 여부를 리턴한다.
- isFull(): 큐가 가득 찼는지 여부를 리턴한다.

제약 조건:
- 고정 크기 k를 넘어서지 않아야 한다.
- 빠져나간 앞쪽 공간을 낭비 없이 재사용해야 한다 (원형 구조).

예제:
MyCircularQueue queue = new MyCircularQueue(3);
queue.enQueue(1); // true
queue.enQueue(2); // true
queue.enQueue(3); // true
queue.enQueue(4); // false (가득 참)
queue.Rear();     // 3 리턴
queue.isFull();   // true 리턴
queue.deQueue();  // true
queue.enQueue(4); // true
queue.Rear();     // 4 리턴
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


class MyCircularQueue:
    """
    시간복잡도: 모든 연산 O(1)
    공간복잡도: O(k)

    접근 방법:
    1. 크기 k짜리 고정 배열을 준비한다.
    2. front_idx(맨 앞 위치)와 count(현재 들어있는 개수)만 들고 다닌다.
    3. rear 위치는 매번 계산: (front_idx + count) % k
    4. 배열 끝에 닿으면 나머지 연산(%)으로 다시 0번 인덱스부터 재사용한다.
    """

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front_idx = 0
        self.count = 0

    # 큐가 가득차지 않았으면 value를 넣고
    # 가득찼으면 False를 리턴
    def enQueue(self, value: int) -> bool:
        # 큐가 가득찼으면 False 리턴
        if self.isFull():
            return False

        # value 저장
        rear_idx = (self.front_idx + self.count) % self.size 
        self.queue[rear_idx] = value
        self.count += 1
        return True
    
    # 제일 앞에꺼 내보내기
    def deQueue(self) -> bool:
        #큐가 가득 찼으면 False 리턴하기 
        if self.isEmpty():
            return False

        # 큐가 남으면 앞에꺼 내보내기
        self.front_idx = (self.front_idx + 1) % self.size
        self.count -= 1
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front_idx]

    # 큐의 맨뒤 요소를 리턴한다. 비어있으면 -1 반환
    def Rear(self) -> int:
        # 비어있으면 -1 반환
        if self.isEmpty() :
            return -1
        # 맨뒤요소 리턴하기
        rear_idx = (self.front_idx + self.count - 1) % self.size
        return self.queue[rear_idx]
        
    # 큐가 비어있는지 여부를 리턴하기
    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size



def solution(operations, values):
    """
    operations: 호출할 메서드 이름 리스트 (첫 원소는 항상 "MyCircularQueue")
    values: 각 연산에 대응하는 인자 리스트 (인자가 없으면 빈 리스트)

    각 연산의 결과를 순서대로 리스트에 담아 리턴한다.
    (생성자처럼 리턴값이 없는 연산은 None을 담는다.)
    """
    results = []
    queue = None

    for op, args in zip(operations, values):
        if op == "MyCircularQueue":
            queue = MyCircularQueue(args[0])
            results.append(None)
        elif op == "enQueue":
            results.append(queue.enQueue(args[0]))
        elif op == "deQueue":
            results.append(queue.deQueue())
        elif op == "Front":
            results.append(queue.Front())
        elif op == "Rear":
            results.append(queue.Rear())
        elif op == "isEmpty":
            results.append(queue.isEmpty())
        elif op == "isFull":
            results.append(queue.isFull())

    return results


test_cases = [
    TestCase(
        name="기본 케이스 (LeetCode 예제)",
        input=(
            [
                "MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
                "Rear", "isFull", "deQueue", "enQueue", "Rear",
            ],
            [[3], [1], [2], [3], [4], [], [], [], [4], []],
        ),
        expected=[None, True, True, True, False, 3, True, True, True, 4],
    ),
    TestCase(
        name="크기 1짜리 큐",
        input=(
            ["MyCircularQueue", "enQueue", "isFull", "Front", "deQueue", "isEmpty"],
            [[1], [10], [], [], [], []],
        ),
        expected=[None, True, True, 10, True, True],
    ),
    TestCase(
        name="빈 큐에서 deQueue/Front/Rear",
        input=(
            ["MyCircularQueue", "deQueue", "Front", "Rear", "isEmpty"],
            [[2], [], [], [], []],
        ),
        expected=[None, False, -1, -1, True],
    ),
    TestCase(
        name="꽉 채운 뒤 앞쪽 비우고 재사용 (원형 재활용 확인)",
        input=(
            [
                "MyCircularQueue", "enQueue", "enQueue", "deQueue",
                "enQueue", "deQueue", "enQueue", "Front", "Rear",
            ],
            [[2], [1], [2], [], [3], [], [4], [], []],
        ),
        expected=[None, True, True, True, True, True, True, 3, 4],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
