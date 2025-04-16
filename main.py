import json
import uuid
import os
from tkinter.simpledialog import askstring
import customtkinter as ctk
import tkinter as tk

DATA_FILE = 'data.json'

def load_tasks():
    try:
        with open(DATA_FILE, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
        save_tasks(tasks)
    for task in tasks:
        task.setdefault('due_date', "No due date")
    return tasks

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(task_desc, due_date=None):
    tasks = load_tasks()
    task = {
        "id": str(uuid.uuid4()),
        "description": task_desc,
        "completed": False,
        "due_date": due_date or "No due date"
    }
    tasks.append(task)
    save_tasks(tasks)

def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    save_tasks(tasks)

def refresh_task_list(task_frame):
    for widget in task_frame.winfo_children():
        widget.destroy()
    tasks = load_tasks()
    for task in tasks:
        create_task_widget(task_frame, task)

def create_task_widget(task_frame, task):
    frame = ctk.CTkFrame(task_frame)
    frame.pack(pady=4, fill="x", padx=10)

    check = ctk.CTkCheckBox(
        frame,
        text=task["description"],
        command=lambda tid=task["id"]: on_check(tid),
        checkbox_width=20,
        checkbox_height=20
    )
    check.select() if task["completed"] else check.deselect()
    check.pack(side="left", padx=5)

    edit_btn = ctk.CTkButton(
        frame,
        text="🔑 Edit",
        width=60,
        command=lambda tid=task["id"]: edit_task_dialog(tid),
        fg_color="orange",
        hover_color="gold",
        text_color="black"
    )
    edit_btn.pack(side="left", padx=5)

    del_btn = ctk.CTkButton(
        frame,
        text="🗑️ Delete",
        width=60,
        command=lambda tid=task["id"]: delete_task(tid),
        fg_color="red",
        hover_color="darkred"
    )
    del_btn.pack(side="right", padx=5)

    due_date = task.get('due_date', 'No due date')
    due_date_label = ctk.CTkLabel(frame, text=f"Due: {due_date}", font=("Arial", 8))
    due_date_label.pack(side="right", padx=5)

def on_check(task_id):
    toggle_task(task_id)
    refresh_task_list(task_frame)

def on_add():
    task_text = entry.get().strip()
    if task_text:
        add_task(task_text)
        entry.delete(0, 'end')
        refresh_task_list(task_frame)

def changetheme():
    current_theme = ctk.get_appearance_mode()
    ctk.set_appearance_mode("Light" if current_theme == "Dark" else "Dark")

def exit_app():
    app.quit()

def edit_task_dialog(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        new_desc = askstring("Edit Task", f"Edit the task '{task['description']}':", initialvalue=task['description'])
        if new_desc:
            task['description'] = new_desc
            save_tasks(tasks)
            refresh_task_list(task_frame)

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    refresh_task_list(task_frame)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Honeylist - To-Do App")
app.geometry("400x500")

menubar = tk.Menu(app)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Toggle Theme", command=changetheme)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
app.config(menu=menubar)

title = ctk.CTkLabel(app, text="To-Do List", font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="Enter a new task")
entry.pack(padx=20, pady=10, fill="x")

add_button = ctk.CTkButton(app, text="Add Task", command=on_add, fg_color="#28282B", border_color='#636363', border_width=1, hover_color='#353935')
add_button.pack(pady=5)

task_frame = ctk.CTkScrollableFrame(app, width=360, height=300)
task_frame.pack(pady=10)

refresh_task_list(task_frame)

app.mainloop()
