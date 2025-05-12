import tkinter as tk

root = tk.Tk()
root.title("To-do list app")
root.geometry("600x450")

label = tk.Label(root,text="To-Do List" ,font={"Calibri", 18})
label.pack(pady=10)

# list of task shown on window
task = tk.Listbox(root, width=50, height=50)
task.pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


root.mainloop()

