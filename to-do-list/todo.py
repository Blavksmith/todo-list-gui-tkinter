import tkinter as tk

root = tk.Tk()
root.title("To-do list app")
root.geometry("600x450")

label = tk.Label(root,text="To-Do List" ,font=("Calibri", 18))
label.pack(pady=10)

# list of task shown on window
task = tk.Listbox(root, width=50, height=20)
task.pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


# to add a task
def add_new_task():
    task_text = task_entry.get()
    if(task_text):
        task.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)

# to delete a task
def delete_task():
    try:
        particular_idx = task.curselection()[0];
        task.delete(particular_idx)
    except IndexError:
        pass


add_button = tk.Button(root, text="Add New Task", command=add_new_task)
add_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)


root.mainloop()

