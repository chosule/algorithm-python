"""
문제: 올바른 괄호
난이도: 보통 (Lv.2)
출처: 프로그래머스 12909
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909

문제 설명:
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 올바른 괄호이면 True, 아니면 False를 리턴하라.
- "()()" 또는 "(())()" 는 올바른 괄호
- ")()(" 또는 "(()(" 는 올바르지 않은 괄호

제약 조건:
- 문자열 s의 길이: 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있다.

예제:
입력: s = "()()"
출력: True

입력: s = "(())()"
출력: True

입력: s = ")()("
출력: False

입력: s = "(()("
출력: False
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
    공간복잡도: O(1)

    접근 방법:
    1. 괄호 종류가 하나뿐이라 스택에 쌓이는 건 전부 '(' 이다.
       그래서 스택 대신 "스택 높이"만 세면 된다.
    2. '(' 면 +1, ')' 면 -1.
    3. 중간에 음수가 되면 짝 없는 ')' 가 나온 것이니 False.
    4. 끝났을 때 0이어야 모든 '(' 가 닫힌 것이다.
    """
    count = 0
    for char in s:
        count += 1 if char == "(" else -1
        if count < 0:
            return False
    return count == 0


# ========================================
# 테스트 케이스
# ========================================

test_cases = [
    TestCase(name="프로그래머스 예제 1", input="()()", expected=True),
    TestCase(name="프로그래머스 예제 2", input="(())()", expected=True),
    TestCase(name="프로그래머스 예제 3", input=")()(", expected=False),
    TestCase(name="프로그래머스 예제 4", input="(()(", expected=False),
    TestCase(name="닫는 괄호 하나", input=")", expected=False),
    TestCase(name="개수는 같지만 순서가 틀림", input="())(()", expected=False),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
