from tkinter import *
from tkinter import filedialog as f
import platform
import sys
import os
# package imports
import src.menu.about as about

TITLE = "Bloc de notas | Python"

# Configuracion de la raiz de nuestro editor
root = Tk()
root.title(TITLE)
if platform.system() == "Windows":
    root.iconbitmap("img/icon.ico")
else:
    root.iconphoto(True, PhotoImage(os.path.join(sys.path[0], "img/icon.xbm")))

url_file = ""
# Funciones

def new_file():
    global url_file
    # Borra desde el primer caracter hasta el ultimo
    text.delete(1.0, "end")
    url_file = ""
    root.title(url_file + TITLE) 

def open_file():
    global url_file
    if url_file != "":
        with open(url_file, 'r') as file:
            file = open(url_file, 'r')
            content = file.read()
            text.delete(1.0, "end")
            text.insert('insert', content)
        root.title(url_file + TITLE)

def save_file():
    global url_file
    if url_file != "":
        content = text.get(1.0, "end-1c")
        with open(url_file, "w+") as file:
            file.write(content)
            root.title("Archivo guardado en " + url_file + TITLE)
    else:
        file = f.asksaveasfile(title="Save file", mode="w", defaultextension=".txt")
        if file is not None:
            url_file = file.name
            content = text.get(1.0, "end-1c")
            with open(url_file, "w+") as file:
                file.write(content)
                root.title("Archivo guardado en " + url_file + TITLE)
                url_file = ""
                root.title("Guardado cancelado " + url_file + TITLE) 



# Menú
bar = Menu(root)
file_menu = Menu(bar, tearoff=0)
file_menu.add_command(label="Nuevo archivo", command=new_file)
file_menu.add_command(label="Abrir archivo", command=open_file)
file_menu.add_command(label="Guardar archivo", command=save_file)
file_menu.add_command(label="Salir", command=root.quit)
bar.add_cascade(menu=file_menu, label="Archivo")
more_menu = Menu(bar, tearoff=0)
more_menu.add_command(label="Licencia", command=about.display_license)
more_menu.add_command(label="Créditos", command=about.display_credits)
more_menu.add_command(label="Contacto", command=about.display_contact)
bar.add_cascade(menu=more_menu, label="Sobre")

# caja de text, donde se escribe ._.XD
text = Text(root)
text.pack(side=LEFT)
text.config(bd=0, padx=6, pady=4, font=("Arial", 14), wrap=NONE)
# Scrollbar para text
scroll = Scrollbar(root)
scroll.config(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)


root.config(menu=bar)
root.mainloop()
