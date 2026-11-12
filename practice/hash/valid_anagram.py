"""
문제: Valid Anagram
난이도: 쉬움
출처: LeetCode 242
링크: https://leetcode.com/problems/valid-anagram/

문제 설명:
두 문자열 s와 t가 주어질 때, t가 s의 애너그램(문자를 재배열해서 만들 수 있는 문자열)이면
True, 아니면 False를 리턴한다.

제약 조건:
- 1 <= s.length, t.length <= 5 * 10^4
- s와 t는 영어 소문자로만 이루어져 있다.

예제:
입력: s = "anagram", t = "nagaram"
출력: True

입력: s = "rat", t = "car"
출력: False
"""

import sys
from collections import Counter
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402
from collections import Counter

def solution(s, t):
    sCount = Counter(s)
    tCount = Counter(t)

    if sCount == tCount:
        return True
    
    return False


test_cases = [
    TestCase(name="LeetCode 예제 1", input=("anagram", "nagaram"), expected=True),
    TestCase(name="LeetCode 예제 2", input=("rat", "car"), expected=False),
    TestCase(name="길이가 다름", input=("a", "ab"), expected=False),
    TestCase(name="같은 문자열", input=("abc", "abc"), expected=True),
    TestCase(name="문자 개수만 다름", input=("aab", "abb"), expected=False),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
