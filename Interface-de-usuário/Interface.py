import tkinter as tk
from tkinter import font, messagebox
import os

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("800x800")
        self.root.config(bg="#CAE4F1")
        
        self.user_text = ''
        self.archive_path = ''
        self.typing_active_dig = False
        self.typing_active_arq = False
        
        # Fontes
        self.base_font = font.Font(family="Arial", size=16)
        self.title_font = font.Font(family="Arial", size=20, weight="bold")
        
        # Frame principal
        self.main_frame = tk.Frame(root, bg="#CAE4F1")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame de entrada
        self.input_frame = tk.Frame(root, bg="#CAE4F1")
        
        # Frame de conteúdo
        self.content_frame = tk.Frame(root, bg="#CAE4F1")
        
        self.show_menu()
    
    def show_menu(self):
        """Exibe o menu principal com os dois botões"""
        self.clear_frames()
        
        # Título
        title = tk.Label(self.main_frame, text="Menu Principal", font=self.title_font, bg="#CAE4F1")
        title.pack(pady=50)
        
        # Botão Digitar
        digitar_btn = tk.Button(
            self.main_frame,
            text="Digitar Texto",
            font=self.base_font,
            width=20,
            height=3,
            bg="#87CEEB",
            cursor="hand2",
            command=self.activate_typing
        )
        digitar_btn.pack(pady=50)
        
        # Botão Arquivo
        arquivo_btn = tk.Button(
            self.main_frame,
            text="Carregar Arquivo",
            font=self.base_font,
            width=20,
            height=3,
            bg="#87CEEB",
            cursor="hand2",
            command=self.activate_archive
        )
        arquivo_btn.pack(pady=50)
    
    def activate_typing(self):
        """Ativa o modo de digitação de texto"""
        self.typing_active_dig = True
        self.user_text = ''
        self.show_typing_input()
    
    def activate_archive(self):
        """Ativa o modo de entrada de caminho de arquivo"""
        self.typing_active_arq = True
        self.archive_path = ''
        self.show_archive_input()
    
    def show_typing_input(self):
        """Exibe a interface de entrada de texto"""
        self.clear_frames()
        
        # Label de instrução
        label = tk.Label(
            self.main_frame,
            text="Digite seu texto (ESC para voltar):",
            font=self.base_font,
            bg="#CAE4F1"
        )
        label.pack(pady=20)
        
        # Campo de entrada
        self.entry_widget = tk.Entry(self.main_frame, font=self.base_font, width=50)
        self.entry_widget.pack(pady=10)
        self.entry_widget.focus()
        self.entry_widget.bind("<KeyRelease>", self.on_typing_key)
        self.entry_widget.bind("<Escape>", lambda e: self.back_to_menu())
        
        # Label para exibir o texto
        self.text_display = tk.Label(
            self.main_frame,
            text=self.user_text,
            font=self.base_font,
            bg="#CAE4F1",
            fg="black",
            wraplength=700,
            justify=tk.LEFT
        )
        self.text_display.pack(pady=20)
        
        # Botão Enviar
        submit_btn = tk.Button(
            self.main_frame,
            text="Enviar",
            font=self.base_font,
            bg="#90EE90",
            command=self.submit_typing
        )
        submit_btn.pack(pady=10)
        
        # Botão Voltar
        back_btn = tk.Button(
            self.main_frame,
            text="Voltar",
            font=self.base_font,
            bg="#FFB6C1",
            command=self.back_to_menu
        )
        back_btn.pack(pady=10)
    
    def show_archive_input(self):
        """Exibe a interface de entrada de caminho de arquivo"""
        self.clear_frames()
        
        # Label de instrução
        label = tk.Label(
            self.main_frame,
            text="Digite o caminho do arquivo (ESC para voltar):",
            font=self.base_font,
            bg="#CAE4F1"
        )
        label.pack(pady=20)
        
        # Campo de entrada
        self.entry_widget = tk.Entry(self.main_frame, font=self.base_font, width=50)
        self.entry_widget.pack(pady=10)
        self.entry_widget.focus()
        self.entry_widget.bind("<KeyRelease>", self.on_archive_key)
        self.entry_widget.bind("<Escape>", lambda e: self.back_to_menu())
        
        # Label para exibir o caminho
        self.path_display = tk.Label(
            self.main_frame,
            text=self.archive_path,
            font=self.base_font,
            bg="#CAE4F1",
            fg="black"
        )
        self.path_display.pack(pady=20)
        
        # Botão Carregar
        submit_btn = tk.Button(
            self.main_frame,
            text="Carregar",
            font=self.base_font,
            bg="#90EE90",
            command=self.load_archive
        )
        submit_btn.pack(pady=10)
        
        # Botão Voltar
        back_btn = tk.Button(
            self.main_frame,
            text="Voltar",
            font=self.base_font,
            bg="#FFB6C1",
            command=self.back_to_menu
        )
        back_btn.pack(pady=10)
    
    def on_typing_key(self, event):
        """Atualiza o texto enquanto digita"""
        self.user_text = self.entry_widget.get()
        self.text_display.config(text=self.user_text)
    
    def on_archive_key(self, event):
        """Atualiza o caminho enquanto digita"""
        self.archive_path = self.entry_widget.get()
        self.path_display.config(text=self.archive_path)
    
    def submit_typing(self):
        """Salva o texto digitado em um arquivo"""
        try:
            with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(self.user_text)
            messagebox.showinfo("Sucesso", "Texto salvo em 'arquivo.txt'")
            self.back_to_menu()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar arquivo: {str(e)}")
    
    def load_archive(self):
        """Carrega e exibe o conteúdo do arquivo"""
        try:
            if not os.path.exists(self.archive_path):
                messagebox.showerror("Erro", "Arquivo não encontrado!")
                return
            
            with open(self.archive_path, 'r', encoding='utf-8') as arquivo:
                content = arquivo.read()
            
            self.show_file_content(content)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir arquivo: {str(e)}")
    
    def show_file_content(self, content):
        """Exibe o conteúdo do arquivo"""
        self.clear_frames()
        
        # Título
        title = tk.Label(
            self.main_frame,
            text=f"Conteúdo de: {self.archive_path}",
            font=self.title_font,
            bg="#CAE4F1"
        )
        title.pack(pady=20)
        
        # Frame com scrollbar para o conteúdo
        scroll_frame = tk.Frame(self.main_frame, bg="#CAE4F1")
        scroll_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(scroll_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget para exibir o conteúdo
        text_widget = tk.Text(
            scroll_frame,
            font=self.base_font,
            height=20,
            width=80,
            yscrollcommand=scrollbar.set
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # Inserir conteúdo
        text_widget.insert(tk.END, content)
        text_widget.config(state=tk.DISABLED)  # Deixar como leitura apenas
        
        # Botão Voltar
        back_btn = tk.Button(
            self.main_frame,
            text="Voltar",
            font=self.base_font,
            bg="#FFB6C1",
            command=self.back_to_menu
        )
        back_btn.pack(pady=10)
    
    def back_to_menu(self):
        """Volta para o menu principal"""
        self.typing_active_dig = False
        self.typing_active_arq = False
        self.show_menu()
    
    def clear_frames(self):
        """Limpa todos os widgets do frame principal"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()