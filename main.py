import customtkinter as ctk
from tkinter import ttk, messagebox
import database

# FUNÇÕES ---




# CONFIDURAÇÕES ---
ctk.set_appearance_mode("dark")

# CONFIG JANELA ---
janela = ctk.CTk()
janela.title("Cadastro de Livros")
janela.geometry(f"700x600") # largura x altura
janela.maxsize(1000, 780)
janela.minsize(600, 380)
janela.attributes("-topmost", True) # sobrepor / true ou false
janela.attributes("-alpha", 0.9) # transparência / entre 1 e 0

# CÓDIGO ---
titulo = ctk.CTkLabel(janela, text="Cadastre seu livro abaixo!", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

frame_tela = ctk.CTkFrame(janela,fg_color="#B5B5B5", border_width=5, corner_radius=10)
frame_tela.pack(side="top", fill="both", padx=35, ipadx=15, ipady=15)


nome_label = ctk.CTkLabel(frame_tela, text="Título", font=("Arial", 15), text_color="black", fg_color="transparent")
nome_label.grid(row=0, column=0, sticky="w", padx=15, pady=(15, 2))

nome_entry = ctk.CTkEntry(frame_tela, placeholder_text="Digite aqui o TÍTULO do livro...", height=35, width=400)
nome_entry.grid(row=1, column=0, padx=15)


autor_label = ctk.CTkLabel(frame_tela, text="Autor", font=("Arial", 15), text_color="black", fg_color="transparent")
autor_label.grid(row=2, column=0, sticky="w", padx=15, pady=(15, 2))

autor_entry = ctk.CTkEntry(frame_tela, placeholder_text="Digite aqui o AUTOR do livro...", height=35, width=400)
autor_entry.grid(row=3, column=0, padx=15)


ano_label = ctk.CTkLabel(frame_tela, text="Ano de publicação", font=("Arial", 15), text_color="black", fg_color="transparent")
ano_label.grid(row=4, column=0, sticky="w", padx=15, pady=(15, 2))

ano_entry = ctk.CTkEntry(frame_tela, placeholder_text="Digite aqui o ANO do livro...", height=35, width=400)
ano_entry.grid(row=5, column=0, padx=15)


# TABELA ---
colunas = ("Título", "Ano", "Autor")
tabela = ttk.Treeview(janela, columns=colunas, show="headings") # show mostra só as colunas que eu tenho

tabela.heading("Título", text="Título") # heading é de cabeçalho
tabela.heading("Ano", text="Ano")
tabela.heading("Autor", text="Autor")

tabela.pack(fill="both", padx=80, pady=20)


# BOTÕES ---
frame_botao = ctk.CTkFrame(janela, fg_color="transparent")
frame_botao.pack(padx=35, pady=15)


botao_adicionar = ctk.CTkButton(frame_botao, text="Adicionar")
botao_adicionar.pack(padx=5, side="left")


botao_editar = ctk.CTkButton(frame_botao, text="Editar")
botao_editar.pack(padx=5, side="left")

botao_excluir = ctk.CTkButton(frame_botao, text="Excluir", fg_color="#d9534f", hover_color="#c9302c")
botao_excluir.pack(padx=5, side="left")


# FIM ---
janela.mainloop()