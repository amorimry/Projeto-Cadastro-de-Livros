import customtkinter as ctk
from tkinter import ttk, messagebox
import database

# FUNÇÕES ---




# CONFIDURAÇÕES ---
ctk.set_appearance_mode("dark")

# CONFIG JANELA ---
janela = ctk.CTk()
janela.title("Cadastro de Livros")
janela.geometry(f"900x580") # largura x altura
janela.maxsize(1000, 780)
janela.minsize(600, 380)
janela.attributes("-topmost", True) # sobrepor / true ou false
janela.attributes("-alpha", 0.9) # transparência / entre 1 e 0

# CÓDIGO ---
titulo = ctk.CTkLabel(janela, text="Cadastre seu livro abaixo!", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

frame_tela = ctk.CTkFrame(janela,fg_color="#B5B5B5", border_width=5, corner_radius=10)
frame_tela.pack(side="top", fill="both", padx=35, ipadx=15, ipady=15)




janela.mainloop()