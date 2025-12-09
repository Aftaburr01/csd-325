"""
todo_app.py

Tkinter To-Do List GUI application.
Based on Listing 2.2 from the Tkinter-By-Example tutorial, 
with modifications for CSD-325 Assignment:

MODIFICATIONS:
1. Title: Changed window title to '[LastName]-ToDo'. (Replace Sampson-ToDo)
2. Menu Colors: Used LightCyan and Navy Blue for menu items.
3. Deletion: Changed binding from left-click ('<Button-1>') to right-click ('<Button-3>').
4. Instructions: Added instructions to the label on how to delete a task.
5. Exit Menu: Added File -> Exit option using root.destroy.
"""
import tkinter as tk
import sys

# Define color palette for complementary menu items
MENU_BG_COLOR = "#E0FFFF" # Light Cyan (Complementary to Navy)
MENU_FG_COLOR = "#000080" # Navy Blue

class ToDoApp:
    def __init__(self, master):
        self.master = master
        
        # Modification 1: Change the Title
        self.master.title("Rahman-ToDo") 

        # --- Menu Setup (Modification 5 & 2) ---
        menubar = tk.Menu(master)
        
        # File Menu
        # tearoff=0 prevents a dashed line from appearing at the top
        file_menu = tk.Menu(menubar, tearoff=0, bg=MENU_BG_COLOR, fg=MENU_FG_COLOR)
        
        # Modification 5: Add File -> Exit command
        # command=master.destroy is the standard way to close a Tkinter window
        file_menu.add_command(label="Exit", command=master.destroy, 
                              activebackground=MENU_FG_COLOR, activeforeground=MENU_BG_COLOR)
        
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Help Menu (Optional, styled for color change requirement)
        help_menu = tk.Menu(menubar, tearoff=0, bg=MENU_BG_COLOR, fg=MENU_FG_COLOR)
        help_menu.add_command(label="About", command=self.show_about, 
                              activebackground=MENU_FG_COLOR, activeforeground=MENU_BG_COLOR)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        master.config(menu=menubar)
        
        # --- Listbox and Scrollbar ---
        self.task_list = tk.Listbox(master, height=15, width=50, 
                                     font=('Arial', 12), selectmode=tk.SINGLE)
        self.task_list.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(master, command=self.task_list.yview)
        self.scrollbar.grid(row=0, column=2, sticky='ns', padx=(0, 10), pady=10)
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        
        # Modification 3: Change binding from left-click ('<Button-1>') to right-click ('<Button-3>')
        self.task_list.bind('<Button-3>', self.delete_task) 

        # --- Input Field ---
        self.task_entry = tk.Entry(master, width=50, font=('Arial', 12))
        self.task_entry.grid(row=1, column=0, padx=10, pady=5)

        # --- Buttons ---
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, 
                                    bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'))
        self.add_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # --- Instructions Label (Modification 4) ---
        instruction_text = "Enter task above. Use the ADD TASK button.\nRIGHT-CLICK a task to delete it."
        self.instructions_label = tk.Label(master, text=instruction_text, 
                                           fg="#8B0000", font=('Arial', 9)) # Dark Red for visibility
        self.instructions_label.grid(row=2, column=0, columnspan=2, pady=(0, 10))

    def add_task(self):
        """Adds the text from the entry field to the Listbox."""
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            # Simple warning for empty task
            tk.messagebox.showwarning("Warning", "Task field cannot be empty.")

    def delete_task(self, event):
        """Deletes the selected task when the right mouse button is clicked."""
        try:
            # Get the index of the task under the cursor when the event occurred
            selected_index = self.task_list.nearest(event.y)
            # Delete the task at that index
            self.task_list.delete(selected_index)
        except:
            # If no task is selected or list is empty, pass silently
            pass
            
    def show_about(self):
        """Placeholder for a Help/About dialog."""
        tk.messagebox.showinfo("About", "ToDo List App\nDeveloped using Python and Tkinter.")

if __name__ == '__main__':
    # Initialize the main Tkinter window
    root = tk.Tk()
    # Instantiate the application
    app = ToDoApp(root)
    # Start the Tkinter event loop
    root.mainloop()
