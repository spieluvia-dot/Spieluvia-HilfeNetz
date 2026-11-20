#!/usr/bin/env python3
"""Negative regression tests for the offline data validator (stdlib only)."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data"

def run_case(label, mutate, expected):
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        (work / "scripts").mkdir()
        (work / "data").mkdir()
        shutil.copy2(ROOT / "scripts" / "validate_data.py", work / "scripts" / "validate_data.py")
        for name in ("standorte.json", "kontakte.json"):
            (work / "data" / name).write_bytes((BASE / name).read_bytes())
        path = work / "data" / "standorte.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        mutate(data["locations"][0])
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        result = subprocess.run([sys.executable, str(work / "scripts" / "validate_data.py")],
                                capture_output=True, text=True, check=False)
        output = result.stdout + result.stderr
        assert result.returncode != 0 and expected in output, (
            f"{label}: expected rejection containing {expected!r}; got rc={result.returncode}: {output}"
        )
        print(f"PASS: rejects {label}")

def main():
    clean = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_data.py")],
                           capture_output=True, text=True, check=False)
    assert clean.returncode == 0, f"Baseline data must pass: {clean.stdout} {clean.stderr}"
    run_case("invalid phone", lambda row: row.update(phone="abc"), "invalid phone format")
    run_case("invalid email", lambda row: row.update(email="invalid-address"), "invalid email format")
    run_case("invalid hours type", lambda row: row.update(hours=["Monday"]), "invalid hours text")
    run_case("invalid extra contacts type", lambda row: row.update(extra_contacts={}), "extra_contacts must be a list")
    run_case("invalid nested contact", lambda row: row.update(extra_contacts=[{"phone": "bad"}]), "invalid phone format")
    print("PASS: validator negative regression suite")

if __name__ == "__main__":
    main()
