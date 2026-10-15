"""
문제: 큐를 이용한 스택 구현 (Implement Stack using Queues)
난이도: 쉬움
출처: LeetCode 225
링크: https://leetcode.com/problems/implement-stack-using-queues/

문제 설명:
큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
- push(x): 요소 x를 스택 맨 위에 삽입한다.
- pop(): 스택 맨 위 요소를 제거하고 리턴한다.
- top(): 스택 맨 위 요소를 조회한다.
- empty(): 스택이 비어 있는지 여부를 리턴한다.

제약 조건:
- 큐의 기본 연산만 써야 한다 (뒤에 넣기, 앞에서 꺼내기/보기, 크기, 비었는지 확인)
- 1 <= x <= 9
- pop/top은 스택이 비어 있지 않을 때만 호출된다.

예제:
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);
stack.top();    // 2 리턴
stack.pop();    // 2 리턴
stack.empty();  // false 리턴
"""

import sys
from collections import deque
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402
from collections import deque

class MyStack:
    def __init__(self):
        self.stack = []
        self.queue = deque
        
    def push(self, x: int) -> None:
        queue.append(x)
        print("??",stack)

        for i range(len(stack)-1):
            stack.append(self.queue.popleft())



    def pop(self) -> int:
        return stack[0]


    def top(self) -> int:
        pass  # TODO: 여기에 코드를 작성하세요

    def empty(self) -> bool:
        pass  # TODO: 여기에 코드를 작성하세요


def solution(operations, arguments):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(
        name="리트코드 예제",
        input=(
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
        ),
        expected=[None, None, None, 2, 2, False],
    ),
    TestCase(
        name="여러 번 push 후 역순으로 pop",
        input=(
            ["MyStack", "push", "push", "push", "pop", "pop", "pop", "empty"],
            [[], [1], [2], [3], [], [], [], []],
        ),
        expected=[None, None, None, None, 3, 2, 1, True],
    ),
    TestCase(
        name="push/pop 번갈아",
        input=(
            ["MyStack", "push", "push", "pop", "push", "top", "pop", "pop", "empty"],
            [[], [1], [2], [], [3], [], [], [], []],
        ),
        expected=[None, None, None, 2, None, 3, 3, 1, True],
    ),
    TestCase(
        name="생성 직후 비어 있음",
        input=(["MyStack", "empty"], [[], []]),
        expected=[None, True],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
