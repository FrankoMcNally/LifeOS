
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import json

VAULT_ROOT = "vaults"

def find_latest_creative_log():
    folders = sorted(os.listdir(VAULT_ROOT), reverse=True)
    for folder in folders:
        universe_path = os.path.join(VAULT_ROOT, folder)
        if not os.path.isdir(universe_path):
            continue
        for subfolder in os.listdir(universe_path):
            log_path = os.path.join(universe_path, subfolder, "creative_events.json")
            if os.path.exists(log_path):
                return log_path
    return None

def load_creative_events(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def update_tree(data):
    for item in tree.get_children():
        tree.delete(item)
    for event in data:
        tree.insert("", "end", values=(
            event.get("entity", ""),
            event.get("domain", ""),
            event.get("title", ""),
            event.get("harmony_score", ""),
            event.get("generation", "")
        ))

def open_log():
    path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if path:
        data = load_creative_events(path)
        update_tree(data)

def load_latest():
    path = find_latest_creative_log()
    if not path:
        messagebox.showwarning("Not Found", "No creative_events.json found.")
        return
    data = load_creative_events(path)
    update_tree(data)

# GUI Setup
root = tk.Tk()
root.title("🧠 Creative Vault Viewer")
root.geometry("900x400")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_load_latest = tk.Button(frame, text="📥 Load Latest Creative Events", command=load_latest)
btn_load_latest.pack(side="left", padx=10)

btn_open = tk.Button(frame, text="📂 Open JSON File", command=open_log)
btn_open.pack(side="left", padx=10)

columns = ("Entity", "Domain", "Title", "Harmony", "Generation")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(padx=10, pady=10, expand=True, fill="both")

root.mainloop()
