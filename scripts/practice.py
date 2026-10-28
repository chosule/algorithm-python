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


STUB = "pass  # TODO: 여기에 코드를 작성하세요"


def _blank_body(fn) -> tuple[int, int, list[str]]:
    """함수/메서드 본문(docstring 포함) 전체를 TODO 스텁 한 줄로 바꾸는 구간을 만든다."""
    indent = " " * (fn.col_offset + 4)
    return (fn.body[0].lineno, fn.end_lineno, [f"{indent}{STUB}\n"])


def _regions(tree) -> list[tuple[int, int, list[str]]]:
    """지워야 할 구간 목록. 최상위 solution 함수 + 최상위 클래스의 docstring/메서드 전부.

    클래스가 있는 설계 문제에서 solution은 풀이가 아니라 연산을 재생하는 테스트 드라이버라서 남긴다.
    """
    regions = []
    found_solution = False
    has_class = any(isinstance(node, ast.ClassDef) for node in tree.body)

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "solution":
            if not has_class:
                regions.append(_blank_body(node))
            found_solution = True
        elif isinstance(node, ast.ClassDef):
            # 클래스 docstring에 접근 방법이 적혀 있으므로 같이 지운다.
            doc = node.body[0]
            if isinstance(doc, ast.Expr) and isinstance(doc.value, ast.Constant) and isinstance(doc.value.value, str):
                regions.append((doc.lineno, doc.end_lineno, []))
            regions.extend(
                _blank_body(m) for m in node.body if isinstance(m, ast.FunctionDef)
            )

    if not found_solution:
        raise ValueError("solution 함수를 찾을 수 없습니다")
    return regions


def build_practice_source(source: str) -> str:
    """풀이 코드(solution 함수, 클래스 메서드)의 본문을 TODO 스텁으로 교체한다.

    문제 설명 docstring, 테스트 케이스, main 블록, 함수/메서드 시그니처는 그대로 둔다.
    """
    lines = source.splitlines(keepends=True)
    # 뒤에서부터 잘라내야 앞쪽 구간의 줄 번호가 밀리지 않는다.
    for start, end, replacement in sorted(_regions(ast.parse(source)), reverse=True):
        lines[start - 1 : end] = replacement
    return "".join(lines)


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
