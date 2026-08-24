import customtkinter as ctk
from tkinter import ttk, messagebox
import database

# FUNÇÕES ---
def atualizar_tabela():
    tabela.delete(*tabela.get_children())

    livros = database.carregar_livros()

    for livro in livros:
        tabela.insert("", "end", values=(livro["título"], livro["autor"], livro["ano"]))

def adicionar():
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    ano = ano_entry.get()

    if titulo == "" or autor == "" or ano == "":
        return messagebox.showwarning("Atenção", "Você deixou algo vazio, preencha todos os campos.")

    database.adicionar_livro(titulo, autor, ano)

    titulo_entry.delete(0, "end")
    autor_entry.delete(0, "end")
    ano_entry.delete(0, "end")

    atualizar_tabela()

def editar():
    selecionado = tabela.selection()

    if not selecionado:
        return messagebox.showwarning("Atenção!", "Selecione um livro na lista para editar.")

    indice = tabela.index(selecionado[0])

    livros = database.carregar_livros()
    livro_selecionado = livros[indice]

    janela_popup_edicao = popup = ctk.CTkToplevel(janela)
    popup.title("Editar livro")
    popup.geometry("350x300")
    popup.grab_set()

    def ao_fechar_popup(): # Libera o travamento da janela principal se fechar no "X"
        popup.grab_release()
        popup.destroy()
        
    popup.protocol("WM_DELETE_WINDOW", ao_fechar_popup)

    ctk.CTkLabel(popup, text="Título:").pack(anchor="w", padx=20, pady=(20, 0))
    titulo_entry_popup = ctk.CTkEntry(popup)
    titulo_entry_popup.pack(fill="x", padx=20)
    titulo_entry_popup.insert(0, livro_selecionado["título"])
 
    ctk.CTkLabel(popup, text="Autor:").pack(anchor="w", padx=20, pady=(10, 0))
    autor_entry_popup = ctk.CTkEntry(popup)
    autor_entry_popup.pack(fill="x", padx=20)
    autor_entry_popup.insert(0, livro_selecionado["autor"])
 
    ctk.CTkLabel(popup, text="Ano de publicação:").pack(anchor="w", padx=20, pady=(10, 0))
    ano_entry_popup = ctk.CTkEntry(popup)
    ano_entry_popup.pack(fill="x", padx=20)
    ano_entry_popup.insert(0, livro_selecionado["ano"])

    # Função do botão de salvar
    def salvar_edicao():
        novo_titulo = titulo_entry_popup.get()
        novo_autor = autor_entry_popup.get()
        novo_ano = ano_entry_popup.get()

        database.atualizar_livro(indice, novo_titulo, novo_autor, novo_ano)

        atualizar_tabela()
        popup.destroy()

    botao_salvar = ctk.CTkButton(popup, text="Salvar", command=salvar_edicao)
    botao_salvar.pack(pady=20)

def excluir():
    pass






# CONFIDURAÇÕES ---
ctk.set_appearance_mode("dark")

# CONFIG JANELA ---
janela = ctk.CTk()
janela.title("Cadastro de Livros")
janela.geometry(f"850x700") # largura x altura
janela.maxsize(1000, 780)
janela.minsize(600, 380)
# janela.attributes("-topmost", True) # sobrepor / true ou false
# janela.attributes("-alpha", 0.9) # transparência / entre 1 e 0

# CÓDIGO ---
cabecalho = ctk.CTkLabel(janela, text="Cadastre seu livro abaixo!", font=("Arial", 20, "bold"))
cabecalho.pack(pady=20)

frame_tela = ctk.CTkFrame(janela,fg_color="#B5B5B5", border_width=5, corner_radius=10)
frame_tela.pack(side="top", fill="both", padx=35, ipadx=15, ipady=15)


titulo_label = ctk.CTkLabel(frame_tela, text="Título", font=("Arial", 15), text_color="black", fg_color="transparent")
titulo_label.grid(row=0, column=0, sticky="w", padx=15, pady=(15, 2))

titulo_entry = ctk.CTkEntry(frame_tela, placeholder_text="Digite aqui o TÍTULO do livro...", height=35, width=400)
titulo_entry.grid(row=1, column=0, padx=15)


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

atualizar_tabela() # a função fica aq pq quando abre o arquivo desktop as informações da tabela não aparecem


# BOTÕES ---
frame_botao = ctk.CTkFrame(janela, fg_color="transparent")
frame_botao.pack(padx=35, pady=15)


botao_adicionar = ctk.CTkButton(frame_botao, text="Adicionar", command=adicionar)
botao_adicionar.pack(padx=5, side="left")

botao_editar = ctk.CTkButton(frame_botao, text="Editar", command=editar)
botao_editar.pack(padx=5, side="left")

botao_excluir = ctk.CTkButton(frame_botao, text="Excluir", fg_color="#d9534f", hover_color="#c9302c")
botao_excluir.pack(padx=5, side="left")


# FIM ---
janela.mainloop()