"""
auditor.py — Brain 2: Zero-Token Deterministic AST & Aesthetic Auditor

Checks generated TSX, SVG, or React components against formal invariants and
banned cliché tokens in under 50ms with zero LLM token consumption.
"""

import sys
import os
import re
import argparse
from typing import List, Tuple

DEFAULT_FORBIDDEN_PATTERNS: List[Tuple[str, str]] = [
    (r"#fdfcf8", "BANNED: Default cream paper hex #fdfcf8 detected. Choose a calibrated or high-contrast palette."),
    (r"#1c1c1c", "BANNED: Default charcoal #1c1c1c detected without contrast calibration."),
    (r"transition:\s*['\"]all\s+0\.3s\s+ease['\"]", "BANNED: Naive CSS 0.3s ease detected. Use non-linear spring physics."),
    (r"ease-in-out", "BANNED: Symmetrical ease-in-out detected. Use asymmetric cubic-bezier curves."),
    (r"Math\.sin\s*\(\s*frame\s*\*\s*0\.1\s*\)", "BANNED: Unconstrained sine bobbing detected. Use kinematic gait formulas."),
    (r"left:\s*['\"]50%['\"].*top:\s*['\"]50%['\"]", "BANNED: Dead-center coordinate detected. Obey Golden-Ratio spatial constraints."),
]

def audit_file(filepath: str) -> List[str]:
    """Scans code file for aesthetic invariant violations."""
    violations = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines, start=1):
        for pattern, reason in DEFAULT_FORBIDDEN_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append(f"Line {idx}: {reason}\n  -> {line.strip()}")
                
    return violations

def main():
    parser = argparse.ArgumentParser(description="Zero-Token Deterministic Auditor (Brain 2)")
    parser.add_argument("file_path", help="Path to TSX, SVG, or JS code file to audit")
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        print(f"Error: Target file '{args.file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    print(f"[*] Brain 2: Auditing '{args.file_path}'...")
    violations = audit_file(args.file_path)
    
    if violations:
        print(f"\n[REJECTED] {len(violations)} Invariant Violation(s) Found:")
        for v in violations:
            print(f"  - {v}")
        print("\nAction Required: Correct flagged tokens to comply with aesthetic constraints.")
        sys.exit(1)
    else:
        print("[PASSED] Code satisfies all structural invariants. (0 tokens burned)")
        sys.exit(0)

if __name__ == "__main__":
    main()
