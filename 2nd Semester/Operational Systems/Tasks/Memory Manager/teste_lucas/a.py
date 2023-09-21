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
        for i in range(8):  # Altere o número de linhas aqui
            row = []
            for j in range(40):  # Altere o número de colunas aqui
                label = tk.Label(frame, bg="white", width=2, height=1, relief="solid", borderwidth=1)
                label.grid(row=i, column=j)
                label.bind("<Button-1>", self.select)
                row.append(label)
            self.grid.append(row)

    def allocate(self, n):
        free_blocks = []
        total_free = 0
        for i in range(8):
            for j in range(40):
                if self.grid[i][j]['bg'] == "white":
                    total_free += 1
                    free_blocks.append((i, j))
                    if len(free_blocks) == n:
                        for k in range(n):
                            self.grid[free_blocks[k][0]][free_blocks[k][1]]['bg'] = "blue"
                        return
                else:
                    free_blocks = []  # Limpa a lista se encontrar um bloco ocupado

        if total_free < n:
            messagebox.showinfo("Erro", "Não existe espaço disponível, favor liberar espaço!")
        else:
            messagebox.showinfo("Erro", "Não existe espaço sequencial, favor organize os processos!")

    def select(self, event):
        if event.widget['bg'] == "blue":
            event.widget['bg'] = "red"
            self.selected.append(event.widget)
        elif event.widget['bg'] == "red":
            event.widget['bg'] = "blue"
            self.selected.remove(event.widget)

    def deallocate(self):
        for widget in self.selected:
            widget['bg'] = "white"
        self.selected = []

    def organize(self):
        memory_blocks = []
        for i in range(8):
            for j in range(40):
                if self.grid[i][j]['bg'] == "blue":
                    memory_blocks.append((i,j))
                    self.grid[i][j]['bg'] = "white"

        index = 0
        x, y = 0, 0
        for i in range(8):
            for j in range(40):
                if index < len(memory_blocks):
                    if y == 40:
                        x += 1
                        y = 0
                    self.grid[x][y].grid(row=i, column=j)
                    self.grid[x][y]['bg'] = "blue"
                    index += 1
                    y += 1

root = tk.Tk()
root.geometry("800x300")  # Fixa o tamanho da janela
root.resizable(0, 0)  # Desativa a opção de tela cheia

title = tk.Label(root, text="Gerenciador de Memória", font=("Arial", 20))  # Adiciona um título
title.pack(pady=10)  # Posiciona o título acima da grade

mm = MemoryManager(root)

button_frame = tk.Frame(root)  # Cria um novo frame para os botões
button_frame.pack(side="top", fill="x", pady=20)  # Adiciona preenchimento vertical

allocate_button = tk.Button(button_frame, text="Alocar", command=lambda: mm.allocate(int(entry.get())), height=2, width=10)
allocate_button.pack(side="left", padx=10)

entry = tk.Entry(button_frame)
entry.pack(side="left")

deallocate_button = tk.Button(button_frame, text="Desalocar", command=mm.deallocate, height=2, width=10)
deallocate_button.pack(side="left", padx=10)

organize_button = tk.Button(button_frame, text="Organizar", command=mm.organize, height=2, width=10)
organize_button.pack(side="left", padx=10)

root.mainloop()