# Claude-to-Gemini Skill Converter (C2G)

> **Transforming Qualitative Agent Skills into Formal Mathematical Invariants for Gemini Flash.**

---

## The Cognitive Gap: Why Claude Skills Fail on Gemini

Anthropic's **Claude** and Google DeepMind's **Gemini** possess fundamentally different cognitive priors:

* **Claude** was trained with strong literary, conversational, and aesthetic reinforcement. When Claude reads human workshop metaphors (*"make lines bow slightly with gentle organic wobble"*), it interprets them as stylistic constraints and naturally produces nuanced, tasteful outputs.
* **Gemini Flash**, by contrast, is a high-throughput Mixture-of-Experts (MoE) engine optimized for formal logic, mathematical proofs, software engineering benchmarks, and strict safety compliance. 

When Gemini encounters qualitative adjectives, its attention heads compute diffuse weights and fall back to the **statistical mean of GitHub** ($0\sigma$ to $1\sigma$ on the token probability curve):
- Standard centered layouts (`x: 50%, y: 50%`)
- Default beige/cream paper (`#fdfcf8`) and dark charcoal ink (`#1c1c1c`)
- Symmetrical CSS easing (`0.3s ease`) or linear time progressions
- Token-burning testing loops where the model wastes thousands of tokens writing assertions rather than elevating artistic craft.

```
                       THE TOKEN PROBABILITY BELL CURVE
                       
                    THE SLOP ZONE
                     (The Mean μ)
                       0σ to 1σ
                     ┌───────────┐
                     │  Average  │
                     │  GitHub   │
                     │Boilerplate│
                     │  Default  │
        ─────────────┴───────────┴─────────────
       │                                       │
       ▼                                       ▼
THE GIBBERISH TAIL                       THE GOLDEN SWEET SPOT
   (Hallucination)                        (Aesthetic Mastery)
      > 3.5σ                                  1.5σ to 2.8σ
┌──────────────────┐                     ┌──────────────────────┐
│ Broken SVG syntax│                     │ Mathematical beauty  │
│ Hallucinated APIs│                     │ Non-linear dynamics  │
│ Syntax Errors    │                     │ Asymmetric tension   │
│ Chaos / Noise    │                     │ Rare, high-taste code│
└──────────────────┘                     └──────────────────────┘
```

**C2G** bridges this gap by acting as a **Semantic Lexical Compiler**, converting qualitative Claude `SKILL.md` files into formal mathematical specifications that Gemini natively commands.

---

## Core Architecture

### 1. The Rosetta Stone Translation
Replaces subjective prose with concrete parameter bounds, kinematic equations, and coordinate tensors:

| Qualitative Claude Phrase | Translated Gemini Mathematical Invariant |
| :--- | :--- |
| *"make it feel organic"* | Stochastic perturbation via Fractional Brownian Motion (octaves=3, amplitude=[0.03L, 0.08L]) |
| *"edges bow slightly"* | Bézier secant offset invariant: quadratic control point offset $d_{\perp} \in [0.06L, 0.12L]$ |
| *"feet that slide"* | Kinematic ground-lock: `ASSERT: Foot_Delta_X == 0 on Stance_Phase` |
| *"balanced layout"* | Golden-Ratio spatial tensor: centroid $X_c \in [0.28W, 0.38W]$; center quadrant $[0.40W, 0.60W]$ is banned |
| *"dramatic pacing"* | Kinematic envelope: 90ms negative recoil, 120ms velocity spike (82% distance), 350ms viscous decay |

### 2. Negative Conditioning: The Cliché Purge
Forces Gemini to output its 3 highest-probability boilerplate solutions into a `FORBIDDEN_SLOP_BUFFER` before writing production code. Every token in this buffer is strictly banned, shifting probability mass into the $1.5\sigma - 2.8\sigma$ sweet spot.

### 3. The Two-Brain Decoupling Protocol
* **Brain 1 (Generative Engine / LLM)**: Focuses 100% of compute on creative synthesis. Brain 1 is strictly forbidden from writing unit tests or assertions.
* **Brain 2 (Zero-Token Auditor / Python)**: Local sub-50ms AST and regex linter (`auditor.py`) that checks for banned tokens, contrast, and layout bounds with **zero token cost**.

---

## Installation & Quickstart

```bash
git clone https://github.com/vizhalsuresh/claude-to-gemini-skill-converter.git
cd claude-to-gemini-skill-converter
```

### 1. Convert a Claude Skill
```bash
python3 converter.py path/to/claude_skill/SKILL.md -o path/to/gemini_skill/SKILL.md
```

### 2. Run the Zero-Token Deterministic Auditor
```bash
python3 auditor.py path/to/generated_component.tsx
```

### 3. Generate Procedural Entropy Seeds
```bash
python3 entropy.py --context "astrophysics simulation scene"
```

---

## Repository Structure

```text
claude-to-gemini-skill-converter/
├── converter.py          # The core skill compiler
├── auditor.py            # Brain 2 zero-token deterministic AST checker
├── entropy.py            # Standalone procedural seed generator (4 physical regimes)
├── examples/             # Before/after conversion samples
│   ├── input_claude.md
│   └── output_gemini.md
├── LICENSE               # MIT License
└── README.md
```

---

## Inspiration & Attribution

This project is inspired by the anti-cliché, entropy-driven creative philosophy of [`mankidev/antialgorithm`](https://github.com/mankidev/antialgorithm). We extend those core anti-slop concepts into an automated compiler pipeline tailored for modern multimodal LLM agent runtimes.

---

## License

MIT License. Contributions, additional lexical transformations, and community PRs are welcome!
