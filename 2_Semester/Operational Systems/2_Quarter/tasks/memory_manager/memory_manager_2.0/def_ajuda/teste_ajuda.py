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
        return self.grid 


    def help():
        janela_ajuda = tk.Toplevel()
        janela_ajuda.title("Ajuda")
        janela_ajuda.geometry("1000x1000")
        Info = Label(janela_ajuda,text= "Explicação do funcionamento de cada botão")
        Info.pack(padx=10,pady=10)
        nb=ttk.Notebook(janela_ajuda,width=1000,height=900)
        nb.pack(padx=10,pady=10)
        funcionamento = Frame(nb)
        nb.add(funcionamento,text="Funcionamento do Programa")

        label_funcionamento = Label(funcionamento, text="Esse Programa simula uma memória de um computador.\nVocê poderá alocar processos em uma memória com até 100 blocos de memória\nOs processos serão criadas em ordem alfabética, e cores aleatórias.\nVocê poderá desalocar um processo especifico da memória dizendo apenas o Nome dele(letra).\nO programa possue um botão limpar processos que ao ser clicado, apagará tudo o que tiver na memória.\nConforme o uso do programa uma memória com espaços vazios nos endereços menores poderá ficar lenta.\nEntão o programa possue um botão chamado realocar que toda vez clicado,\nRealocará um bloco de processos até o inicio da memória")
        label_funcionamento.pack(pady=70,anchor=CENTER, fill="both")
        label_criadores = Label(funcionamento,text= "Esse programa foi desenvolvido por: Guilherme Penso, Matheus Guilherme, Murilo Lustosa e Emanoel Andre.")
        label_criadores.pack(padx=10,pady=10)
        label_criadores.config(font="Arial 12")
        Alocar= Frame(nb)
        label_info=Label(Alocar,text="Funcionamento do Botão Alocar.")
        label_info.pack(padx=10,pady=10)
        label_imagealocar1=Label(Alocar,text="",image=img/alocar1)
        label_imagealocar1.pack(padx=10,pady=10)
        mensagealocar= Label(Alocar,text="A Memória estará em branco.")
        mensagealocar.pack()
        label_gridalocar=Label(Alocar,text="",image=img/gridbranco)
        label_gridalocar.pack()
        mensagealocar2=Label(Alocar,text="Após o clicar no botão Alocar, abrirá a seguinte aba, que adicionarei um processo de tamanho 5, como exemplo.")
        mensagealocar2.pack()
        label_imagemalocar2=Label(Alocar,text="",image=img/alocar2)
        label_imagemalocar2.pack()
        mensagealocar3=Label(Alocar,text="Após clicar OK,a Memória adicionará um processo com 5 blocos, com o nome 'A'.")
        mensagealocar3.pack()
        label_imagemalocar3=Label(Alocar,text="",image=img/alocar3)
        label_imagemalocar3.pack()
        nb.add(Alocar,text ="Alocar")

        Desalocar = Frame(nb)
        label_info2 = Label(Desalocar, text="Funcionamento do Botão Desalocar.")
        label_info2.pack(padx=10, pady=10)
        label_imagedesalocar1 = Label(Desalocar, text="", image=img/desalocar1)
        label_imagedesalocar1.pack(padx=10, pady=10)
        mensagedesalocar = Label(Desalocar, text="A Memória estará com um processo 'B' com o tamanho de 7 blocos.")
        mensagedesalocar.pack()
        label_griddesalocar = Label(Desalocar, text="", image=img/desalocar2)
        label_griddesalocar.pack()
        mensagedesalocar2 = Label(Desalocar,
                            text="Após clicar no botão Desalocar, abrirá a seguinte aba, que digitariei o Nome do processo que quero remover, o processo neste caso, é o Processo 'B'.")
        mensagedesalocar2.pack()
        label_imagemdesalocar2 = Label(Desalocar, text="", image=img/desalocar3)
        label_imagemdesalocar2.pack()
        mensagedesalocar3 = Label(Desalocar, text="Após clicar OK,a Memória removerá o Processo digitado.")
        mensagedesalocar3.pack()
        label_imagemdesalocar3 = Label(Desalocar, text="", image=img/gridbranco)
        label_imagemdesalocar3.pack()
        nb.add(Desalocar,text="Desalocar")

        Desalocar_tudo = Frame(nb)
        label_info3 = Label(Desalocar_tudo, text="Funcionamento do Botão Limpar Processos.")
        label_info3.pack(padx=10, pady=10)
        label_imagelimpar1 = Label(Desalocar_tudo, text="", image=img/limpar1)
        label_imagelimpar1.pack(padx=10, pady=10)
        mensagelimpar1 = Label(Desalocar_tudo, text="A Memória com algums processos:")
        mensagelimpar1.pack()
        label_imagelimpar2 = Label(Desalocar_tudo, text="", image=img/limpar2)
        label_imagelimpar2.pack()
        mensagalimpar3 = Label(Desalocar_tudo,text="Após você clique no botão Limpar Processos, a Memória apagará tudo, exemplo abaixo:")
        mensagalimpar3.pack()
        label_imagegrid = Label(Desalocar_tudo,text="",image=img/gridbranco)
        label_imagegrid.pack()
        nb.add(Desalocar_tudo,text= "Limpar Processos")

        Realocar = Frame(nb)
        label_info4 = Label(Realocar, text="Funcionamento do Botão Limpar Processos.")
        label_info4.pack(padx=10, pady=10)
        label_Realocar1 = Label(Realocar, text="", image=img/realocar1)
        label_Realocar1.pack(padx=10, pady=10)
        mensageRealocar1 = Label(Realocar, text="A Memória com algums processos, e um endereço livre, para melhorar o desempenho da memória você clica em Realocar")
        mensageRealocar1.pack()
        label_Realocar2 = Label(Realocar,text="",image=img/realocar2)
        label_Realocar2.pack()
        mensageRealocar2 = Label(Realocar,text="Após Clicar no botão Realocar,o primeiro Processo encontrado irá para o começo da memória como no exemplo abaixo: ")
        mensageRealocar2.pack()
        label_Realocar3 = Label(Realocar,text="",image=img/realocar3)
        label_Realocar3.pack()
        mensageRealocar3 = Label(Realocar,text=" Você pode realocar toda vez que desejar. ")
        mensageRealocar3.pack()
        nb.add(Realocar, text="Realocar")

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
allocate_button = tk.Button(button_frame, text="Alocar", command=mm.allocate, height=5, width=21, bg='gray', borderwidth=0)
allocate_button.pack(side="left", padx=5)
deallocate_button = tk.Button(button_frame, text="Desalocar", command=mm.deallocate, height=5, width=21, bg='gray', borderwidth=0)
deallocate_button.pack(side="left", padx=5)
full_deallocate_button = tk.Button(button_frame, text="Limpar Processos", command=mm.full_deallocate, height= 5, width=21, bg='gray', borderwidth=0)
full_deallocate_button.pack(side='left', padx=5)
reallocate_button = tk.Button(button_frame, text="Realocar", command=mm.reallocate, height=5, width=21, bg='gray', borderwidth=0)
reallocate_button.pack(side="left", padx=5)
help_button = tk.Button(button_frame, text="Help", command=mm.help, height=5, width=21, bg='gray', borderwidth=0)
help_button.pack(side="left", padx=5)
root.mainloop()
