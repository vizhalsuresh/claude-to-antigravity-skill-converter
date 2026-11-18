"""
converter.py — Claude-to-Antigravity Skill Compiler

Translates qualitative prompt skills into formal mathematical specifications
and constraint assertions for Antigravity agentic AI runtimes.
"""

import os
import sys
import re
import argparse
from typing import List, Tuple

# Abstract transformation rules: qualitative descriptions -> formal constraints
GENERAL_TRANSFORMS: List[Tuple[str, str]] = [
    (r"\b(smooth and organic|organic feel|natural movement)\b",
     "stochastically perturbed via Fractional Brownian Motion (amplitude=[0.03L, 0.08L])"),
    (r"\b(slight wobble|hand-drawn wobble|gentle jitter)\b",
     "deterministic coordinate offset: P'(t) = P(t) + sum(A_k * sin(k * w * t + phi_k))"),
    (r"\b(curved edges|subtly curved|rounded corners)\b",
     "Bézier secant offset: quadratic control point offset d_perp in [0.06L, 0.12L] perpendicular to secant"),
    (r"\b(avoid straight lines|no ruler lines)\b",
     "INVARIANT: Pure linear commands with zero curvature are FORBIDDEN"),
    (r"\b(balanced composition|centered layout)\b",
     "Golden-Ratio Spatial Tensor: hero mass centroid X_c in [0.28W, 0.38W] or [0.62W, 0.72W]; central quadrant [0.40W, 0.60W] is prohibited"),
    (r"\b(cinematic timing|natural pacing)\b",
     "Kinematic Tension Curve: anticipation recoil (-8%), velocity acceleration (via non-linear spring), and viscous decay"),
    (r"\b(generic output|ai slop|boilerplate)\b",
     "statistical mean collapse (0σ - 1σ peak probability token clustering)"),
]

DIRECTIVE_HEADER = """
## [COGNITIVE DIRECTIVE: ANTIGRAVITY DIVERGENCE ENGINE]

### 1. MANDATORY GATE 0: THE CLICHÉ PURGE (NEGATIVE REINFORCEMENT)
Before generating code or design layouts, the model must output the 3 highest-probability boilerplate solutions into a banned buffer:
```json
{
  "forbidden_slop_buffer": {
    "cliche_1_layout": "Default centered coordinates [0.5W, 0.5H]",
    "cliche_2_palette": "Default neutral/uncalibrated color hexes",
    "cliche_3_motion": "Symmetrical 0.3s ease-in-out or unconstrained sine waves"
  }
}
```
**BUFFER_LOCK**: All tokens listed in the buffer are strictly prohibited from the final output.

### 2. FORMAL CONSTRAINTS & MATHEMATICAL BOUNDS
- **Spatial Centroid**: The primary visual focal point must not reside in the dead-center quadrant. Anchor to Golden Ratio nodes: `(0.382W, 0.618H)` or `(0.618W, 0.382H)`.
- **Dynamic Tension**: Motion curves must enforce asymmetric velocity profiles with steep initial slopes and viscous settle. Zero linear transitions.
- **Color Metric**: Maintain high contrast ratio (CIELAB ΔE*ab >= 45.0) between primary foreground and substrate.

### 3. TWO-BRAIN PROTOCOL
- **Brain 1 (Generative)**: Dedicated to creative synthesis without writing test assertions.
- **Brain 2 (Deterministic)**: Local sub-50ms AST and boundary verification script running with zero token overhead.
"""

def convert_skill_text(raw_text: str) -> str:
    """Transforms qualitative skill text into formal Antigravity-native specifications."""
    text = raw_text
    
    for pattern, replacement in GENERAL_TRANSFORMS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
    text = re.sub(r"\bClaude\b", "Antigravity", text)
    text = re.sub(r"\bGemini\b", "Antigravity", text)
    
    frontmatter_match = re.match(r"^(---\s*\n.*?\n---\s*\n)", text, re.DOTALL)
    if frontmatter_match:
        fm = frontmatter_match.group(1)
        body = text[len(fm):]
        # Preserve valid YAML formatting using block scalar
        fm = re.sub(
            r"description:\s*(['\"].*?['\"]|.*?)\n",
            r"description: >-\n  \1 (Reinforced with Antigravity mathematical invariants)\n",
            fm
        )
        return fm + "\n" + DIRECTIVE_HEADER.strip() + "\n\n" + body.lstrip()
    else:
        return DIRECTIVE_HEADER.strip() + "\n\n" + text

def main():
    parser = argparse.ArgumentParser(description="Convert qualitative skills to Gemini-native invariant skills")
    parser.add_argument("input_path", help="Path to input qualitative SKILL.md")
    parser.add_argument("-o", "--output", help="Destination path for converted Gemini SKILL.md")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_path):
        print(f"Error: Input file '{args.input_path}' not found.", file=sys.stderr)
        sys.exit(1)
        
    with open(args.input_path, "r", encoding="utf-8") as f:
        original = f.read()
        
    converted = convert_skill_text(original)
    out_path = args.output or f"{os.path.splitext(args.input_path)[0]}.gemini.md"
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(converted)
        
    print(f"[SUCCESS] Converted: {args.input_path} -> {out_path}")

if __name__ == "__main__":
    main()
