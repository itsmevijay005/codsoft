import tkinter as tk
from tkinter import messagebox
import os

FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return f.read().splitlines()
    return []

# Save tasks to file
def save_tasks():
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        save_tasks()
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = tasks.pop(selected)
        save_tasks()
        update_listbox()
        messagebox.showinfo("Deleted", f"Deleted: {task}")
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            tasks[selected] = new_task
            save_tasks()
            update_listbox()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter new task!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("450x500")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Entry Box
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

add_btn = tk.Button(frame, text="Add", width=10, bg="#4CAF50", fg="white", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(frame, text="Update", width=10, bg="#2196F3", fg="white", command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(frame, text="Delete", width=10, bg="#f44336", fg="white", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=15)

# Load existing tasks
update_listbox()

# Run App
root.mainloop()