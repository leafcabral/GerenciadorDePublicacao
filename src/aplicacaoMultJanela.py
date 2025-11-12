"""
ASMbleia
	Ian Caliel Matos Cabral
	João Paulo Pipper da Silva
	Rafael Cabral Lopes
	Vitor Felberg Barcelos
Serra, Brasil
TODO TODO TODO TODO TODO TODO TODO TODO 

Autora original: Alessandra Aguiar Vilarinho 
"""

import tkinter as tk
from tkinter import ttk

class ChildWindow:
    def __init__(self, parent, title, content):
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.minsize(400, 300)
        self.window.resizable(False, False)
        
        # Frame principal
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=False)
        
        # Conteúdo da janela
        label = ttk.Label(main_frame, text=content, font=('Arial', 12))
        label.pack(pady=20)
        
        # Botão de fechar
        close_button = ttk.Button(
            main_frame, 
            text="Fechar", 
            command=self.window.destroy
        )
        close_button.pack(pady=10)

class InserirDados:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Inserir uma nova publicação")
        self.window.minsize(400, 300)
        self.window.resizable(False, False)

        main_frame: ttk.Frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=False)

        # LABEL E INPUT DO ID DO TÍTULO
        titulo_label: ttk.Label = ttk.Label(main_frame, text="ID do título:", font=('Arial', 12))
        titulo_label.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="w")

        self.titulo_input: tk.Text = tk.Text(main_frame, height=1, width=20)
        self.titulo_input.grid(row=0, column=1, pady=10, sticky="w")

        self.titulo_input.bind('<KeyPress>', self.VerificarCaractereID)
        self.titulo_input.bind('<KeyRelease>', self.VerificarCaractereID)

        # LABEL E INPUT DA DATA DO TÍTULO

        data_label: ttk.Label = ttk.Label(main_frame, text="Data do título:", font=('Arial', 12))
        data_label.grid(row=1, column=0, padx=(0, 10), pady=10, sticky="w")

        self.data_input: tk.Text = tk.Text(main_frame, height=1, width=20)
        self.data_input.grid(row=1, column=1, pady=10, sticky="w")

        self.data_input.bind('<KeyPress>', self.VerificarCaractereData)
        self.data_input.bind('<KeyRelease>', self.VerificarCaractereData)

        # BOTÕES:

        cancelar_button = ttk.Button(
            main_frame, 
            text="Cancelar", 
            command=self.window.destroy
        )
        cancelar_button.grid(row=2, column=0, pady=10)

        ok = ttk.Button(
            main_frame, 
            text="Ok", 
            command=lambda: self.Input(self.titulo_input)
        )
        ok.grid(row=2, column=1, pady=10)

    def VerificarCaractereID(self, event):
        tam: int = len(self.titulo_input.get("1.0", "end-1c"))
        LIMITE_CHAR: int = 8

        if tam >= LIMITE_CHAR and event.keysym not in {"BackSpace", "Delete"}:
            return "break"
        
        if not (event.char.isdigit() or event.keysym == "BackSpace"):
            return "break"

    def VerificarCaractereData(self, event):
        tam: int = len(self.titulo_input.get("1.0", "end-1c"))
        LIMITE_CHAR: int = 8

        if tam >= LIMITE_CHAR and event.keysym not in {"BackSpace", "Delete"}:
            return 'break'
        
        if event.char.isdigit() or event.keysym == "BackSpace":
            return
        
        return "break"

    def Input(self, textbox: tk.Text):
        INPUT: str = textbox.get("1.0", "end-1c")

        print(INPUT)

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Publicações")
        self.root.geometry("800x600")

        self.root.minsize(800, 600)
        
        # Configurar o menu principal
        self.setup_menu()
        
        # Conteúdo da janela principal
        self.setup_content()
    
    def setup_content(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="vtkaxx", 
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=10)
        
        # Descrição
        desc_label = ttk.Label(
            main_frame, 
            text="leafcabral",
            font=('Arial', 12, 'bold')
        )
        desc_label.pack(pady=20)
        
        # Rodapé
        footer_label = ttk.Label(
            main_frame, 
            text="calielian",
            font=('Arial', 10, 'bold')
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)
    
    def setup_menu(self):
        # Criar a barra de menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Empregado
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Banco de dados", menu=file_menu)
        file_menu.add_command(
            label="Inserir", 
            command=lambda: InserirDados(self.root)
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Alterar", 
            command=lambda: ChildWindow(self.root, "Alterar empregado", "Aqui entra sua janela com\n\n\nlógica para alterar um empregado")
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Excluir", 
            command=lambda: ChildWindow(self.root, "Excluir empregado", "Aqui entra sua janela com\n\n\nlógica para excluir um empregado")
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Consultar por critério", 
            command=lambda: ChildWindow(self.root, "Consultar por critério", "Aqui entra sua janela com\n\n\nlógica para consultar um empregado por um critério")
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Consultar todos", 
            command=lambda: ChildWindow(self.root, "Consultar todos", "Aqui entra sua janela com\n\n\nlógica para consultar todos empregados")
        )
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        
        # Menu Ajuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        help_menu.add_command(
            label="Socorro quero terminar este trabalho...", 
            command=lambda: ChildWindow(self.root, "Terminando as disciplinas de programação com a profa. Alessandra.", "Adeus Programação em Python")
        )
        help_menu.add_separator()
        help_menu.add_command(label="Sobre", command=self.show_about)
    
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("Sobre")
        about_window.geometry("300x200")
        
        ttk.Label(about_window, text="Gerenciador de Publicações", font=('Arial', 14)).pack(pady=10)
        ttk.Label(about_window, text="Versão 1.0").pack()
        ttk.Label(about_window, text="Desenvolvidos por ASMbleia\nAutora original: Alessandra Aguiar").pack(pady=10)
        
        ttk.Button(about_window, text="OK", command=about_window.destroy).pack(pady=20)

def main() -> None:
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()