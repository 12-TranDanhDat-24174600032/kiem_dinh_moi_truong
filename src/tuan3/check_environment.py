#!/usr/bin/env python3
"""
check_environment.py
Kiểm tra tối thiểu môi trường làm việc cho TCS_K20 - Chương 1.

Cách chạy từ thư mục gốc project:
    python src/check_environment.py

Script chỉ kiểm tra:
- thư mục hiện hành có phải thư mục gốc project hay không;
- có đủ các thư mục src/, data/, output/, docs/;
- có tệp data/students_utf8.csv;
- Python đang chạy có thuộc .venv của project;
- pip có hoạt động với chính interpreter đang dùng;
- phiên bản và đường dẫn Python.

PASS chỉ xác nhận các điều kiện trên, không khẳng định dataset đúng nội dung
hoặc mọi cấu hình VS Code đều hoàn hảo.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

CHECKER_VERSION = "2026-10-01-R3"


def show(status: str, label: str, detail: str = "") -> None:
    suffix = f" — {detail}" if detail else ""
    print(f"[{status}] {label}{suffix}")


def main() -> int:
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    cwd = Path.cwd().resolve()
    venv_dir = project_root / ".venv"

    checks = []

    checks.append(
        ("Thư mục hiện hành", cwd == project_root.resolve(), str(cwd))
    )

    for folder_name in ("src", "data", "output", "docs"):
        folder = project_root / folder_name
        checks.append(
            (f"Thư mục {folder_name}/", folder.is_dir(), str(folder))
        )

    dataset = project_root / "data" / "students_utf8.csv"
    checks.append(
        ("Dataset students_utf8.csv", dataset.is_file(), str(dataset))
    )

    # Không dùng Path(sys.executable).resolve() để xác định môi trường ảo.
    # Trên Ubuntu, .venv/bin/python thường là symbolic link trỏ tới
    # /usr/bin/python3.x; resolve() sẽ lần theo liên kết và gây FAIL giả.
    # sys.prefix là thư mục của môi trường Python đang chạy, còn
    # sys.base_prefix là thư mục của Python nền dùng để tạo môi trường đó.
    python_exe = Path(sys.executable)
    active_prefix = Path(sys.prefix).resolve()
    expected_prefix = venv_dir.resolve()
    in_virtual_environment = sys.prefix != sys.base_prefix
    correct_project_venv = active_prefix == expected_prefix
    checks.append(
        (
            "Python thuộc .venv của project",
            (
                venv_dir.is_dir()
                and in_virtual_environment
                and correct_project_venv
            ),
            str(python_exe),
        )
    )

    try:
        proc = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        pip_ok = proc.returncode == 0
        pip_detail = (proc.stdout or proc.stderr).strip()
    except Exception as exc:
        pip_ok = False
        pip_detail = f"{type(exc).__name__}: {exc}"

    checks.append(("pip của interpreter đang dùng", pip_ok, pip_detail))

    print("=== TCS_K20 · CHECK ENVIRONMENT ===")
    print(f"Checker      : {CHECKER_VERSION}")
    print(f"Project root : {project_root}")
    print(f"Python       : {sys.version.split()[0]}")
    print(f"Executable   : {sys.executable}")
    print(f"sys.prefix   : {sys.prefix}")
    print(f"Expected venv: {expected_prefix}")
    print()

    passed = 0
    for label, ok, detail in checks:
        if ok:
            passed += 1
            show("PASS", label, detail)
        else:
            show("FAIL", label, detail)

    total = len(checks)
    print()
    if passed == total:
        print(f"RESULT: PASS — {passed}/{total} điều kiện đạt.")
        print("Lưu ý: PASS chỉ xác nhận đúng phạm vi mà script này kiểm tra.")
        return 0

    print(f"RESULT: FAIL — {passed}/{total} điều kiện đạt.")
    if not correct_project_venv:
        print()
        print("NGUYÊN NHÂN: Chương trình không chạy bằng Python của .venv trong project.")
        print("CÁCH CHẠY ĐÚNG:")
        print(f"  cd {project_root}")
        print("  source .venv/bin/activate")
        print("  python src/check_environment.py")
    else:
        print("Hãy xem từng dòng FAIL phía trên để xác định điều kiện chưa đạt.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
