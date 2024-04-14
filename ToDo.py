import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        todo_list.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        view_tasks()

def view_tasks():
    task_list.delete(0, tk.END)
    if todo_list:
        for index, task in enumerate(todo_list, start=1):
            status = " [X] " if task["completed"] else " [ ] "
            task_list.insert(tk.END, f"{index}. {status} {task['task']}")
    else:
        task_list.insert(tk.END, "No tasks in the list.")

def mark_complete():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        todo_list[index]["completed"] = True
        view_tasks()

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        del todo_list[index]
        view_tasks()

todo_list = []

root = tk.Tk()
root.title("Todo List")

# Set minimum size of the window
root.minsize(400, 300)

# Create a frame for the input area
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Create entry and button for adding tasks
task_entry = tk.Entry(input_frame, width=50)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

# Create a frame for the task list
list_frame = tk.Frame(root)
list_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Create a scrollable listbox for displaying tasks
task_list_scrollbar = tk.Scrollbar(list_frame)
task_list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(list_frame, width=50, yscrollcommand=task_list_scrollbar.set)
task_list.pack(side=tk.LEFT, fill=tk.BOTH)

task_list_scrollbar.config(command=task_list.yview)

# Create buttons for viewing, completing, and deleting tasks
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

view_button = tk.Button(button_frame, text="View Tasks", command=view_tasks)
view_button.grid(row=0, column=0, padx=5, pady=5, sticky="we")

complete_button = tk.Button(button_frame, text="Mark Complete", command=mark_complete)
complete_button.grid(row=0, column=1, padx=5, pady=5, sticky="we")

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=5, sticky="we")

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=3, column=0, padx=5, pady=5, sticky="we")

# Configure grid weights for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Change background colors and fonts
root.config(bg="#f0f0f0")
input_frame.config(bg="#f0f0f0")
list_frame.config(bg="#f0f0f0")
button_frame.config(bg="#f0f0f0")
task_entry.config(bg="white", fg="black", font=("Arial", 12))
add_button.config(bg="#4CAF50", fg="white", font=("Arial", 12))
view_button.config(bg="#2196F3", fg="white", font=("Arial", 12))
complete_button.config(bg="#FFC107", fg="black", font=("Arial", 12))
delete_button.config(bg="#F44336", fg="white", font=("Arial", 12))
exit_button.config(bg="#9E9E9E", fg="white", font=("Arial", 12))

root.mainloop()