import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Explorador de Arquivos")
root.geometry("800x600")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    with open(filename, 'r') as file:
        content = file.read()
        inputtxt.delete(1.0, tk.END)
        inputtxt.insert(tk.END, content)



root.configure(bg="lightblue")

# layout: duas colunas (0 = área principal, 1 = controles)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

label_file_explorer = tk.Label(root, text="No file selected", bg="lightblue")
label_file_explorer.grid(row=0, column=0, padx=10, pady=5, sticky="w")

button_arq = tk.Button(
    root,
    text="Importar Arquivo",
    bg="lightgray",
    activebackground="gray",
    cursor="hand2",
    command=browseFiles
)

# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


slider_label = tk.Label(
    root, 
    text='Volume:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)

current_value_label = tk.Label(
    root,
    text='Current Value:'
)

current_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

value_label = tk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)

print(get_current_value())

inputtxt = tk.Text(root, height = 10, width = 25, bg = "light yellow")
inputtxt.grid(row=1, column=0, rowspan=3, sticky='nsew', padx=10, pady=10)

# colocar controles na coluna da direita
button_arq.grid(row=3, column=1, padx=20, pady=10, sticky='e')

root.mainloop()
