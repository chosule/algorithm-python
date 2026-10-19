"""
문제: 올바른 괄호 (Valid Parentheses)
난이도: 쉬움
출처: LeetCode 20
링크: https://leetcode.com/problems/valid-parentheses/

문제 설명:
'(', ')', '{', '}', '[', ']' 로만 이루어진 문자열 s가 주어질 때, 올바른 괄호 문자열인지 판별하라.
- 여는 괄호는 같은 종류의 닫는 괄호로 닫혀야 한다.
- 여는 괄호는 올바른 순서로 닫혀야 한다.
- 모든 닫는 괄호에는 짝이 되는 같은 종류의 여는 괄호가 있어야 한다.

제약 조건:
- 1 <= s.length <= 10^4
- s는 '()[]{}' 문자로만 이루어진다.

예제:
입력: s = "()[]{}"
출력: True

입력: s = "(]"
출력: False

입력: s = "([])"
출력: True
"""

import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(s):
    """
    시간복잡도: O(n)
    공간복잡도: O(n)

    접근 방법:
    1. 닫는 괄호 → 여는 괄호 짝을 딕셔너리로 둔다.
    2. 여는 괄호는 스택에 쌓는다.
    3. 닫는 괄호가 나오면 스택 맨 위가 그 짝이어야 한다. 비었거나 다르면 False.
    4. 끝까지 돌고 스택이 비어 있어야 모든 괄호가 닫힌 것이다.
    """
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return not stack


# ========================================
# 테스트 케이스
# ========================================

test_cases = [
    TestCase(name="한 쌍", input="()", expected=True),
    TestCase(name="종류별로 나란히", input="()[]{}", expected=True),
    TestCase(name="종류가 다름", input="(]", expected=False),
    TestCase(name="중첩", input="([])", expected=True),
    TestCase(name="순서가 엇갈림", input="([)]", expected=False),
    TestCase(name="여는 괄호만 남음", input="((", expected=False),
    TestCase(name="닫는 괄호로 시작", input="]", expected=False),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
