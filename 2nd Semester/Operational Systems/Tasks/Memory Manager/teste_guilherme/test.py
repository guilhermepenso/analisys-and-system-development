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

    def organize(s
