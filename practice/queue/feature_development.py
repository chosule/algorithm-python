"""
문제: 기능개발
난이도: 레벨 2
출처: 프로그래머스 42586
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586

문제 설명:
프로그래머스 팀은 기능 개선 작업을 수행 중이다. 각 기능은 진도율(progresses)과
하루에 늘어나는 진도율(speeds)을 가지고 있고, 진도율이 100%에 도달하면 배포할 수 있다.

단, 기능들은 작업 순서대로만 배포할 수 있다. 어떤 기능이 100%가 되어도,
그보다 먼저 배포됐어야 할 앞 기능이 아직 100%가 안 됐으면 기다렸다가 같이 배포된다.

각 배포마다 몇 개의 기능이 함께 배포되는지 순서대로 리턴하라.

제약 조건:
- 작업의 개수(progresses의 길이)는 100개 이하
- 작업 진도는 100 미만의 자연수
- 작업 속도는 100 이하의 자연수

예제:
입력: progresses = [93, 30, 55], speeds = [1, 30, 5]
출력: [2, 1]

입력: progresses = [95, 90, 99, 99, 80, 99], speeds = [1, 1, 1, 1, 1, 1]
출력: [1, 3, 2]
"""

import math
import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402
import math

def solution(progresses, speeds):
    result = []
    days = []
    count = 1

    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i])/speeds[i]))

    standard = days[0]
    for i in range(1,len(days)):
        if standard >= days[i]:
            count += 1
        else:
            result.append(count)
            standard = days[i]
            count = 1
    
    result.append(count)

    return result

test_cases = [
    TestCase(name="프로그래머스 예제 1", input=([93, 30, 55], [1, 30, 5]), expected=[2, 1]),
    TestCase(
        name="프로그래머스 예제 2",
        input=([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]),
        expected=[1, 3, 2],
    ),
    TestCase(name="전부 같은 날 배포", input=([99, 99, 99], [1, 1, 1]), expected=[3]),
    TestCase(name="기능 하나뿐", input=([50], [10]), expected=[1]),
    TestCase(name="딱 100으로 시작하는 기능 포함", input=([100, 99], [1, 1]), expected=[1, 1]),
    TestCase(name="뒤로 갈수록 점점 느려짐", input=([30, 30, 30], [10, 5, 1]), expected=[1, 1, 1]),
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
