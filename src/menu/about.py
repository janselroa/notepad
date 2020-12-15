# En este archivo se almacenan todas las funciones de la barra de menu 
# en la cascada "Sobre"
from tkinter import messagebox

def display_license():
    with open("LICENSE", "r") as file:
        m = file.read()
    messagebox.showinfo("License", m)

def display_credits():
    LINK = "https://github.com/janselroa/bloc-de-notas-python"
    m = f"""
Esta aplicación ha sido desarrollada por Jansel Roa en su repositorio de GitHub:

{LINK}

Puedes leer la lista completa de contribuidores de esta aplicación en el archivo contributors.md
    """
    messagebox.showinfo("Créditos", m)

def display_contact():
    m = """
Si necesitas contactar en relacción con este programa, puedes hacerlo en nuestro repositorio de GitHub.

Tambien puedes contactarme a mi correo janselroa2424@gmail.com


"""
    messagebox.showinfo("Contacto", m)
