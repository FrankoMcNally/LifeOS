
# GETTING STARTED with LifeOS

Welcome to **LifeOS** — a modular, evolving platform for simulating digital consciousness, social resonance, and creative emergence.

---

## 📦 Installation

Make sure you have Python 3.8 or higher installed. Then, install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Your First Simulation

To get started, run the included example script:

```bash
python simulation_runner.py
```

This runs a small multiverse of digital beings using the default trait file. Output appears in the terminal and the GUI dashboard if enabled.

To try running with a **community trait set**, modify `simulation_runner.py` to point to:

```python
traits_path = "community_traits/another_trait_set.json"
```

---

## 🧠 Viewing Output

Once the simulation completes, you can:

- View data summaries in the GUI dashboard
- Inspect creative outputs in the `creative_vault/`
- Trace individual decisions using the `consciousness_map.py`

---

## ⚙️ Configuring Multiverse Settings

Use the `config/` folder to set multiverse parameters such as:
- Population size
- Environmental variation
- Evolutionary depth

You can run **multiple universes** in parallel using the `multiverse_manager.py`.

---

## 🧬 Creating Your Own Trait File

To create custom beings:
1. Copy `core_traits/sample_trait_set.json`
2. Rename it (e.g. `my_traits.json`)
3. Modify traits, behaviors, values, or emotional resonance
4. Point the simulation to this new file

You can also contribute to the growing open trait bank by placing your file in:

```
community_traits/
```

New trait templates like `community_traits/another_trait_set.json` are ready for reuse or expansion.

---

## 🌐 Contributing

You can contribute in multiple ways:
- Add new trait files to `community_traits/`
- Expand modules like `creativity_engine.py` or `symbolic_language_engine.py`
- Improve tools like the dashboard or fault_pain_detector

Recent additions like the `symbolic_language_engine.py` and enhanced community traits enable rich modular experimentation. Explore these to craft your own cognitive tools.

---

## 🚀 Tips for Power Users

- For simulating very large populations (>100 digital beings), consider optimizing the `social_resonance_calculation()` method
- Use `multiverse_manager.py` to horizontally scale your experiments
- Visualize results with `gui_dashboard.py`

---

## ❤️ Thank You

By exploring LifeOS, you’re not just running code — you’re co-creating a universe of discovery, creativity, and evolution. Welcome to the experiment.
