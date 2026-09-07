"""
저장된 정답(problems/)에서 solution 함수의 본문만 지운 연습용 파일을
practice/ 아래에 생성한다. 문제 설명과 테스트 케이스는 그대로 유지되고
풀이 코드만 안 보이는 상태로 다시 풀어볼 수 있다.

사용법:
  python3 scripts/practice.py array/two_sum          # practice/array/two_sum.py 생성 (이미 있으면 건너뜀)
  python3 scripts/practice.py array/two_sum --force   # 이미 있어도 덮어써서 초기화
  python3 scripts/practice.py --all                   # problems/ 전체를 practice/ 에 생성 (이미 있는 건 건너뜀)
"""

import argparse
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
PRACTICE_DIR = ROOT / "practice"


def build_practice_source(source: str) -> str:
    """solution 함수의 시그니처만 남기고 본문(docstring 포함)을 TODO 스텁으로 교체한다."""
    tree = ast.parse(source)
    solution_fn = next(
        (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "solution"),
        None,
    )
    if solution_fn is None:
        raise ValueError("solution 함수를 찾을 수 없습니다")

    lines = source.splitlines(keepends=True)
    body_start = solution_fn.body[0].lineno  # 1-indexed
    body_end = solution_fn.end_lineno  # 1-indexed, inclusive
    indent = " " * (solution_fn.col_offset + 4)
    stub_body = f"{indent}pass  # TODO: 여기에 코드를 작성하세요\n"

    return "".join(
        lines[: solution_fn.lineno - 1]  # def solution(...): 앞부분 그대로
        + lines[solution_fn.lineno - 1 : body_start - 1]  # 시그니처(여러 줄 가능) 유지
        + [stub_body]
        + lines[body_end:]  # 함수 이후(테스트 케이스, main 블록 등) 그대로
    )


def make_practice_file(problem_path: Path, force: bool) -> str:
    rel = problem_path.relative_to(PROBLEMS_DIR)
    target = PRACTICE_DIR / rel
    if target.exists() and not force:
        return f"건너뜀 (이미 있음): {rel}"

    practice_source = build_practice_source(problem_path.read_text(encoding="utf-8"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(practice_source, encoding="utf-8")
    return f"생성됨: {rel}"


def main():
    parser = argparse.ArgumentParser(description="정답을 숨긴 연습용 파일 생성")
    parser.add_argument("problem", nargs="?", help="예: array/two_sum (확장자 생략)")
    parser.add_argument("--all", action="store_true", help="problems/ 전체 처리")
    parser.add_argument("--force", action="store_true", help="이미 있어도 덮어써서 초기화")
    args = parser.parse_args()

    if args.all:
        targets = sorted(
            p for p in PROBLEMS_DIR.rglob("*.py") if p.name != "__init__.py"
        )
        if not targets:
            print("problems/ 아래에 문제가 없습니다.")
            sys.exit(0)
    elif args.problem:
        candidate = PROBLEMS_DIR / f"{args.problem}.py"
        if not candidate.exists():
            print(f"문제를 찾을 수 없음: {candidate.relative_to(ROOT)}")
            sys.exit(1)
        targets = [candidate]
    else:
        parser.print_help()
        sys.exit(1)

    for target in targets:
        print(make_practice_file(target, args.force))


if __name__ == "__main__":
    main()
