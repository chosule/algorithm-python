"""테스트 헬퍼 유틸리티
알고리즘 문제 풀이 시 테스트를 쉽게 할 수 있도록 도와주는 함수들
"""

import time
from dataclasses import dataclass, field
from typing import Any, Callable


class Colors:
    RESET = "\033[0m"
    BRIGHT = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"


def success(message: str) -> None:
    print(f"{Colors.GREEN}{message}{Colors.RESET}")


def error(message: str) -> None:
    print(f"{Colors.RED}{message}{Colors.RESET}")


def info(message: str) -> None:
    print(f"{Colors.BLUE}{message}{Colors.RESET}")


def warn(message: str) -> None:
    print(f"{Colors.YELLOW}{message}{Colors.RESET}")


def title(message: str) -> None:
    print(f"{Colors.BRIGHT}{Colors.CYAN}{message}{Colors.RESET}")


@dataclass
class TestCase:
    input: Any
    expected: Any
    name: str = ""


def _as_args(value: Any) -> tuple:
    """input이 tuple/list면 여러 인자로, 아니면 단일 인자로 취급한다."""
    return tuple(value) if isinstance(value, (tuple, list)) else (value,)


def run_tests(solution: Callable, test_cases: list[TestCase]) -> None:
    title("=== 테스트 시작 ===\n")

    passed = 0
    failed = 0

    for index, case in enumerate(test_cases):
        name = case.name or f"테스트 케이스 {index + 1}"
        args = _as_args(case.input)

        try:
            start = time.perf_counter()
            result = solution(*args)
            elapsed_ms = (time.perf_counter() - start) * 1000

            if result == case.expected:
                success(f"✓ {name}")
                info(f"  실행 시간: {elapsed_ms:.4f}ms")
                print(f"  결과: {result!r}\n")
                passed += 1
            else:
                error(f"✗ {name}")
                warn(f"  예상: {case.expected!r}")
                warn(f"  실제: {result!r}")
                info(f"  실행 시간: {elapsed_ms:.4f}ms\n")
                failed += 1
        except Exception as err:  # noqa: BLE001 - 테스트 러너는 모든 예외를 잡아서 보고해야 한다
            error(f"✗ {name} - 에러 발생")
            error(f"  {err}\n")
            failed += 1

    title("=== 테스트 결과 ===")
    success(f"통과: {passed}개")
    if failed > 0:
        error(f"실패: {failed}개")
    print(f"총 {len(test_cases)}개\n")
