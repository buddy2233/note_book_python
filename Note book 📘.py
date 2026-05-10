import tkinter as tk

def save_note():
    note = text_area.get("1.0", tk.END)
    with open("note.txt", "w") as f:
        f.write(note)

root = tk.Tk()
root.title("Simple Notebook")

text_area = tk.Text(root)
text_area.pack(fill="both", expand=True)

save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack()

root.mainloop()
