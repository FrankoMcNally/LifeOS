# Getting Started with LifeOS (Beginner Friendly)

Welcome to LifeOS! This guide assumes **no prior coding experience**.

---

## ✅ Step 1: Install Python

1. Go to [https://www.python.org/downloads](https://www.python.org/downloads)
2. Download **Python 3.10 or newer**
3. During install, **check the box that says "Add Python to PATH"**
4. Finish the install

---

## ✅ Step 2: Launch LifeOS

1. Unzip the LifeOS.zip file to a folder like `C:\LifeOS\`
2. Double-click the file: `run_lifeos_simulation.bat`

---

## ✅ What to Expect

- A console window or GUI will launch
- Simulation will run with digital agents
- Data will be logged in `logs/simulation_log.txt`

---

## 🛠 If Things Go Wrong

### ⚠️ Python not found
Open `Command Prompt` and type:
```
python --version
```
If it fails, reinstall Python and **make sure to tick "Add to PATH"**

---

### ⚠️ Simulation doesn't launch
1. Right-click the batch file → “Run as Administrator”
2. Or open terminal manually:
```
cd C:\LifeOS\
python core/simulation_runner.py
```

---

## 📌 What Each File Does

- `simulation_runner.py`: main control center
- `observer_mode.py`: tracks digital behavior
- `free_will.py`: adds random actions
- `harmony_engine.py`: maintains balance
- `community_traits.json`: starter DNA data
- `run_lifeos_simulation.bat`: one-click launcher (Windows only)

---

## 🔁 Restarting or Resetting

You can run the simulation multiple times with different traits by editing:
```
traits/community_traits.json
```

---

Enjoy exploring LifeOS!