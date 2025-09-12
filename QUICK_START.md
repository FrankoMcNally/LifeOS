
# 🚀 Quick Start Guide to LifeOS

Welcome to the **LifeOS Simulation Framework** — a digital experiment that models the evolution of life, behavior, and emotion based on encoded DNA traits.

This guide will walk you through getting started — **even if you’re not an expert**.

---

## 🧠 What is LifeOS?

LifeOS is a Python-based simulation that brings digital beings ("entities") to life using:

- Trait-based DNA blueprints
- Relationship dynamics (12 couples)
- Emotional patterns & harmonic scoring
- Emergent cultural and behavioral structures

Each day in the simulation, the beings **interact, evolve, and make decisions** based on internal code — not hardcoded behaviors.

---

## 🖥️ System Requirements

- Python 3.10 or later
- Git (to clone the repo)
- pip (Python package manager)

---

## 🛠️ Setup Instructions

### 1. 🔽 Clone the Repository

```bash
git clone https://github.com/your-username/LifeOS.git
cd LifeOS
```

### 2. 🧪 Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

### 3. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Your First Simulation

### Step 1: Animate a Single Being

This will generate and observe one entity with a core trait set.

```bash
python simulation_runner.py --mode single
```

Watch the console — you'll see how the being activates, selects traits, and interacts.

### Step 2: Start the 12 Couples Simulation

This is the full evolution model with bonding, offspring, rituals, etc.

```bash
python simulation_runner.py --mode couples
```

Each run represents a "Day".

> **Important**: The system tracks trait activation, emotional flow, pair bonding, and child creation in real-time.

---

## 📁 Project Structure Overview

```bash
LifeOS/
├── scr/                    # Core source files
│   ├── traits/             # Core, optional, and emergent trait definitions
│   ├── entity.py           # The digital human class
│   ├── simulator.py        # Simulation engine
│   └── observer.py         # Observer module (generates reports)
│
├── simulation_runner.py    # Main launcher script
├── requirements.txt        # Python dependencies
├── reports/                # Daily simulation outputs
└── README.md               # Project overview
```

---

## 🔍 Where Are the Results?

Every time a simulation runs, it generates **daily report files** in `reports/`. These `.md` files contain:

- Trait activity
- Emotional states
- Cultural observations
- Offspring development

### Example:

```bash
reports/
├── DAY1_REPORT.md
├── DAY2_REPORT.md
└── DAY3_REPORT.md
```

You can read them directly in GitHub for easy interpretation.

---

## 🤔 Questions or Confused?

- Start with `DAY1_REPORT.md` in the `reports/` folder — it walks through the first full simulation day.
- Still unsure? Open an [issue on GitHub](https://github.com/your-username/LifeOS/issues) — we're here to help.

---

## 👥 Coming Soon

- A simplified GUI viewer (planned)
- Sample DNA configurations
- Discord or discussion thread

---

Thanks for being curious — you're part of a brand new form of digital life exploration. 🧬
