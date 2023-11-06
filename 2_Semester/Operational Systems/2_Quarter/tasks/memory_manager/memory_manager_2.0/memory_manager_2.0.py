import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
import itertools
import random
import string

def gerador_nome_processo():
    tamanho = 1
    while True:
        for s in itertools.product(string.ascii_uppercase, repeat=tamanho):
            yield "".join(s)
        tamanho += 1

class GerenciadorMemoria:
    def __init__(self, mestre):
        self.mestre = mestre
        self.grade = [None] * 100
        self.grupos = {}
        self.chars = gerador_nome_processo()
        self.status = [0] * 100
        self.criar_grade()

    def criar_grade(self):
        quadro = tk.Frame(self.mestre)
        quadro.pack(expand=True)
        for i in range(100):
            rotulo = tk.Label(quadro, bg="white", width=10, height=3, relief="solid", borderwidth=1.2)
            rotulo.grid(row=i//10, column=i%10)
            self.grade[i] = rotulo

    def alocar(self):
        n = tkinter.simpledialog.askinteger("Alocar", "Digite o Tamanho do Processo")
        blocos_livres = []
        melhor_ajuste = None
        total_livre = 0
        for i in range(100):
            if self.status[i] == 0:
                total_livre += 1
                blocos_livres.append(i)
            else:
                if len(blocos_livres) >= n:
                    if melhor_ajuste is None or len(melhor_ajuste) > len(blocos_livres):
                        melhor_ajuste = list(blocos_livres)
                blocos_livres = []
        if len(blocos_livres) >= n:
            if melhor_ajuste is None or len(melhor_ajuste) > len(blocos_livres):
                melhor_ajuste = list(blocos_livres)
        if total_livre < n:
            messagebox.showinfo("Erro", "Sem Espaço Total")
            return
        if melhor_ajuste is None:
            messagebox.showinfo("Erro", "Sem Espaço Sequencial")
            return
        cor_bloco = "#{:06x}".format(random.randint(0x0000, 0xFFFFFF))
        nome_bloco = next(self.chars)
        for k in range(n):
            self.grade[melhor_ajuste[k]]["text"] = nome_bloco
            self.grade[melhor_ajuste[k]]["background"] = cor_bloco
            self.grupos[nome_bloco] = cor_bloco
            self.status[melhor_ajuste[k]] = 1

    def desalocar(self):
        d = tkinter.simpledialog.askstring("Desalocar", "Digite o Nome do Processo")
        for i in range(100):
            if self.grade[i]["text"] == d.upper():
                self.grade[i]['background'] = "white"
                self.grade[i]["text"] = ""
                self.status[i] = 0

    def limpar_processos(self):
        for i in range(100):
            if self.status[i] != 0:
                self.grade[i]["background"] = "white"
                self.grade[i]["text"] = ""
                self.status[i] = 0

    def realocar(self):
        tamanho_memoria = 0
        texto_memoria = None
        for pos in range(1, 100):
            if self.status[pos - 1] == 0 and self.status[pos] == 1:
                texto_memoria = self.grade[pos]["text"]
                while pos < 100 and self.grade[pos]["text"] == texto_memoria:
                    tamanho_memoria += 1
                    pos += 1
                break
        if texto_memoria is None:
            return self.grade
        for pos in range(100):
            if texto_memoria == self.grade[pos]["text"]:
                self.grade[pos]["text"] = ""
                self.grade[pos]["background"] = "white"
                self.status[pos] = 0
        for pos in range(100):
            if self.status[pos] == 0 and tamanho_memoria > 0:
                self.grade[pos]["text"] = texto_memoria
                self.grade[pos]["background"] = self.grupos[texto_memoria]
                self.status[pos] = 1
                tamanho_memoria -= 1
        return self.grade

def main():
    raiz = tk.Tk()
    largura = 800
    altura = 600
    raiz.resizable(0, 0)
    raiz.title('Gerenciador de Memória')
    largura_tela = raiz.winfo_screenwidth()
    altura_tela = raiz.winfo_screenheight()
    x = (largura_tela/2) - (largura/2)
    y = (altura_tela/2) - (altura/2)
    raiz.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
    mm = GerenciadorMemoria(raiz)
    quadro_botao = tk.Frame(raiz)
    quadro_botao.pack(side="top", fill="x", pady=20)
    botao_alocar = tk.Button(quadro_botao, text="Alocar", command=mm.alocar, height=5, width=26, bg='gray', borderwidth=0)
    botao_alocar.pack(side="left", padx=5)
    botao_desalocar = tk.Button(quadro_botao, text="Desalocar", command=mm.desalocar, height=5, width=26, bg='gray', borderwidth=0)
    botao_desalocar.pack(side="left", padx=5)
    botao_limpar_processos = tk.Button(quadro_botao, text="Limpar Processos", command=mm.limpar_processos, height= 5, width=26, bg='gray', borderwidth=0)
    botao_limpar_processos.pack(side='left', padx=5)
    botao_realocar = tk.Button(quadro_botao, text="Realocar", command=mm.realocar, height=5, width=26, bg='gray', borderwidth=0)
    botao_realocar.pack(side="left", padx=5)
    raiz.mainloop()

if __name__ == "__main__":
    main()