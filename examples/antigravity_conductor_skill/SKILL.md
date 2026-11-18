---
name: antigravity-conductor
description: >-
  Executive runtime conductor and anti-slop enforcer for Antigravity agents. Enforces the Gate 0 Cliché Purge, mathematical invariants, zero-token AST verification, and single-frame visual inspection on all creative and code tasks.
---

# Antigravity Conductor: Executive Runtime Enforcer

> **PURPOSE**: Guides agentic models to produce high-taste, mathematically grounded creative outputs while eliminating generic boilerplate and avoiding recursive token-burning test loops.

---

## The 4-Gate Execution Protocol

Execute these 4 gates in strict sequence for any visual, motion, or code generation task:

### Gate 0: The Cliché Purge & Entropy Seed
Before writing production files, output the 3 most common, default solutions into the `forbidden_slop_buffer`:
```json
{
  "gate_0_cliche_purge": {
    "cliche_1_layout": "Default centered alignment [0.5W, 0.5H]",
    "cliche_2_palette": "Standard uncalibrated neutral hexes",
    "cliche_3_motion": "Symmetrical 0.3s ease-in-out transition"
  }
}
```
Optionally derive an external physical seed:
```bash
python3 entropy.py --context "scene description"
```

### Gate 1: Constraint-Bounded Generation (Brain 1)
- Write the target component code adhering strictly to the mathematical constraints in the active skill.
- **Rules**: Zero linear transitions, enforce Golden-Ratio spatial centroids, enforce contrast ratio ($\Delta E \ge 45.0$).
- **No Test Suites**: Brain 1 is strictly prohibited from writing unit tests or mock assertion harnesses in its generation turn.

### Gate 2: Zero-Token Deterministic Audit (Brain 2)
Run the local static auditor before rendering or running code:
```bash
python3 auditor.py path/to/generated_component.tsx
```
If violations are detected, patch only the flagged lines without altering creative coordinates.

### Gate 3: Single-Frame Visual Proof
Render a single still frame at the hero beat and present the image path for human inspection before committing to multi-frame production.
