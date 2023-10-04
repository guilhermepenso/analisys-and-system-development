# FALTA alterar Realocação para mostrar animação por blocos
# FALTA botão de help
# ?? verificar não por cor, mas por bits 0 e 1 a disponibilidade do endereço

import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
import itertools
import random
import string
import time

# Gerador de Letras para Nomear os Processos
def process_name_generator():
    size = 1
    while True:
        for s in itertools.product(string.ascii_uppercase, repeat = size):
            yield "".join(s)
        size += 1
class memory_manager:

# Declaração Self / Master para visual no Tkinter   
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.groups = {}
        self.chars = process_name_generator()
        self.create_grid()

# Criação da Grade com Linhas e Colunas, definição da Cor do Fundo de cada Slot
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

# Função de alocar memória
    def allocate(self):
        n = tkinter.simpledialog.askinteger("Alocar", "Digite o Tamanho do Processo")
        free_blocks = []
        best_fit = None
        total_free = 0
        # Pesquisa dentro da grid 
        for i in range(10):
            for j in range(10):
                # Verificação dos blocos vazios, se verdadeiro aumenta os blocos livres totais e os blocos livres
                if self.grid[i][j]["background"] == "white":
                    total_free += 1
                    free_blocks.append((i, j))
                else: 
                    if len(free_blocks) >= n:
                        if best_fit is None or len(best_fit) > len(free_blocks):
                            best_fit = list(free_blocks)
                    free_blocks = []
        # Quando terminar de verificar todas as grids, terá outro processo de verificação se o valor digitado é maior que os blocos disponíveis         
        if len(free_blocks) >= n:
            if best_fit is None or len(best_fit) > len(free_blocks):
                            best_fit = list(free_blocks)              
        # Se o valor digitado for maior que o total livre, uma mensagem de erro aparecerá                   
        if total_free < n:
            messagebox.showinfo("Erro", "Sem Espaço Total")
            return
        # Se o a lista de blocos disponíveis nos free_blocks for menor, uma mensagem aparecerá que não tem espaço sequencial
        if best_fit is None:
            messagebox.showinfo("Erro", "Sem Espaço Sequencial")
            return
        # Gerador de cores e letrar para cada processo
        color = "#{:06x}".format(random.randint(0x0000, 0xFFFFFF))
        id_group = next(self.chars)
        
        # Separação de blocos de processos com os nomes e cores
        for k in range(n):
            self.grid[best_fit[k][0]][best_fit[k][1]]["background"] = color
            self.grid[best_fit[k][0]][best_fit[k][1]]["text"] = id_group
        self.groups[id_group] = color

    def deallocate(self):
        d = tkinter.simpledialog.askstring("Desalocar", "Digite o Nome do Processo")
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]["text"] == d.upper():
                    self.grid[i][j]['background'] = "white"
                    self.grid[i][j]["text"] = ""
    
    def full_deallocate(self):
        for i in range(10):
            for j in range(10):
                if self.grid[i][j]["background"] != "white":
                    self.grid[i][j]["background"] = "white"
                    self.grid[i][j]["text"] = ""
    # Função de realocação na memória
    def reallocate(self):
        memory_blocks = []
        
        # Procura dentro da grid dos processos
        for i in range(10):
            for j in range(10):
                
                # Verificação de processos que estão ocupados
                if self.grid[i][j]['background'] != "white":
                    
                    # Salva os processos ocupadas no memory_blocks 
                    memory_blocks.append((i, j, self.grid[i][j]["text"], self.grid[i][j]["background"]))
                    
                    # Altera os dados atuais para não ocupados visualmente
                    self.grid[i][j]['background'] = "white"
                    self.grid[i][j]['text'] = ""
                    
        # Declaração de variáveis para coordenadas de realocação
        index = 0
        x, y = 0, 0
        
        # Procura dentro da grid dos processos
        for i in range(10):
            for j in range(10):
                
                # Verifica a quantidade restante de processos dos memory_blocks
                if index < len(memory_blocks):
                    if y == 10:
                        x += 1
                        y = 0
                    self.grid[x][y].grid(row=i, column=j)
                    
                    # Preenche novamente a partir das primeiras posições os blocos guardado na memory_blocks
                    self.grid[x][y]['background'] = memory_blocks[index][3]
                    self.grid[x][y]['text'] = memory_blocks[index][2]
                    # Aumenta o index para verificar o if 
                    index += 1
                    
                # Root atualiza a tela
                root.update()
                
                # Timer visual para realocação lenta
                time.sleep(0.05)
                y += 1

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
allocate_button = tk.Button(button_frame, text="Alocar", command=mm.allocate, height=5, width=26,  bg='gray', borderwidth=0)
allocate_button.pack(side="left", padx=5)
deallocate_button = tk.Button(button_frame, text="Desalocar", command=mm.deallocate, height=5, width=26,  bg='gray', borderwidth=0)
deallocate_button.pack(side="left", padx=5)
full_deallocate_button = tk.Button(button_frame, text="Limpar Processos", command=mm.full_deallocate, height= 5, width=26, bg='gray', borderwidth=0)
full_deallocate_button.pack(side='left', padx=5)
reallocate_button = tk.Button(button_frame, text="Realocar", command=mm.reallocate, height=5, width=26,  bg='gray', borderwidth=0)
reallocate_button.pack(side="left", padx=5)

root.mainloop()