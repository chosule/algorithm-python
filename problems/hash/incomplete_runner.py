"""
문제: 완주하지 못한 선수
난이도: 레벨 1
출처: 프로그래머스 42576
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576

문제 설명:
마라톤에 참여한 선수 이름 배열 participant와 완주한 선수 이름 배열 completion이
주어진다. 단 한 명의 선수를 제외하고 모두 완주했을 때, 완주하지 못한 선수의 이름을
리턴하라.

제약 조건:
- 참가자 수는 1명 이상 100,000명 이하
- completion의 길이는 participant의 길이보다 1 작다
- 이름은 알파벳 소문자 1~20글자
- 참가자 중에는 동명이인이 있을 수 있다

예제:
입력: participant = ["leo", "kiki", "eden"], completion = ["eden", "kiki"]
출력: "leo"

입력: participant = ["mislav", "stanko", "mislav", "ana"], completion = ["stanko", "ana", "mislav"]
출력: "mislav"  (mislav가 두 명인데 한 명만 완주)
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


def solution(participant, completion):
    """
    시간복잡도: O(n)
    공간복잡도: O(n)

    접근 방법:
    1. 동명이인이 있으니 set은 안 된다 (이름이 하나로 합쳐져서 몇 명인지 잃어버림).
    2. Counter로 이름 → 사람 수를 센다.
    3. 참가자 Counter에서 완주자 Counter를 빼면 개수가 남은 이름 하나만 남는다.
    """
    left = Counter(participant) - Counter(completion)
    return next(iter(left))


test_cases = [
    TestCase(name="프로그래머스 예제 1", input=(["leo", "kiki", "eden"], ["eden", "kiki"]), expected="leo"),
    TestCase(
        name="프로그래머스 예제 2",
        input=(
            ["marina", "josipa", "nikola", "vinko", "filipa"],
            ["josipa", "filipa", "marina", "nikola"],
        ),
        expected="vinko",
    ),
    TestCase(
        name="동명이인 중 한 명만 완주",
        input=(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]),
        expected="mislav",
    ),
    TestCase(name="참가자 한 명", input=(["solo"], []), expected="solo"),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
