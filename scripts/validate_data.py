#!/usr/bin/env python3
"""Dependency-free, offline validation of HilfeNetz's public JSON datasets."""
import json
from datetime import date
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []
def fail(msg):
    errors.append(msg)
def load(name):
    try:
        return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail(f"{name}: invalid JSON: {exc}")
        return {}
def valid_url(value):
    p = urlparse(str(value))
    return p.scheme == "https" and bool(p.netloc) and not p.username and not p.password
def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        return False
    try:
        return date.fromisoformat(value) <= date.today()
    except ValueError:
        return False
def valid_phone(value):
    return isinstance(value, str) and bool(re.fullmatch(r"\+?[0-9][0-9 ()/.-]*", value.strip())) and 3 <= len(re.sub(r"\D", "", value)) <= 20

def valid_email(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value.strip()))

def check_contact_fields(row, prefix):
    for key in ("phone", "email", "hours"):
        if key not in row or row[key] is None or row[key] == "":
            continue
        value = row[key]
        if key == "phone" and not valid_phone(value):
            fail(f"{prefix}: invalid phone format")
        elif key == "email" and not valid_email(value):
            fail(f"{prefix}: invalid email format")
        elif key == "hours" and (not isinstance(value, str) or not value.strip()):
            fail(f"{prefix}: invalid hours text")
    extras = row.get("extra_contacts", [])
    if not isinstance(extras, list):
        fail(f"{prefix}: extra_contacts must be a list")
    else:
        for j, extra in enumerate(extras):
            if not isinstance(extra, dict):
                fail(f"{prefix}: extra_contacts[{j}] must be an object")
            else:
                check_contact_fields(extra, f"{prefix} extra_contacts[{j}]")

locations = load("standorte.json").get("locations", [])
seen = set()
for i, row in enumerate(locations):
    prefix = f"standorte.json locations[{i}]"
    for key in ("name", "city", "postal_code", "address", "url", "source_url", "verified_on"):
        if not isinstance(row.get(key), str) or not row[key].strip():
            fail(f"{prefix}: missing {key}")
    if not re.fullmatch(r"\d{5}", str(row.get("postal_code", ""))):
        fail(f"{prefix}: invalid German postal code")
    for key in ("url", "source_url"):
        if row.get(key) and not valid_url(row[key]):
            fail(f"{prefix}: invalid {key}")
    if row.get("verified_on") and not valid_date(row["verified_on"]):
        fail(f"{prefix}: invalid verified_on")
    check_contact_fields(row, prefix)
    ident = (str(row.get("name", "")).casefold().strip(), str(row.get("address", "")).casefold().strip())
    if ident in seen:
        fail(f"{prefix}: duplicate name/address")
    seen.add(ident)
contacts = load("kontakte.json").get("entries", {})
if not isinstance(contacts, dict):
    fail("kontakte.json: entries must be an object")
else:
    for name, row in contacts.items():
        if not isinstance(row, dict):
            fail(f"kontakte.json {name}: not an object")
            continue
        check_contact_fields(row, f"kontakte.json {name}")
        if row.get("verified_on") and not valid_date(row["verified_on"]):
            fail(f"kontakte.json {name}: invalid or future verified_on")
        for key in ("contact_url", "source_url"):
            if row.get(key) and not valid_url(row[key]):
                fail(f"kontakte.json {name}: invalid {key}")
print(f"Checked {len(locations)} locations and {len(contacts)} contact entries.")
if errors:
    print("\n".join("ERROR: " + e for e in errors))
    raise SystemExit(1)
print("PASS: offline JSON/schema/duplicate checks")
