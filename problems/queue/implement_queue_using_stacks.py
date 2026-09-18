"""
문제: 스택을 이용한 큐 구현 (Implement Queue using Stacks)
난이도: 쉬움
출처: LeetCode 232
링크: https://leetcode.com/problems/implement-queue-using-stacks/

문제 설명:
스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
- push(x): 요소 x를 큐 마지막에 삽입한다.
- pop(): 큐 처음에 있는 요소를 제거한다.
- peek(): 큐 처음에 있는 요소를 조회한다.
- empty(): 큐가 비어 있는지 여부를 리턴한다.

제약 조건:
- 리스트를 스택처럼만 써야 한다 (append/pop처럼 한쪽 끝만 조작. 인덱스로 중간/맨 앞 접근 금지)

예제:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();   // 1 리턴
queue.pop();    // 1 리턴
queue.empty();  // false 리턴
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


class MyQueue:
    # 스택을 이용해서 큐를 구현하자
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # TODO: 큐 처음 요소를 조회만 하고 리턴 (제거 X)
        # output이 모두 없을경우에만 
        if not self.output: 
            # input 모두 실행
            while self.input:
                # output에 거꾸로 대입
                self.output.append(self.input.pop())
        
        # 스택으로 구현한 큐 첫번째 반환
        return self.output[-1]



    def empty(self) -> bool:
        # TODO: 큐가 비어있는지 리턴
        return self.input == [] and self.output == []


def solution(operations, values):
    """
    operations: 호출할 메서드 이름 리스트 (첫 원소는 항상 "MyQueue")
    values: 각 연산에 대응하는 인자 리스트 (인자가 없으면 빈 리스트)

    각 연산의 결과를 순서대로 리스트에 담아 리턴한다.
    (생성자/push처럼 리턴값이 없는 연산은 None을 담는다.)
    """
    results = []
    queue = None

    for op, args in zip(operations, values):
        if op == "MyQueue":
            queue = MyQueue()
            results.append(None)
        elif op == "push":
            queue.push(args[0])
            results.append(None)
        elif op == "pop":
            results.append(queue.pop())
        elif op == "peek":
            results.append(queue.peek())
        elif op == "empty":
            results.append(queue.empty())

    return results


test_cases = [
    TestCase(
        name="기본 케이스",
        input=(
            ["MyQueue", "push", "push", "peek", "pop", "empty"],
            [[], [1], [2], [], [], []],
        ),
        expected=[None, None, None, 1, 1, False],
    ),
    TestCase(
        name="여러 번 push 후 순서대로 pop",
        input=(
            ["MyQueue", "push", "push", "push", "pop", "pop", "pop"],
            [[], [1], [2], [3], [], [], []],
        ),
        expected=[None, None, None, None, 1, 2, 3],
    ),
    TestCase(
        name="push/pop 번갈아 (input/output 재활용 확인)",
        input=(
            ["MyQueue", "push", "push", "pop", "push", "pop", "pop", "empty"],
            [[], [1], [2], [], [3], [], [], []],
        ),
        expected=[None, None, None, 1, None, 2, 3, True],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
