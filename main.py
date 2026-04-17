'''
Ponto de entrada principal do sistema Santuário Manager.
Este script inicializa o banco de dados e abre a interface gráfica.
'''
import tkinter as tk
import database
from ui import ChurchApp

def main():
    # Inicializa o banco de dados e cria as tabelas se necessário
    database.create_tables()
    
    # Inicia a interface gráfica
    root = tk.Tk()
    app = ChurchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
