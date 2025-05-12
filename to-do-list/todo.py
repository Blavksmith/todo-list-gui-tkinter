import tkinter as tk

root = tk.Tk()
root.title("To-do list app")
root.geometry("600x450")
root.config(bg="black")

label = tk.Label(root,text="To-Do List" ,font=("Calibri", 25, "bold"), fg="white", bg="black")
label.pack(pady=10)

task_entry = tk.Entry(root, width=40, relief="solid")
task_entry.pack(pady=10)

task_frame = tk.Frame(root)
task_frame.pack(pady=10)
# storing in checkboxes
checkboxes = []

# to add a task
def add_new_task():
    task_text = task_entry.get()
    if(task_text):
        var = tk.IntVar() # save a status (0 and 1) for each checckbox
        checkbox = tk.Checkbutton(task_frame, text=task_text, variable=var, onvalue=1, offvalue=0)
        checkbox.pack(anchor="w")
        checkboxes.append((checkbox, var))
        task_entry.delete(0, tk.END)


# delete a task
def delete_completed_task():
    for checkbox, var in checkboxes[:]:
        if var.get() == 1: # if checkbox selected
            checkbox.pack_forget() # hide a checkbox
            checkboxes.remove((checkbox, var)) # remove every toggled checkbox from the list.


add_button = tk.Button(root, text="Add New Task", command=add_new_task, bg="#4CAF50", relief="raised", font=("Calibri", 12), fg="white")
add_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_completed_task, bg="#F44336", font=("Calibri", 12), bd=2, fg="white")
delete_button.pack(pady=10) 


root.mainloop()

