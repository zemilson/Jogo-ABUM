import tkinter as tk
from tkinter import ttk, messagebox
import models
from datetime import datetime

class ChurchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Santuário Manager - Sistema de Gestão de Igreja")
        self.root.geometry("1100x700")
        
        # Configuração de cores
        self.bg_color = "#f0f2f5"
        self.sidebar_color = "#1c1e21"
        self.accent_color = "#1877f2"
        self.text_color = "#ffffff"
        
        self.root.configure(bg=self.bg_color)
        
        # Layout Principal
        self.setup_layout()
        self.show_dashboard()

    def setup_layout(self):
        # Sidebar
        self.sidebar = tk.Frame(self.root, width=220, bg=self.sidebar_color, relief='flat')
        self.sidebar.pack(expand=False, fill='both', side='left')
        self.sidebar.pack_propagate(False)
        
        # Header do Sidebar
        tk.Label(self.sidebar, text="SANTUÁRIO", bg=self.sidebar_color, fg=self.accent_color, 
                 font=("Helvetica", 18, "bold"), pady=30).pack()
        
        # Botões do Sidebar
        menu_items = [
            ("Dashboard", self.show_dashboard),
            ("Membros", self.show_membros),
            ("Finanças", self.show_financas),
            ("Eventos", self.show_eventos),
            ("Configurações", self.show_settings)
        ]
        
        for text, command in menu_items:
            btn = tk.Button(self.sidebar, text=text, command=command, bg=self.sidebar_color, 
                          fg=self.text_color, font=("Helvetica", 11), relief="flat", 
                          activebackground=self.accent_color, activeforeground="white",
                          anchor="w", padx=30, pady=12, cursor="hand2", bd=0)
            btn.pack(fill='x')

        # Conteúdo Principal
        self.main_content = tk.Frame(self.root, bg=self.bg_color)
        self.main_content.pack(expand=True, fill='both', side='right')

    def clear_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def create_header(self, title):
        header_frame = tk.Frame(self.main_content, bg="white", height=70)
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text=title, bg="white", fg="#1c1e21", 
                 font=("Helvetica", 16, "bold"), padx=30).pack(side='left', fill='y')

    # --- Dashboard ---
    def show_dashboard(self):
        self.clear_content()
        self.create_header("Visão Geral")
        
        content_frame = tk.Frame(self.main_content, bg=self.bg_color, padx=30, pady=30)
        content_frame.pack(expand=True, fill='both')
        
        # Dados para o Dashboard
        membros = models.get_membros()
        transacoes = models.get_transacoes()
        total_membros = len(membros)
        total_entradas = sum(t[3] for t in transacoes if t[1] == 'Entrada')
        total_saidas = sum(t[3] for t in transacoes if t[1] == 'Saída')
        saldo = total_entradas - total_saidas
        
        # Grid de Cards
        cards_frame = tk.Frame(content_frame, bg=self.bg_color)
        cards_frame.pack(fill='x')
        
        self.create_card(cards_frame, "Membros Ativos", str(total_membros), "#1877f2", 0)
        self.create_card(cards_frame, "Saldo em Caixa", f"R$ {saldo:.2f}", "#2ecc71", 1)
        self.create_card(cards_frame, "Entradas (Mês)", f"R$ {total_entradas:.2f}", "#3498db", 2)

    def create_card(self, parent, title, value, color, column):
        card = tk.Frame(parent, bg="white", padx=20, pady=20, relief="flat", highlightbackground="#ddd", highlightthickness=1)
        card.grid(row=0, column=column, padx=10, sticky="nsew")
        parent.grid_columnconfigure(column, weight=1)
        
        tk.Label(card, text=title, bg="white", fg="#65676b", font=("Helvetica", 10, "bold")).pack(anchor="w")
        tk.Label(card, text=value, bg="white", fg=color, font=("Helvetica", 18, "bold"), pady=10).pack(anchor="w")

    # --- Membros ---
    def show_membros(self):
        self.clear_content()
        self.create_header("Gestão de Membros")
        
        container = tk.Frame(self.main_content, bg=self.bg_color, padx=30, pady=20)
        container.pack(expand=True, fill='both')
        
        # Toolbar
        toolbar = tk.Frame(container, bg=self.bg_color)
        toolbar.pack(fill='x', pady=(0, 20))
        
        tk.Button(toolbar, text="+ Adicionar Membro", command=self.add_membro_dialog, 
                  bg=self.accent_color, fg="white", font=("Helvetica", 10, "bold"), 
                  padx=15, pady=8, relief="flat", cursor="hand2").pack(side='left')
        
        # Tabela
        columns = ("ID", "Nome", "Telefone", "E-mail", "Status")
        self.tree_membros = ttk.Treeview(container, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_membros.heading(col, text=col)
            self.tree_membros.column(col, width=150)
        
        self.tree_membros.pack(expand=True, fill='both')
        self.refresh_membros_list()

    def refresh_membros_list(self):
        for item in self.tree_membros.get_children():
            self.tree_membros.delete(item)
        for m in models.get_membros():
            # ID, Nome, Telefone, Email, Status (ajustar índices conforme banco)
            self.tree_membros.insert('', 'end', values=(m[0], m[1], m[3], m[4], m[7]))

    def add_membro_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Novo Membro")
        dialog.geometry("400x500")
        dialog.configure(padx=20, pady=20)
        
        fields = [("Nome Completo", "nome"), ("Endereço", "endereco"), ("Telefone", "telefone"), ("E-mail", "email")]
        entries = {}
        
        for label_text, key in fields:
            tk.Label(dialog, text=label_text, font=("Helvetica", 10)).pack(anchor="w", pady=(10, 2))
            entry = tk.Entry(dialog, font=("Helvetica", 11), width=40)
            entry.pack(pady=(0, 5))
            entries[key] = entry
            
        def save():
            data = {k: v.get() for k, v in entries.items()}
            if not data['nome']:
                messagebox.showerror("Erro", "O nome é obrigatório.")
                return
            
            models.add_membro(data['nome'], data['endereco'], data['telefone'], data['email'], "", "")
            messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso!")
            dialog.destroy()
            self.refresh_membros_list()
            
        tk.Button(dialog, text="Salvar Membro", command=save, bg=self.accent_color, fg="white", 
                  font=("Helvetica", 10, "bold"), pady=10, width=30, relief="flat", cursor="hand2").pack(pady=20)

    # --- Finanças ---
    def show_financas(self):
        self.clear_content()
        self.create_header("Gestão Financeira")
        
        container = tk.Frame(self.main_content, bg=self.bg_color, padx=30, pady=20)
        container.pack(expand=True, fill='both')
        
        # Toolbar
        toolbar = tk.Frame(container, bg=self.bg_color)
        toolbar.pack(fill='x', pady=(0, 20))
        
        tk.Button(toolbar, text="+ Nova Transação", command=self.add_transacao_dialog, 
                  bg="#2ecc71", fg="white", font=("Helvetica", 10, "bold"), 
                  padx=15, pady=8, relief="flat", cursor="hand2").pack(side='left')
        
        # Tabela de Transações
        columns = ("ID", "Tipo", "Categoria", "Valor", "Data", "Membro", "Descrição")
        self.tree_financas = ttk.Treeview(container, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_financas.heading(col, text=col)
            self.tree_financas.column(col, width=120)
        
        self.tree_financas.pack(expand=True, fill='both')
        self.refresh_financas_list()

    def refresh_financas_list(self):
        for item in self.tree_financas.get_children():
            self.tree_financas.delete(item)
        for f in models.get_transacoes():
            self.tree_financas.insert('', 'end', values=f)

    def add_transacao_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Nova Transação")
        dialog.geometry("400x550")
        dialog.configure(padx=20, pady=20)
        
        tk.Label(dialog, text="Tipo (Entrada/Saída):").pack(anchor="w")
        tipo_var = tk.StringVar(value="Entrada")
        ttk.Combobox(dialog, textvariable=tipo_var, values=["Entrada", "Saída"]).pack(fill='x', pady=5)
        
        tk.Label(dialog, text="Categoria:").pack(anchor="w")
        cat_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=cat_var, values=["Dízimo", "Oferta", "Despesa", "Outros"]).pack(fill='x', pady=5)
        
        tk.Label(dialog, text="Valor (R$):").pack(anchor="w")
        valor_entry = tk.Entry(dialog)
        valor_entry.pack(fill='x', pady=5)
        
        tk.Label(dialog, text="Descrição:").pack(anchor="w")
        desc_entry = tk.Entry(dialog)
        desc_entry.pack(fill='x', pady=5)
        
        def save():
            try:
                valor = float(valor_entry.get().replace(',', '.'))
                data_hoje = datetime.now().strftime("%Y-%m-%d")
                models.add_transacao(tipo_var.get(), cat_var.get(), valor, data_hoje, None, desc_entry.get())
                messagebox.showinfo("Sucesso", "Transação registrada!")
                dialog.destroy()
                self.refresh_financas_list()
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido.")
        
        tk.Button(dialog, text="Registrar", command=save, bg="#2ecc71", fg="white", 
                  font=("Helvetica", 10, "bold"), pady=10, relief="flat").pack(pady=20, fill='x')

    # --- Eventos ---
    def show_eventos(self):
        self.clear_content()
        self.create_header("Calendário de Eventos")
        
        container = tk.Frame(self.main_content, bg=self.bg_color, padx=30, pady=20)
        container.pack(expand=True, fill='both')
        
        # Toolbar
        toolbar = tk.Frame(container, bg=self.bg_color)
        toolbar.pack(fill='x', pady=(0, 20))
        
        tk.Button(toolbar, text="+ Novo Evento", command=self.add_evento_dialog, 
                  bg="#e67e22", fg="white", font=("Helvetica", 10, "bold"), 
                  padx=15, pady=8, relief="flat", cursor="hand2").pack(side='left')
        
        # Tabela
        columns = ("ID", "Título", "Data", "Hora", "Local", "Descrição")
        self.tree_eventos = ttk.Treeview(container, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_eventos.heading(col, text=col)
            self.tree_eventos.column(col, width=120)
        
        self.tree_eventos.pack(expand=True, fill='both')
        self.refresh_eventos_list()

    def refresh_eventos_list(self):
        for item in self.tree_eventos.get_children():
            self.tree_eventos.delete(item)
        for e in models.get_eventos():
            self.tree_eventos.insert('', 'end', values=e)

    def add_evento_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Novo Evento")
        dialog.geometry("400x550")
        dialog.configure(padx=20, pady=20)
        
        fields = [("Título do Evento", "titulo"), ("Data (AAAA-MM-DD)", "data"), 
                  ("Hora (HH:MM)", "hora"), ("Local", "local"), ("Descrição", "descricao")]
        entries = {}
        
        for label_text, key in fields:
            tk.Label(dialog, text=label_text).pack(anchor="w", pady=(10, 2))
            entry = tk.Entry(dialog, width=40)
            entry.pack(pady=(0, 5))
            entries[key] = entry
            
        def save():
            data = {k: v.get() for k, v in entries.items()}
            if not data['titulo'] or not data['data']:
                messagebox.showerror("Erro", "Título e Data são obrigatórios.")
                return
            
            models.add_evento(data['titulo'], data['data'], data['hora'], data['local'], data['descricao'])
            messagebox.showinfo("Sucesso", "Evento agendado!")
            dialog.destroy()
            self.refresh_eventos_list()
            
        tk.Button(dialog, text="Salvar Evento", command=save, bg="#e67e22", fg="white", 
                  font=("Helvetica", 10, "bold"), pady=10, width=30, relief="flat").pack(pady=20)

    def show_settings(self):
        self.clear_content()
        self.create_header("Configurações")
        tk.Label(self.main_content, text="Configurações do Sistema", bg=self.bg_color, pady=50).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChurchApp(root)
    root.mainloop()
