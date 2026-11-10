"""
문제: 전화번호 목록
난이도: 레벨 2
출처: 프로그래머스 42577
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577

문제 설명:
전화번호부에 적힌 번호 중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 한다.
예를 들어 "119"는 "1195524421"의 접두어다.
어떤 번호가 다른 번호의 접두어인 경우가 있으면 False, 없으면 True를 리턴하라.

제약 조건:
- phone_book의 길이는 1 이상 1,000,000 이하
- 각 전화번호의 길이는 1 이상 20 이하
- 같은 전화번호가 중복해서 들어 있지 않다

예제:
입력: ["119", "97674223", "1195524421"]
출력: False  ("119"가 "1195524421"의 접두어)

입력: ["123", "456", "789"]
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


def solution(phone_book):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(name="프로그래머스 예제 1", input=(["119", "97674223", "1195524421"],), expected=False),
    TestCase(name="프로그래머스 예제 2", input=(["123", "456", "789"],), expected=True),
    TestCase(name="프로그래머스 예제 3", input=(["12", "123", "1235", "567", "88"],), expected=False),
    TestCase(name="번호 하나뿐", input=(["12345"],), expected=True),
    TestCase(name="접두어가 뒤쪽에 있음", input=(["1195524421", "97674223", "119"],), expected=False),
    TestCase(name="중간에 포함되지만 접두어는 아님", input=(["23", "123"],), expected=True),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
