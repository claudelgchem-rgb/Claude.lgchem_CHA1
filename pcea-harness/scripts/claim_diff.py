#!/usr/bin/env python3
"""claim_diff.py — verbatim 일치 강제 장치 (PCEA Harness)

청구항 두 텍스트를 **있는 그대로** 문자 단위로 비교한다.
이 스크립트는 PCEA 하니스의 "사람이 아니라 코드가 비교한다" 원칙을 구현한다.

핵심 규칙:
  * 정규화 없음. 공백·문장부호·줄바꿈·대소문자를 절대 무시하지 않는다.
    청구항에서는 쉼표 하나, 세미콜론 하나, comprising vs consisting 하나가
    권리범위를 바꾼다. 따라서 그것들이 곧 비교 대상이다.
  * 단 한 글자라도 다르면 MISMATCH (exit code 1).
  * 완전히 동일하면 MATCH (exit code 0).
  * 파일 접근 오류 등은 exit code 2.

사용법:
  python scripts/claim_diff.py --a fileA.txt --b fileB.txt
  python scripts/claim_diff.py --a fileA.txt --b fileB.txt --json
  python scripts/claim_diff.py --a-text "..." --b-text "..."   # 인라인 비교

종료 코드:
  0 = 완전 일치 (MATCH)
  1 = 불일치 (MISMATCH)
  2 = 사용 오류 / 파일 접근 오류
"""

import argparse
import difflib
import json
import sys


def read_source(path, inline_text, label):
    """파일 경로 또는 인라인 텍스트에서 원문을 읽는다. 정규화하지 않는다."""
    if path is not None and inline_text is not None:
        raise ValueError(f"{label}: 파일과 인라인 텍스트를 동시에 줄 수 없습니다.")
    if path is not None:
        # newline='' 으로 줄바꿈 문자를 변환하지 않고 그대로 보존한다.
        with open(path, "r", encoding="utf-8", newline="") as fh:
            return fh.read()
    if inline_text is not None:
        return inline_text
    raise ValueError(f"{label}: --{label} 또는 --{label}-text 중 하나가 필요합니다.")


def compare(text_a, text_b, name_a, name_b):
    """두 텍스트를 변형 없이 비교하고 결과 dict 를 반환한다."""
    identical = text_a == text_b

    # 라인 단위 unified diff (사람이 읽기 좋은 형태).
    # keepends=True 로 줄바꿈 차이까지 보이게 한다.
    diff_lines = list(
        difflib.unified_diff(
            text_a.splitlines(keepends=True),
            text_b.splitlines(keepends=True),
            fromfile=name_a,
            tofile=name_b,
            lineterm="",
        )
    )

    # 첫 번째로 갈라지는 문자 위치(가장 작은 차이도 잡아내기 위함).
    first_diff_index = None
    if not identical:
        min_len = min(len(text_a), len(text_b))
        for i in range(min_len):
            if text_a[i] != text_b[i]:
                first_diff_index = i
                break
        if first_diff_index is None:
            # 한쪽이 다른 쪽의 접두어인 경우 (길이만 다름).
            first_diff_index = min_len

    return {
        "result": "MATCH" if identical else "MISMATCH",
        "identical": identical,
        "len_a": len(text_a),
        "len_b": len(text_b),
        "first_diff_char_index": first_diff_index,
        "unified_diff": "".join(diff_lines),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="청구항 두 텍스트를 정규화 없이 문자 단위로 비교한다 (verbatim 강제)."
    )
    parser.add_argument("--a", dest="a_path", help="비교 대상 A 파일 경로")
    parser.add_argument("--b", dest="b_path", help="비교 대상 B 파일 경로")
    parser.add_argument("--a-text", dest="a_text", help="비교 대상 A 인라인 텍스트")
    parser.add_argument("--b-text", dest="b_text", help="비교 대상 B 인라인 텍스트")
    parser.add_argument(
        "--json", action="store_true", help="결과를 JSON 으로 출력 (에이전트 파싱용)"
    )
    args = parser.parse_args(argv)

    try:
        text_a = read_source(args.a_path, args.a_text, "a")
        text_b = read_source(args.b_path, args.b_text, "b")
    except (ValueError, OSError) as exc:
        if args.json:
            print(json.dumps({"result": "ERROR", "error": str(exc)}, ensure_ascii=False))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    name_a = args.a_path or "A(inline)"
    name_b = args.b_path or "B(inline)"
    report = compare(text_a, text_b, name_a, name_b)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"RESULT: {report['result']}")
        print(f"len(A)={report['len_a']}  len(B)={report['len_b']}")
        if not report["identical"]:
            print(f"first differing char index: {report['first_diff_char_index']}")
            print("----- unified diff -----")
            print(report["unified_diff"])

    return 0 if report["identical"] else 1


if __name__ == "__main__":
    sys.exit(main())
