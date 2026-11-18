"""
entropy.py — Standalone Procedural Entropy Generator

Provides deterministic, physical-regime seed values for layout, timing,
and coordinate perturbation to push generative models away from the statistical mean.
"""

import sys
import random
import hashlib
import argparse

REGIMES = [
    {
        "family": "Print & Paint",
        "description": "Uneven ink absorption, mechanical misregistration, plate chatter, paper tooth",
        "parameters": {"roughness": 0.08, "bleed_px": 2.4, "taper": "ragged"}
    },
    {
        "family": "Screens & Machines",
        "description": "Phosphor bloom, subpixel chromatic separation, scanline rasterization, LED matrix",
        "parameters": {"bloom_sigma": 1.8, "scanline_density": 0.45, "chroma_split_px": 1.5}
    },
    {
        "family": "Camera & Science",
        "description": "Sensor photon noise, lens barrel distortion, optical vignetting, telemetry verniers",
        "parameters": {"noise_floor": 0.04, "barrel_k1": -0.06, "vignette_falloff": 0.32}
    },
    {
        "family": "Material & Light",
        "description": "Specular caustics, volumetric refraction, structural seams, faceted edge-wear",
        "parameters": {"caustic_scale": 14.0, "refract_ior": 1.45, "bevel_radius": 0.05}
    }
]

def generate_entropy(context: str = "") -> dict:
    """Generates a structured entropy package based on an optional context string."""
    seed_source = context if context else str(random.random())
    digest = hashlib.sha256(seed_source.encode("utf-8")).hexdigest()
    int_seed = int(digest[:8], 16)
    
    rng = random.Random(int_seed)
    chosen_regime = rng.choice(REGIMES)
    
    return {
        "seed": int_seed,
        "family": chosen_regime["family"],
        "description": chosen_regime["description"],
        "parameters": chosen_regime["parameters"],
        "golden_ratio_offset": (round(rng.uniform(0.28, 0.38), 3), round(rng.uniform(0.62, 0.72), 3))
    }

def main():
    parser = argparse.ArgumentParser(description="Standalone Procedural Entropy Generator")
    parser.add_argument("--context", default="", help="Context string to deterministically derive entropy")
    args = parser.parse_args()
    
    result = generate_entropy(args.context)
    print(f"Entropy Seed: {result['seed']}")
    print(f"Physical Regime: {result['family']}")
    print(f"Characteristics: {result['description']}")
    print(f"Recommended Spatial Nodes: {result['golden_ratio_offset']}")

if __name__ == "__main__":
    main()
