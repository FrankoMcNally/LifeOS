import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json
import os

class GUIDashboard:
    def __init__(self, master):
        self.master = master
        master.title("LifeOS Trait Loader")

        self.label = tk.Label(master, text="Select a Trait File to Load:")
        self.label.pack(pady=10)

        self.trait_file_path = tk.StringVar()
        self.dropdown = ttk.Combobox(master, textvariable=self.trait_file_path)
        self.dropdown.pack(pady=5)

        self.load_button = tk.Button(master, text="Load Traits", command=self.load_traits)
        self.load_button.pack(pady=10)

        self.text_output = tk.Text(master, height=15, width=60)
        self.text_output.pack(pady=5)

        self.refresh_trait_file_list()

    def refresh_trait_file_list(self):
        trait_files = []
        for folder in ['traits', 'community_traits']:
            if os.path.isdir(folder):
                for file in os.listdir(folder):
                    if file.endswith(".json"):
                        trait_files.append(os.path.join(folder, file))
        self.dropdown['values'] = trait_files
        if trait_files:
            self.dropdown.current(0)

    def load_traits(self):
        path = self.trait_file_path.get()
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, json.dumps(data, indent=2))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load trait file:\n{str(e)}")
        else:
            messagebox.showwarning("Missing File", "Selected trait file does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUIDashboard(root)
    root.mainloop()