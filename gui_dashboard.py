
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import subprocess
import os
import json

VAULT_DIR = "vaults"

def run_simulation():
    try:
        subprocess.run(["python", "simulation_runner.py"], check=True)
        messagebox.showinfo("Simulation", "Simulation completed successfully.")
        refresh_logs()
    except Exception as e:
        messagebox.showerror("Error", f"Simulation failed: {e}")

def run_observer():
    try:
        subprocess.run(["python", "observer_mode.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Observer failed: {e}")

def get_latest_log():
    if not os.path.exists(VAULT_DIR):
        return None
    folders = sorted(os.listdir(VAULT_DIR), reverse=True)
    for folder in folders:
        log_path = os.path.join(VAULT_DIR, folder, "harmony_log.json")
        if os.path.exists(log_path):
            return log_path
    return None

def refresh_logs():
    log_path = get_latest_log()
    if not log_path:
        log_display.delete(1.0, tk.END)
        log_display.insert(tk.END, "No logs found.")
        return

    with open(log_path, "r") as f:
        logs = json.load(f)
        display_text = ""
        for entry in logs[-10:]:  # Show last 10 events
            display_text += f"{entry['entity']} (Gen {entry['generation']}): {entry['response']}
"

    log_display.delete(1.0, tk.END)
    log_display.insert(tk.END, display_text)

# Setup GUI
root = tk.Tk()
root.title("LifeOS Dashboard")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="🧬 LifeOS Simulation Dashboard", font=("Helvetica", 16)).pack(pady=10)

btn_simulate = tk.Button(frame, text="▶️ Run Simulation", width=25, command=run_simulation)
btn_simulate.pack(pady=5)

btn_observe = tk.Button(frame, text="🔍 Launch Observer Mode", width=25, command=run_observer)
btn_observe.pack(pady=5)

tk.Label(frame, text="Recent Events:").pack(pady=10)

log_display = scrolledtext.ScrolledText(frame, width=70, height=10, font=("Courier", 10))
log_display.pack()

refresh_logs()

root.mainloop()
