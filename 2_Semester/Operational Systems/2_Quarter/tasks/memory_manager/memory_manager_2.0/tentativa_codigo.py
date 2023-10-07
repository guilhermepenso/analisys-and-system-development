# bitmap de 100 espaços
# cada bit pode ser= 0: livre / 1: ocupado
# lista encadeada contendo as memórias livres e alocadas
# posição inicial do processo na lista encadeada
# largura ou tamanho do processo

import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox
import itertools
import random
import time

def process_Name_Generator():
    size = 1
    while True:
        for s in itertools.produtct(string.ascii_uppercase, repeat = size):
            yield " ".join(s)
        size += 1

def 

class Memory_Manager:
    
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.groups = {}
        self.chars = process_Name_Generator()
        self.create_Grid()

    def create_grid(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True)
        for i in range(10):
            row = []
            for j in range(10):
                self.grid[i][j] = 0;
                label = tk.Label(frame, bg="white", width=10, height=3, relief="solid", borderwidth=1.2)
                label.grid(row=i, column=j)
                label.bind("<Button-1>")
                row.append(label)
            self.grid.append(row)

    def allocate(self):
        process_Size = input ("Digite o tamanho do processo: ")
        total_free = 0
        free_blocks = []
        for i in range(10):
            for j in range(10):
                if self.grid[i][j] != 0:
                    if best_fit is None or len(best_fit) > len(free_blocks):
                        best_fit = list(free_blocks)
                    free_blocks = []
                else:
                    total_free += 1
                    free_blocks.append([i][j])
        if best_fit 
                        