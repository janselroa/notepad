from tkinter import *
from tkinter import filedialog as f
from io import open

# Configuracion de la raiz de nuestro editor
root = Tk()
root.title("Bloc de notas")
root.iconbitmap("bloc.ico")

url_file = ""


# Funciones

def new_file():
    global url_file
    # Borra desde el primer caracter hasta el ultimo
    text.delete(1.0, "end")
    url_file = ""
    root.title(url_file + title)


def open_file():
    global url_file
    url_file = f.askopenfilename(initialdir='.', filetype=((
                                                               "Archivos de texto", "*.txt"
                                                           ),), title="Open File")
    if url_file != "":
        file = open(url_file, 'r')
        content = file.read()
        text.delete(1.0, "end")
        text.insert('insert', content)
        file.close()
        root.title(url_file + title)


def save_file():
    global url_file
    if url_file != "":
        content = text.get(1.0, "end-1c")
        file = open(url_file, 'w+')
        file.write(content)
        root.title("Archivo guardado en " + url_file + title)
        file.close()
    else:
        file = f.asksaveasfile(title="Save file", mode="w", defaultextension=".txt")
        if file is not None:
            url_file = file.name
            content = text.get(1.0, "end-1c")
            file = open(url_file, 'w+')
            file.write(content)


            root.title("Archivo guardado en " + url_file + title)
            file.close()
        else:
            url_file = ""
            root.title("Guardado cancelado " + url_file + title)

# Menú
bar = Menu(root)
file_menu = Menu(bar, tearoff=0)
file_menu.add_command(label="Nuevo archivo", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Abrir archivo", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Guardar archivo", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

bar.add_cascade(menu=file_menu, label="Archivo")

# caja de text, donde se escribe ._.XD
text = Text(root)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("Arial", 14))

root.config(menu=bar)
root.mainloop()
