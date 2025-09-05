
# 🧬 LifeOS — Getting Started Guide

Welcome to **LifeOS**, a human-inspired life simulation engine rooted in modular traits, DNA-level logic, and community interaction.

This document will guide you through getting started, running simulations, and modifying key modules.

---

## ⚡ Quickstart

If you're just here to see it run:

```bash
git clone https://github.com/FrankoMcNally/LifeOS.git
cd LifeOS
pip install -r requirements.txt
python run.py
```

---

## 🔧 Installation

To install the dependencies, ensure you're using Python 3.9+ and run:

```bash
pip install -r requirements.txt
```

Make sure you are in the project root directory when executing any commands.

---

## 🚀 Running Your First Simulation

LifeOS comes with a ready-to-run test script:

```bash
python run.py
```

This runs a continuous simulation loop (100 iterations by default) using internal modules like:

- ConsciousnessMap
- TraitCompiler
- ResonanceMath
- FreeWillResolver
- InstinctMatrix
- FaultPainDetector
- SymbolicLanguageEngine

Example output is printed to the terminal to help visualize the behavior.

---

## 🔬 Customizing Traits & Community Behavior

You can adjust simulation behavior using parameters in:

- `examples/example_1_high_stress_scenario.py`
- `community_traits/*.json` files

For example, modify `social_instincts.json` to adjust default population traits, behaviors, or personality profiles.

---

## 🧪 Testing

Run the test suite with:

```bash
pytest tests/
```

---

## 📁 Folder Overview

| Folder                  | Description |
|-------------------------|-------------|
| `src/`                 | Core logic and simulation modules |
| `examples/`            | Example simulation scripts |
| `community_traits/`    | Sample trait configurations |
| `tests/`               | Unit tests |
| `docs/`                | Whitepaper and extended documentation |
| `lifeos-banner.png`    | Repo banner (used in README) |
| `run.py`               | Main continuous simulation entry point |

---

## 🛠 Next Steps

- Explore the `src/kernel/` modules to understand the core brain logic.
- Experiment with modifying traits in `src/traits/` and watching how behavior changes.
- Try swapping out example JSON files to simulate different communities or stress scenarios.

---

## 👁‍🗨 Note

Some advanced modules (like `EvolutionEngine`, `CreativityEngine`) are currently stubbed. They serve as placeholders for future development and won’t affect initial simulations.

---

Enjoy simulating with **LifeOS** — and thank you for contributing to a better understanding of conscious systems.
