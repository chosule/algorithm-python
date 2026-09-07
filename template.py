"""
문제: [문제 이름을 여기에 작성]
난이도: [쉬움/보통/어려움]
출처: [백준/프로그래머스/LeetCode 등]
링크: [문제 링크]

문제 설명:
[문제에 대한 간단한 설명]

제약 조건:
- [제약 조건 1]
- [제약 조건 2]

예제:
입력: [예제 입력]
출력: [예제 출력]
"""

import sys
from pathlib import Path

# 파일이 어느 depth(problems/<category>/...)에 복사되든 utils를 찾을 수 있도록
# utils/test_helper.py가 있는 상위 폴더를 프로젝트 루트로 간주해 경로에 추가한다.
_here = Path(__file__).resolve().parent
for _parent in (_here, *_here.parents):
    if (_parent / "utils" / "test_helper.py").exists():
        sys.path.insert(0, str(_parent))
        break

from utils.test_helper import TestCase, run_tests  # noqa: E402


def solution(value):
    """
    시간복잡도: O(?)
    공간복잡도: O(?)

    접근 방법:
    1. [단계 1]
    2. [단계 2]
    3. [단계 3]
    """
    # TODO: 여기에 코드를 작성하세요
    return value


# ========================================
# 테스트 케이스
# ========================================

test_cases = [
    TestCase(name="기본 케이스", input=1, expected=1),
    TestCase(name="엣지 케이스 1", input=0, expected=0),
    # 추가 테스트 케이스를 여기에 작성하세요
]

if __name__ == "__main__":
    run_tests(solution, test_cases)
