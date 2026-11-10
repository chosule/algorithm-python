"""
문제: 로마 숫자를 정수로 (Roman to Integer)
난이도: 쉬움
출처: LeetCode 13
링크: https://leetcode.com/problems/roman-to-integer/

문제 설명:
로마 숫자는 I(1), V(5), X(10), L(50), C(100), D(500), M(1000) 일곱 글자로 쓴다.
보통 큰 글자가 왼쪽에 오고 값을 더한다. 예) XII = 10 + 1 + 1 = 12
단, 작은 글자가 큰 글자 바로 왼쪽에 오면 빼는 규칙이 있다.
- IV = 4, IX = 9
- XL = 40, XC = 90
- CD = 400, CM = 900
로마 숫자 문자열 s를 정수로 바꿔 리턴하라.

제약 조건:
- 1 <= s의 길이 <= 15
- s는 I, V, X, L, C, D, M으로만 이루어져 있다
- s는 1 이상 3999 이하의 올바른 로마 숫자다

예제:
입력: s = "III"      출력: 3
입력: s = "LVIII"    출력: 58    (L 50 + V 5 + III 3)
입력: s = "MCMXCIV"  출력: 1994  (M 1000 + CM 900 + XC 90 + IV 4)
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
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(name="리트코드 예제 1", input=("III",), expected=3),
    TestCase(name="리트코드 예제 2", input=("LVIII",), expected=58),
    TestCase(name="리트코드 예제 3", input=("MCMXCIV",), expected=1994),
    TestCase(name="빼기 규칙 하나", input=("IV",), expected=4),
    TestCase(name="빼기 규칙 여러 개", input=("XLIX",), expected=49),
    TestCase(name="최댓값", input=("MMMCMXCIX",), expected=3999),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
