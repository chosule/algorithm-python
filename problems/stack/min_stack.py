"""
문제: 최솟값 스택 (Min Stack)
난이도: 보통
출처: LeetCode 155
링크: https://leetcode.com/problems/min-stack/

문제 설명:
push, pop, top, 그리고 최솟값 조회를 모두 O(1)에 하는 스택을 구현하라.
- push(val): 요소 val을 스택에 넣는다.
- pop(): 스택 맨 위 요소를 제거한다.
- top(): 스택 맨 위 요소를 조회한다.
- getMin(): 스택에 있는 요소 중 최솟값을 조회한다.

제약 조건:
- -2^31 <= val <= 2^31 - 1
- pop, top, getMin은 스택이 비어 있지 않을 때만 호출된다.
- 각 연산은 O(1)이어야 한다.

예제:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // -3 리턴
minStack.pop();
minStack.top();    // 0 리턴
minStack.getMin(); // -2 리턴
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


class MinStack:
    """
    시간복잡도: 모든 연산 O(1)
    공간복잡도: O(n)

    접근 방법:
    1. 값을 넣을 때 (값, 그 시점까지의 최솟값)을 한 쌍으로 같이 쌓는다.
    2. 그러면 맨 위 쌍의 두 번째 값이 항상 "지금 스택 전체의 최솟값"이다.
    3. pop하면 그 쌍이 통째로 빠지므로, 아래 쌍에 저장된 이전 최솟값이 자연스럽게 다시 드러난다.
       예) push -2, 0, -3 → [(-2, -2), (0, -2), (-3, -3)] → pop → [(-2, -2), (0, -2)] → getMin = -2
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def solution(operations, arguments):
    """리트코드 설계 문제 형식(연산 이름 배열 + 인자 배열)을 그대로 재생해 결과 배열을 만든다."""
    stack = None
    results = []
    for name, args in zip(operations, arguments):
        if name == "MinStack":
            stack = MinStack()
            results.append(None)
        else:
            results.append(getattr(stack, name)(*args))
    return results


test_cases = [
    TestCase(
        name="리트코드 예제",
        input=(
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
        ),
        expected=[None, None, None, None, -3, None, 0, -2],
    ),
    TestCase(
        name="같은 최솟값이 여러 번 들어옴",
        input=(
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            [[], [1], [1], [2], [], [], [], [], []],
        ),
        expected=[None, None, None, None, 1, None, 1, None, 1],
    ),
    TestCase(
        name="최솟값을 pop하면 이전 최솟값으로 돌아감",
        input=(
            ["MinStack", "push", "push", "getMin", "pop", "getMin", "top"],
            [[], [5], [3], [], [], [], []],
        ),
        expected=[None, None, None, 3, None, 5, 5],
    ),
    TestCase(
        name="값이 하나뿐",
        input=(["MinStack", "push", "top", "getMin"], [[], [7], [], []]),
        expected=[None, None, 7, 7],
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
