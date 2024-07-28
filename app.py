import tkinter as tk
from tkinter import messagebox
import json
import os

HABITS_FILE = "habits.json"

def setup_window():
    root = tk.Tk()
    root.title("Habit Tracker")
    root.geometry("400x300")
    return root

def create_input_fields(root):
    tk.Label(root, text="Habit Name:").pack(pady=5)
    
    habit_entry = tk.Entry(root, width=30)
    habit_entry.pack(pady=5)
    
    return habit_entry

def create_buttons(root, habit_entry, habit_list):
    log_button = tk.Button(root, text="Log Habit", command=lambda: log_habit(habit_entry, habit_list))
    log_button.pack(pady=5)
    
    view_button = tk.Button(root, text="View Habits", command=lambda: view_habits(habit_list))
    view_button.pack(pady=5)

def create_habit_list(root):
    habit_list = tk.Listbox(root, width=50, height=10)
    habit_list.pack(pady=10)
    return habit_list

def log_habit(habit_entry, habit_list):
    habit = habit_entry.get().strip()
    if habit:
        habit_list.insert(tk.END, habit)
        habit_entry.delete(0, tk.END)
        save_habits(habit_list)
    else:
        messagebox.showwarning("Warning", "Habit name cannot be empty.")

def view_habits(habit_list):
    habit_list.delete(0, tk.END)
    habits = load_habits()
    for habit in habits:
        habit_list.insert(tk.END, habit)

def save_habits(habit_list):
    habits = habit_list.get(0, tk.END)
    with open(HABITS_FILE, "w") as file:
        json.dump(habits, file)

def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "r") as file:
            habits = json.load(file)
    else:
        habits = []
    return habits

def main():
    root = setup_window()
    
    habit_entry = create_input_fields(root)
    habit_list = create_habit_list(root)
    
    create_buttons(root, habit_entry, habit_list)
    
    view_habits(habit_list)
    
    root.mainloop()

if __name__ == "__main__":
    main()
