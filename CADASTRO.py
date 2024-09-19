import sqlite3
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import DataBase

# Conectando ou criando o banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criando a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Local TEXT NOT NULL,
        Valor INTEGER NOT NULL,
        Pago TEXT NOT NULL,
        Serie TEXT NOT NULL,
        Data TEXT NOT NULL       
    )
''')

conn.commit()

# Função para adicionar um usuário ao banco de dados
def Add_boleto():
    Valor = Valor_entry.get()
    Local = Local_entry.get()
    Pago = Pago_entry.get()
    Serie = Serie_entry.get()
    Dia = Dia_entry.get()

    if Local == "" or Local == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
    else:
        cursor.execute("INSERT INTO users (Valor, Local, Pago, Serie, Data) VALUES (?, ?, ?, ?, ?)", (Valor, Local, Pago, Serie, Dia))
        conn.commit()
        messagebox.showinfo("Sucesso", "Boleto adicionado com sucesso!")
        Valor_entry.delete(0, END)
        Local_entry.delete(0, END)
        Pago_entry.delete(0, END)
        Serie_entry.delete(0, END)
        Dia_entry.delete(0, END)
        display_users()

# função deletar boletos
def delete_Boleto():
    selected_item = listbox.get(ANCHOR)
    if selected_item:
        user_id = selected_item.split(' ')[1]
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        display_users()
        messagebox.showinfo("Sucesso", "Boleto deletado com sucesso!")
    else:
        messagebox.showerror("Erro", "Selecione um Boleto para deletar")

# função usuarios e booleanas
def display_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    listbox.delete(0, END)
    for row in rows:
        listbox.insert(END, f"ID: {row[0]} | Local: {row[1]} | N°-Doc: {row[2]} | Pago: {row[3]} | Valor: {row[4]}")

# Função para exibir os usuários
def update_user():
    selected_item = listbox.get(ANCHOR)
    if selected_item:
        Local = selected_item.split(' ')[1]
        Valor = Valor_entry.get()
        Pago = Pago_entry.get()
        Serie = Serie_entry.get
        if Valor == "" or Pago == "" or Local =="" :
            messagebox.showerror("Erro", "Preencha todos os campos.")
        else:
            cursor.execute("UPDATE users SET Pago=?, WHERE Valor=? WHERE Local=?, WHERE Serie=?", (Valor, Pago, Local, Serie))
            conn.commit()
            messagebox.showinfo("Sucesso", "Boleto atualizado.")
            display_users()
    else:
        messagebox.showerror("Erro", "Selecione um Boleto para atualizar.")

# Interface gráfica
root = Tk()
root.title("Gerenciador de Boletos")
root.geometry('750x400')
root.resizable(False, False)

# subindo as imagens 
pastaApp= os.path.dirname(__file__)
img = PhotoImage(file='./img/bandeira.png')
img2= PhotoImage(file='./img/Logo.png')
# Criando um label e colocando a imagem nele

img_label = Label(root, image=img )# Mantendo a referência da imagem
img_label.place(x=560, y=10)

img_label = Label(root, image=img2)
img_label.place(x=250, y=10)
# explicando o uso 
commit_label = Label(root, text='1°-Adicione em cada \n campo os dados e clique no \n botao Adicionar Boleto \n\n 2°-Para Deletar, Antes Clique \n no boleto criado, \n logo após \n no botao Deletar Boleto')
commit_label.place(x=520, y=120)

# Labels e entradas
Local_label = Label(root, text="Local")
Local_label.place(x=20, y=10)

Local_entry = Entry(root)
Local_entry.place(x=120, y=10)

Serie_label = Label(root, text="N° do Doc")
Serie_label.place(x=20, y=40)

Serie_entry = Entry(root)
Serie_entry.place(x=120, y=70)

Valor_label = Label(root, text='Valor')
Valor_label.place(x=20, y=70)

Valor_entry = Entry(root)
Valor_entry.place(x=120, y=40)

Pago_label = Label(root, text='Pago')
Pago_label.place(x=20, y=100)

Pago_entry = Entry(root)
Pago_entry.place(x=120, y=100)

Dia_label = Label(root, text='Data')
Dia_label.place(x=20, y=130)

Dia_entry = Entry(root)
Dia_entry.place(x=120, y=130)

# Botões
add_button = Button(root, text="Adicionar Boleto", command=Add_boleto, border=3, )
add_button.place(x=10, y=190)

# Cria o botão "Deletar"

delete_button = Button(root, text="Deletar Boleto", command=delete_Boleto, border=3)
delete_button.place(x=120, y=190)


# Botão para salvar o arquivo

# Botão Colar
#botao_colar = Button(root, text="Colar", command=colar_texto, border=3)
#botao_colar.place(x=370, y=190)

# Lista para exibir os usuários
listbox = Listbox(root, width=80,)
listbox.place(x=5, y=230)
for item in ("SELECT * FROM users"):
    listbox.insert(END, 0)
# Exibir os usuários no início
display_users()

# fechamento de pagina
root.mainloop()

# Fechar a conexão ao fechar o programa
conn.close()
