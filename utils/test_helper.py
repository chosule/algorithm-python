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


def _short(value: Any, limit: int = 120) -> str:
    """큰 입력/결과가 터미널을 덮지 않도록 repr을 잘라낸다."""
    text = repr(value)
    return text if len(text) <= limit else f"{text[:limit]}... (총 {len(value)}개)" if hasattr(value, "__len__") else f"{text[:limit]}..."


def _run_one(solution: Callable, test_cases: list[TestCase]) -> tuple[int, int, float]:
    """테스트 케이스를 한 벌 실행하고 (통과, 실패, 총 실행시간ms)을 돌려준다."""
    passed = 0
    failed = 0
    total_ms = 0.0

    for index, case in enumerate(test_cases):
        name = case.name or f"테스트 케이스 {index + 1}"
        args = _as_args(case.input)

        try:
            start = time.perf_counter()
            result = solution(*args)
            elapsed_ms = (time.perf_counter() - start) * 1000
            total_ms += elapsed_ms

            if result == case.expected:
                success(f"✓ {name}")
                info(f"  실행 시간: {elapsed_ms:.4f}ms")
                print(f"  결과: {_short(result)}\n")
                passed += 1
            else:
                error(f"✗ {name}")
                warn(f"  예상: {_short(case.expected)}")
                warn(f"  실제: {_short(result)}")
                info(f"  실행 시간: {elapsed_ms:.4f}ms\n")
                failed += 1
        except Exception as err:  # noqa: BLE001 - 테스트 러너는 모든 예외를 잡아서 보고해야 한다
            error(f"✗ {name} - 에러 발생")
            error(f"  {err}\n")
            failed += 1

    return passed, failed, total_ms


def run_tests(solution: Callable | dict[str, Callable], test_cases: list[TestCase]) -> None:
    """풀이 하나, 또는 {이름: 풀이} 여러 개를 같은 테스트 케이스로 실행한다.

    여러 개를 넘기면 접근법별로 나눠 실행하고 마지막에 속도를 비교한다.
        run_tests(solution, test_cases)
        run_tests({"브루트포스": solution_bruteforce, "스택": solution}, test_cases)
    """
    solutions = solution if isinstance(solution, dict) else {"": solution}
    multi = len(solutions) > 1
    totals: dict[str, float] = {}

    for label, fn in solutions.items():
        title(f"=== {label or '테스트'} 시작 ===\n")
        passed, failed, total_ms = _run_one(fn, test_cases)
        totals[label] = total_ms

        title(f"=== {label or '테스트'} 결과 ===")
        success(f"통과: {passed}개")
        if failed > 0:
            error(f"실패: {failed}개")
        print(f"총 {len(test_cases)}개 · 합계 {total_ms:.4f}ms\n")

    if multi:
        _print_comparison(totals)


def _print_comparison(totals: dict[str, float]) -> None:
    """접근법별 총 실행시간을 가장 빠른 쪽 기준으로 비교해 보여준다."""
    title("=== 속도 비교 ===")
    fastest = min(totals.values())
    width = max(len(label) for label in totals)
    for label, total_ms in sorted(totals.items(), key=lambda item: item[1]):
        # ponytail: 테스트 케이스가 작으면 배수가 흔들린다. 경향만 보는 용도.
        ratio = f"{total_ms / fastest:.1f}x" if fastest > 0 else "-"
        line = f"  {label:<{width}}  {total_ms:9.4f}ms  {ratio:>6}"
        success(line) if total_ms == fastest else print(line)
    print()
