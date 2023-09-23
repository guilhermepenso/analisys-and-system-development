import tkinter as tk
from tkinter import messagebox
import random
import string
import tkinter.simpledialog
import itertools

# Função para gerar caracteres sequenciais pelo itertools

def process_name_generator():
    size = 1
    while True:
        for s in itertools.product(string.ascii_uppercase, repeat = size):
            yield "".join(s)
        size += 1
        
# Classe que engloba toda a parte do gerenciamento e lógica da memória

class memory_manager:
    
    # Função com declarações self
    
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.groups = {}
        self.process = {}
        self.chars = process_name_generator()
        self.create_grid()

    # Função para criação da tabela para alocar os processamentos de forma visual e lógica
    
    def create_grid(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True)
        for i in range(10):
            row = []
            for j in range(10):
                label = tk.Label(frame, bg="white", width=10, height=3, relief="solid", borderwidth=1.2)
                label.grid(row=i, column=j)
                label.bind("<Button-1>")
                row.append(label)
            self.grid.append(row)

    def allocate(self):
        n = tkinter.simpledialog.askinteger("Alocar", "Qual o tamanho do processo a ser alocado?")
        free_blocks = []
        total_free = 0
        best_fit = None
        for i in range(10):
            for j in range(10):
                if (self.grid[i][j]['background'] == "white"):
                    total_free += 1
                    free_blocks.append((i, j))
                else:
                    if len(free_blocks) >= n:
                        if best_fit is None or len(best_fit) > len(free_blocks):
                                best_fit = list(free_blocks)
                        free_blocks = []
        if len(free_blocks) >= n and (best_fit is None or len(best_fit) > len(free_blocks)):
            best_fit = list(free_blocks)
        if total_free < n:
            messagebox.showinfo("Erro", "Sem Espaço Total")
            return
        if best_fit is None:
            messagebox.showinfo("Erro", "Sem Espaço Sequencial")
            return
        color= "#{:06x}".format(random.randint(0x0000, 0xFFFFFF))
        id_group = next(self.chars)
        for k in range(n):
            self.grid[best_fit[k][0]][best_fit[k][1]]["background"] = color
            self.grid[best_fit[k][0]][best_fit[k][1]]["text"] = id_group
        self.groups[id_group] = color
                        
    def deallocate(self):
        d = tkinter.simpledialog.askstring("Desalocar", "Qual o nome do processo que será desalocado?")
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]["text"] == d.upper():
                    self.grid[i][j]['background'] = "white"
                    self.grid[i][j]["text"] = ""

    def reallocate(self):
        memory_blocks = []
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]['background'] != "white":
                    memory_blocks.append((i, j, self.grid[i][j]["text"], self.grid[i][j]["background"]))
                    self.grid[i][j]['background'] = "white"
                    self.grid[i][j]['text'] = ""
        index = 0
        x, y = 0, 0
        for i in range(10):
            for j in range(10):
                if index < len(memory_blocks):
                    if y == 10:
                        x += 1
                        y = 0
                    self.grid[x][y].grid(row=i, column=j)
                    self.grid[x][y]['background'] = memory_blocks[index][3]
                    self.grid[x][y]['text'] = memory_blocks[index][2]
                    index += 1
                root.update()
                y += 1

root = tk.Tk()
root.geometry("800x600")  # Fixa o tamanho da janela
root.resizable(0, 0)  # Desativa a opção de tela cheia
root.title('Gerenciador de Memória')
root.iconbitmap("2nd Semester\Operational Systems\Tasks\Memory Manager\RAM.ico")

mm = memory_manager(root)

button_frame = tk.Frame(root)  # Cria um novo frame para os botões
button_frame.pack(side="top", fill="x", pady=20)  # Adiciona preenchimento vertical

allocate_button = tk.Button(button_frame, text="Alocar", command=mm.allocate, height=5, width=35,  bg='gray')
allocate_button.pack(side="left", padx=5)

deallocate_button = tk.Button(button_frame, text="Desalocar", command=mm.deallocate, height=5, width=35,  bg='gray')
deallocate_button.pack(side="left", padx=5)

reallocate_button = tk.Button(button_frame, text="Realocar", command=mm.reallocate, height=5, width=35,  bg='gray')
reallocate_button.pack(side="left", padx=5)

root.mainloop()