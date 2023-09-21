# LÓGICA
    # ALOCAR PRECISA SER EM BLOCOS
        # ALOCAR PRECISA NOMEAR O PROCESSO E COLOCAR COR RANDOM EM CADA ALOCAÇÃO
        # PRECISA DE BEST FIT IMPLEMENTADO
        ## VISUALMENTE ABRIR UM POP UP PARA PREENCHER COM OS DADOS NO TKINTER
    # DESALOCAR PRECISA SER EM BLOCOS
        # DESALOCAR PRECISA SER PELO NOME O PROCESSO 
        # FUNÇÃO DE DESALOCAR TODOS OS PROCESSOS
        ## VISUALMENTE ABRIR UM POP UP PARA PREENCHER COM OS DADOS NO TKINTER
    # REALOCAR PELOS BLOCOS
        

import tkinter as tk
from tkinter import messagebox

class MemoryManager:
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.selected = []
        self.create_grid()

    def create_grid(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True)
        for i in range(10):  # Altere o número de linhas aqui
            row = []
            for j in range(10):  # Altere o número de colunas aqui
                label = tk.Label(frame, bg="white", width=3, height=1, relief="solid", borderwidth=1)
                label.grid(row=i, column=j)
                label.bind("<Button-1>", self.select)
                row.append(label)
            self.grid.append(row)


    def allocate(self, n):
        free_blocks = []
        total_free = 0
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]['bg'] == "white":
                    total_free += 1
                    free_blocks.append((i, j))
                    if len(free_blocks) == n:
                        for k in range(n):
                            self.grid[free_blocks[k][0]][free_blocks[k][1]]['bg'] = "green"
                        return
                else:
                    free_blocks = []  # Limpa a lista se encontrar um bloco ocupado

        if total_free < n:
            messagebox.showinfo("Erro", "Sem espaço, precisa liberar espaço!")
        else:
            messagebox.showinfo("Erro", "Sem espaço sequencial, realocar os processos!")

    def select(self, event):
        if event.widget['bg'] == "green":
            event.widget['bg'] = "red"
            self.selected.append(event.widget)
        elif event.widget['bg'] == "red":
            event.widget['bg'] = "green"
            self.selected.remove(event.widget)

    def deallocate(self):
        for widget in self.selected:
            widget['bg'] = "white"
        self.selected = []

    def organize(self):
        memory_blocks = []
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]['bg'] == "green":
                    memory_blocks.append((i,j))
                    self.grid[i][j]['bg'] = "white"

        index = 0
        x, y = 0, 0
        for i in range(10):
            for j in range(10):
                if index < len(memory_blocks):
                    if y == 10:
                        x += 1
                        y = 0
                    self.grid[x][y].grid(row=i, column=j)
                    self.grid[x][y]['bg'] = "green"
                    index += 1
                    y += 1

root = tk.Tk()
root.geometry("400x350")  # Fixa o tamanho da janela
root.resizable(0, 0)  # Desativa a opção de tela cheia

title = tk.Label(root, text="", font=("Arial", 20))  # Adiciona um título
title.pack(pady=10)  # Posiciona o título acima da grade

mm = MemoryManager(root)

button_frame = tk.Frame(root)  # Cria um novo frame para os botões
button_frame.pack(side="top", fill="x", pady=20)  # Adiciona preenchimento vertical

allocate_button = tk.Button(button_frame, text="Alocar", command=lambda: mm.allocate(int(entry.get())), height=2, width=10)
allocate_button.pack(side="left", padx=5)

entry = tk.Entry(button_frame)
entry.pack(side="left")

deallocate_button = tk.Button(button_frame, text="Desalocar", command=mm.deallocate, height=2, width=10)
deallocate_button.pack(side="left", padx=10)

organize_button = tk.Button(button_frame, text="Realocar", command=mm.organize, height=2, width=10)
organize_button.pack(side="left", padx=10)

root.mainloop()