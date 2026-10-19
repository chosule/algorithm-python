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


# 문제 설명:
# '(', ')', '{', '}', '[', ']' 로만 이루어진 문자열 s가 주어질 때, 올바른 괄호 문자열인지 판별하라.
# - 여는 괄호는 같은 종류의 닫는 괄호로 닫혀야 한다.
# - 여는 괄호는 올바른 순서로 닫혀야 한다.
# - 모든 닫는 괄호에는 짝이 되는 같은 종류의 여는 괄호가 있어야 한다.

# s = "()[]{}"
def solution(s): 
    stack = []
    obj = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    for i in range(len(s)):
        # 여는 괄호만 stack 에 넣기
        if s[i] in obj:
            stack.append(s[i])
            print("stack ->", stack)
        else:
            # 마지막 여는 괄호를 꺼내거 obj[그것] == v 인지 확인하기
            if not stack or obj[stack.pop()] != s[i]:
                return False

    return len(stack) == 0 
    
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
