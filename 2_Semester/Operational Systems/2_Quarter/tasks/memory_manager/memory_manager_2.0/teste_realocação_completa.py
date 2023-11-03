import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
import itertools
import random
import string
import time

def process_name_generator():
    size = 1
    while True:
        for s in itertools.product(string.ascii_uppercase, repeat = size):
            yield "".join(s)
        size += 1

class memory_manager:
    def __init__(self, master):
        self.master = master
        self.grid = [None] * 100  # Altera para ter 100 posições no total.
        self.groups = {}
        self.chars = process_name_generator()
        self.status = [0] * 100  # Altera para ter 100 posições no total.
        self.create_grid()

    def create_grid(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True)
        for i in range(0, 100):  # Altera o range para começar em 0 e ir até 99.
            label = tk.Label(frame, bg="white", width=10, height=3, relief="solid", borderwidth=1.2)
            label.grid(row=i//10, column=i%10)  # Ajusta a posição do grid para começar em 0.
            self.grid[i] = label

    def allocate(self):
        n = tkinter.simpledialog.askinteger("Alocar", "Digite o Tamanho do Processo")
        free_blocks = []
        best_fit = None
        total_free = 0
        for i in range(0, 100):  # Altera o range para começar em 0 e ir até 99.
            if self.status[i] == 0:
                total_free += 1
                free_blocks.append(i)
            else:
                if len(free_blocks) >= n:
                    if best_fit is None or len(best_fit) > len(free_blocks):
                        best_fit = list(free_blocks)
                free_blocks = []
        if len(free_blocks) >= n:
            if best_fit is None or len(best_fit) > len(free_blocks):
                best_fit = list(free_blocks)
        if total_free < n:
            messagebox.showinfo("Erro", "Sem Espaço Total")
            return
        if best_fit is None:
            messagebox.showinfo("Erro", "Sem Espaço Sequencial")
            return
        block_color = "#{:06x}".format(random.randint(0x0000, 0xFFFFFF))
        block_name = next(self.chars)
        for k in range(n):
            self.grid[best_fit[k]]["text"] = block_name
            self.grid[best_fit[k]]["background"] = block_color
            self.groups[block_name] = block_color
            self.status[best_fit[k]] = 1

    def deallocate(self):
        d = tkinter.simpledialog.askstring("Desalocar", "Digite o Nome do Processo")
        for i in range(0, 100):  # Altera o range para começar em 0 e ir até 99.
            if self.grid[i]["text"] == d.upper():
                self.grid[i]['background'] = "white"
                self.grid[i]["text"] = ""
                self.status[i] = 0

    def full_deallocate(self):
        for i in range(0, 100):  # Altera o range para começar em 0 e ir até 99.
            if self.status[i] != 0:
                self.grid[i]["background"] = "white"
                self.grid[i]["text"] = ""
                self.status[i] = 0

    def reallocate(self):
        while True:    
            TamanhoMemoria = 0
            TextoMemoria = None
            for Pos in range(1, 100):  
                if self.status[Pos - 1] == 0 and self.status[Pos] == 1:
                    TextoMemoria = self.grid[Pos]["text"]
                    while Pos < 100 and self.grid[Pos]["text"] == TextoMemoria:
                        TamanhoMemoria += 1
                        Pos += 1
                    break
            if TextoMemoria is None:
                return self.grid 
            for Pos in range(0, 100):  
                if TextoMemoria == self.grid[Pos]["text"]:
                    self.grid[Pos]["text"] = ""
                    self.grid[Pos]["background"] = "white"
                    self.status[Pos] = 0
            for Pos in range(0, 100):  
                if self.status[Pos] == 0 and TamanhoMemoria > 0:
                    self.grid[Pos]["text"] = TextoMemoria
                    self.grid[Pos]["background"] = self.groups[TextoMemoria]
                    self.status[Pos] = 1
                    TamanhoMemoria -= 1
                    time.sleep(0.2)
        return self.grid


root = tk.Tk()
width = 800
height = 600
root.resizable(0, 0)
root.title('Gerenciador de Memória')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
mm = memory_manager(root)
button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x", pady=20)
allocate_button = tk.Button(button_frame, text="Alocar", command=mm.allocate, height=5, width=26, bg='gray', borderwidth=0)
allocate_button.pack(side="left", padx=5)
deallocate_button = tk.Button(button_frame, text="Desalocar", command=mm.deallocate, height=5, width=26, bg='gray', borderwidth=0)
deallocate_button.pack(side="left", padx=5)
full_deallocate_button = tk.Button(button_frame, text="Limpar Processos", command=mm.full_deallocate, height= 5, width=26, bg='gray', borderwidth=0)
full_deallocate_button.pack(side='left', padx=5)
reallocate_button = tk.Button(button_frame, text="Realocar", command=mm.reallocate, height=5, width=26, bg='gray', borderwidth=0)
reallocate_button.pack(side="left", padx=5)
root.mainloop()
