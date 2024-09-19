import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import os


# Função para criar o banco de dados e a tabela
def criar_banco_de_dados():
    conn = sqlite3.connect('DataBase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  Local TEXT,
                  Serie INTEGER,   
                  Valor INTEGER, 
                  Pago INTEGER,
                  Data INTEGER,
                  Data2 INTEGER,
                  Data3 INTEGER,
                  Recebido INTEGER
                    )''')
    conn.commit()
    conn.close()


def buscar():
    print("ok")


# Função para adicionar um novo usuário ao banco de dados
def add_Boletos():
    Local = entrada_Local.get()
    Serie = entrada_Serie.get()
    Valor = entrada_Valor.get()
    Pago = entrada_Pago.get()
    Data = entrada_Data.get()
    Data2 = entrada_Data2.get()
    Data3 = entrada_Data3.get()
    Recebido = entrada_Recebido.get()
    if Local and Serie and Valor and Pago and Data and Data2 and Data3 and Recebido:
        conn = sqlite3.connect('DataBase.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (Local, Serie, Valor, Pago, Data, Data2, Data3, Recebido) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (Local, Serie, Valor, Pago, Data, Data2, Data3, Recebido))
        conn.commit()
        conn.close()
        entrada_Local.delete(0, tk.END)
        entrada_Serie.delete(0, tk.END)
        entrada_Valor.delete(0, tk.END)
        entrada_Pago.delete(0, tk.END)
        entrada_Data.delete(0, tk.END)
        entrada_Data2.delete(0, tk.END)
        entrada_Data3.delete(0, tk.END)
        entrada_Recebido.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Boleto adicionado com sucesso!")
        carregar_Boletos()
    else:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")


# Função para carregar os usuários do banco de dados no Treeview
def carregar_Boletos():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect('DataBase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()

    for users in users:
        tree.insert('', tk.END, values=users)


# Função para gerar o PDF a partir do Treeview
def adicionar_ao_treeview():
    Local = entrada_Local.get()
    Serie = entrada_Serie.get()
    Valor = entrada_Valor.get()
    Pago = entrada_Pago.get()
    Data = entrada_Data.get()
    Data2 = entrada_Data2.get()
    Data3 = entrada_Data3.get()
    Recebido = entrada_Recebido.get()
    if Local and Serie and Valor and Data and Data2 and Data3 and Recebido:
        novo_id = len(tree.get_children()) + 1
        tree.insert('', 'end', values=(novo_id, Local, Serie, Valor, Pago, Data, Data2, Data3, Recebido))
        entrada_Local.delete(0, tk.END)
        entrada_Serie.delete(0, tk.END)
        entrada_Valor.delete(0, tk.END)
        entrada_Pago.delete(0, tk.END)
        entrada_Data.delete(0, tk.END)
        entrada_Data2.delete(0, tk.END)
        entrada_Data3.delete(0, tk.END)
        entrada_Recebido.delete(0, tk.END)


def gerar_pdf():
    Local = entrada_Local.get()
    Serie = entrada_Serie.get()
    Valor = entrada_Valor.get()
    Pago = entrada_Pago.get()
    Data = entrada_Data.get()
    Data2 = entrada_Data2.get()
    Data3 = entrada_Data3.get()
    Recebido = entrada_Recebido.get()
    if not (Local and Serie and Valor and Pago and Data and Data2 and Data3 and Recebido):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    nome_arquivo = "Boleto.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    # Título
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(largura / 2.0, altura - 50, "Esquadrias Souza")

    # Dados
    c.setFont("Helvetica", 14)
    c.drawString(100, altura - 100, f"Local: {Local}")
    c.drawString(100, altura - 130, f"Serie: {Serie}")
    c.drawString(100, altura - 160, f"Valor: {Valor}")
    c.drawString(100, altura - 190, f"Pago: {Pago}")
    c.drawString(100, altura - 220, f"Data Venc.: {Data}")
    c.drawString(100, altura - 250, f"Data Venc-2: {Data2}")
    c.drawString(100, altura - 285, f"Data Venc-3: {Data3}")
    c.drawString(100, altura - 310, f"Recebido: {Recebido}")
    c.showPage()
    c.save()


# Configuração da janela principal do Tkinter
root = tk.Tk()
root.title("Gerenciador de Boletos")
root.geometry('700x440')
root.resizable(False, False)
root.config(bg='#089471')
Bg1 = '#089471'
Cor1 = '#FDFFFE'
Cor2 = '#44B356'
Cor3 = '#B4C9B7'
# Criar banco de dados e tabela ao iniciar
criar_banco_de_dados()

# Criando frame da logo

pastaApp = os.path.dirname(__file__)

frame = tk.Frame(root, width=680, bg=Cor3, )
frame.place(x=7, y=5, relheight=0.47, relwidth=0.98, )

image = Image.open("img/Logo.png")
photo = ImageTk.PhotoImage(image)
# Labels e Entradas para Nome, Idad
label = tk.Label(frame, image=photo, bg=Cor3, )
label.image = photo
label.place(x=360, y=15)

tk.Label(root, text="Local", bg=Cor3).place(x=15, y=15)
entrada_Local = tk.Entry(root, border=3)
entrada_Local.place(x=100, y=10)

tk.Label(root, text="N° do Doc", bg=Cor3).place(x=15, y=40)
entrada_Serie = tk.Entry(root, border=3)
entrada_Serie.place(x=100, y=40)

tk.Label(root, text="Valor", bg=Cor3).place(x=15, y=70)
entrada_Valor = tk.Entry(root, border=3)
entrada_Valor.place(x=100, y=70)

tk.Label(root, text='Pago', bg=Cor3).place(x=15, y=100)
entrada_Pago = tk.Entry(root, border=3)
entrada_Pago.place(x=100, y=100)

tk.Label(root, text='Data Venc.', bg=Cor3).place(x=205, y=150)
entrada_Data = tk.Entry(root, border=3)
entrada_Data.place(x=280, y=145)

tk.Label(root, text='Data Venc-2', bg=Cor3).place(x=205, y=175)
entrada_Data2 = tk.Entry(root, border=3, )
entrada_Data2.place(x=280, y=175)

tk.Label(root, text='Recebido', bg=Cor3).place(x=410, y=150)
entrada_Recebido = tk.Entry(root, border=3)
entrada_Recebido.place(x=510, y=145)

tk.Label(root, text='Data Venc-3', bg=Cor3).place(x=410, y=180)
entrada_Data3 = tk.Entry(root, border=3, )
entrada_Data3.place(x=510, y=175)

entrada_Pesquisa = tk.Entry(root, border=3, )
entrada_Pesquisa.place(x=100, y=130)

dados = (entrada_Pesquisa)
# Configuração do Treeview para exibir múltiplas colunas
tree = ttk.Treeview(root, columns=('ID', 'Local', 'Serie', 'Valor', 'Pago', 'Data', 'Data2', 'Data3', 'Recebido'),
                    show='headings', )
tree.heading('ID', text='ID')
tree.heading('Local', text='Local')
tree.heading('Serie', text='Serie')
tree.heading('Valor', text='Valor')
tree.heading('Pago', text='Pago')
tree.heading('Data', text='Data')
tree.heading('Data2', text='Data2')
tree.heading('Data3', text='Data3')
tree.heading('Recebido', text='Recebido')
# Definindo largura das colunas
tree.column('ID', width=10)
tree.column('Local', width=50)
tree.column('Serie', width=50)
tree.column('Valor', width=80)
tree.column('Pago', width=60)
tree.column('Data', width=60)
tree.column('Data2', width=60)
tree.column('Data3', width=50)
tree.column('Recebido', width=50)

# Exibe o Treeview na janela
tree.place(x=7, y=225, relheight=0.47, relwidth=0.98, )

# Botão para gerar o PDF com os dados do Treeview
botao_gerar_pdf = tk.Button(root, text="Gerar PDF", bg=Cor2, font='Arial  8 bold', command=gerar_pdf)
botao_gerar_pdf.place(x=130, y=170)

# Botão para adicionar o usuário
botao_adicionar = tk.Button(root, text="Adicionar Boleto", bg=Cor2, font='Arial  8 bold', command=add_Boletos)
botao_adicionar.place(x=10, y=170)

botao_adicionar = tk.Button(root, text="Pesquisar", bg=Cor2, font='Arial  8 bold', command=buscar)
botao_adicionar.place(x=10, y=130)

# Carrega os usuários existentes ao iniciar a aplicação
carregar_Boletos()

# Inicia o loop principal do Tkinter
root.mainloop()
