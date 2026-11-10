"""
문제: 의상
난이도: 레벨 2
출처: 프로그래머스 42578
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578

문제 설명:
코니는 매일 다른 옷 조합을 입는다. clothes의 각 원소는 [의상 이름, 의상 종류]다.
하루에 종류별로 최대 1가지만 입을 수 있고, 최소 한 개의 의상은 입어야 한다.
서로 다른 옷 조합의 수를 리턴하라.

제약 조건:
- clothes의 길이는 1 이상 30 이하
- 같은 이름의 의상은 존재하지 않는다

예제:
입력: [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
출력: 5
  headgear 2개, eyewear 1개
  → yellow_hat / blue_sunglasses / green_turban /
    yellow_hat + blue_sunglasses / green_turban + blue_sunglasses
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


def solution(clothes):
    pass  # TODO: 여기에 코드를 작성하세요


test_cases = [
    TestCase(
        name="프로그래머스 예제 1",
        input=([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],),
        expected=5,
    ),
    TestCase(
        name="프로그래머스 예제 2",
        input=([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]],),
        expected=3,
    ),
    TestCase(name="옷 하나뿐", input=([["cap", "headgear"]],), expected=1),
    TestCase(
        name="종류 3개에 하나씩",
        input=([["a", "hat"], ["b", "top"], ["c", "shoes"]],),
        expected=7,
    ),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
