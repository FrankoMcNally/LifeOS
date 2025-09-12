
# 🛠️ LifeOS Troubleshooting Guide

This guide addresses common issues users might face when trying to run LifeOS for the first time.

---

## ⚙️ 1. Simulation Doesn’t Start

### 🔍 Symptom:
- `run.py` exits without running
- No traits or beings appear in logs

### ✅ Fix:
- Ensure your `traits/` folder (including `core_traits/`) is populated.
- Check if `community_loader.py` is properly referencing the trait directories.
- Confirm that Python 3.10+ is installed.

---

## 📦 2. Missing Dependencies

### 🔍 Symptom:
- Errors like `ModuleNotFoundError: No module named 'pandas'`

### ✅ Fix:
- Run: `pip install -r requirements.txt`

---

## 🗂️ 3. GUI Doesn't Open or Crashes

### 🔍 Symptom:
- GUI fails to launch
- Logs mention `tkinter` issues

### ✅ Fix:
- Ensure you are running the simulation in a desktop environment (not remote server).
- Tkinter should be preinstalled with most Python 3 installations, but you can install manually:
  - On Ubuntu: `sudo apt-get install python3-tk`
  - On Windows/macOS: Tkinter is included.

---

## 📁 4. Observer or Dashboard Doesn’t Show Output

### 🔍 Symptom:
- Simulation runs but no visible data or insights are logged

### ✅ Fix:
- Ensure `observer_mode.py` is correctly imported and enabled in your runner script.
- If using GUI, ensure the data is routed to the GUI dashboard or observer logger.

---

## 🧬 5. Traits Not Activating

### 🔍 Symptom:
- Digital beings show no behaviors or personality differentiation

### ✅ Fix:
- Check the `core_traits/`, `optional_traits/`, and `emergent_traits/` directories.
- Make sure traits are in `.json` or `.py` format as required.
- Validate trait structure matches expected schema.

---

## 🌍 6. Custom Community Doesn’t Load

### 🔍 Symptom:
- Simulation falls back to defaults
- Your custom beings or couples don't appear

### ✅ Fix:
- Double-check formatting in your custom `community_traits/` or `community_structure.json`
- Use the template in `examples/` to validate your structure.

---

## 💬 Still Stuck?

Open an [Issue on GitHub](https://github.com/your-repo-url/issues) or reach out via the README contact instructions.

---

Happy simulating! 🌱
