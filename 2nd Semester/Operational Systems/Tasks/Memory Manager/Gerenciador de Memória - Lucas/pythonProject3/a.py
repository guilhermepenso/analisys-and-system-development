import tkinter as tk
from tkinter import messagebox
import random
import string
import tkinter.simpledialog
import itertools
from datetime import datetime
import time


def gerador_de_letras():
    tamanho = 1
    while True:
        for s in itertools.product(string.ascii_lowercase, repeat=tamanho):
            yield "".join(s)
        tamanho += 1


class GerenciadorDeMemoria:
    def __init__(self, mestre):
        self.mestre = mestre
        self.grade = []
        self.selecionado = []
        self.grupos = {}
        self.processos = {}
        self.letras = gerador_de_letras()
        self.criar_grade()

    def criar_grade(self):
        quadro = tk.Frame(self.mestre)
        quadro.pack(expand=True)
        for i in range(8):
            linha = []
            for j in range(40):
                rotulo = tk.Label(quadro, bg="white", width=2, height=1, relief="solid", borderwidth=1)
                rotulo.grid(row=i, column=j)
                rotulo.bind("<Button-1>", self.selecionar)
                linha.append(rotulo)
            self.grade.append(linha)

    def alocar(self):
        n = tkinter.simpledialog.askinteger("Entrada", "Quantos processos você gostaria de alocar?")
        blocos_livres = []
        total_livre = 0
        melhor_ajuste = None
        for i in range(8):
            for j in range(40):
                if self.grade[i][j]['bg'] == "white":
                    total_livre += 1
                    blocos_livres.append((i, j))
                else:
                    if len(blocos_livres) >= n:
                        if melhor_ajuste is None or len(melhor_ajuste) > len(blocos_livres):
                            melhor_ajuste = list(blocos_livres)
                    blocos_livres = []
        # Verifica o último bloco de memória livre após o loop
        if len(blocos_livres) >= n:
            if melhor_ajuste is None or len(melhor_ajuste) > len(blocos_livres):
                melhor_ajuste = list(blocos_livres)

        if total_livre < n:
            messagebox.showinfo("Erro", "Não existe espaço disponível!")
            return
        if melhor_ajuste is None:
            messagebox.showinfo("Erro", "Não existe espaço sequencial, favor organize os processos!")
            return

        cor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        id_grupo = next(self.letras)
        for k in range(n):
            self.grade[melhor_ajuste[k][0]][melhor_ajuste[k][1]]['bg'] = cor
            self.grade[melhor_ajuste[k][0]][melhor_ajuste[k][1]]['text'] = id_grupo
        self.grupos[id_grupo] = cor
        self.processos[id_grupo] = {'tamanho': n, 'tempo_alocacao': datetime.now(), 'tempo_desalocacao': None}

    def selecionar(self, evento):
        if evento.widget['text'] != '':
            id_grupo = evento.widget['text']
            cor = self.grupos[id_grupo]
            for i in range(8):
                for j in range(40):
                    if self.grade[i][j]['text'] == id_grupo:
                        if self.grade[i][j]['bg'] == cor:
                            self.grade[i][j]['bg'] = "red"
                            self.selecionado.append(self.grade[i][j])
                        else:
                            self.grade[i][j]['bg'] = cor
                            self.selecionado.remove(self.grade[i][j])

    def desalocar(self):
        for widget in self.selecionado:
            id_grupo = widget['text']
            if id_grupo in self.processos:
                self.processos[id_grupo]['tempo_desalocacao'] = datetime.now()
            widget['bg'] = "white"
            widget['text'] = ''
        self.selecionado = []

    def realocar(self):
        self.desabilitar_interacao()

        blocos_memoria = []

        for i in range(8):
            for j in range(40):
                if self.grade[i][j]['bg'] != "white":
                    blocos_memoria.append((i, j, self.grade[i][j]['text'], self.grade[i][j]['bg']))
                    self.grade[i][j]['bg'] = "white"
                    self.grade[i][j]['text'] = ''

        indice = 0
        x, y = 0, 0

        for i in range(8):
            for j in range(40):
                if indice < len(blocos_memoria):
                    if y == 40:
                        x += 1
                        y = 0
                    self.grade[x][y].grid(row=i, column=j)
                    self.grade[x][y]['bg'] = blocos_memoria[indice][3]
                    self.grade[x][y]['text'] = blocos_memoria[indice][2]
                    indice += 1
                root.update()
                time.sleep(0.04)  # pausa de 0.01 segundo
                y += 1

        self.habilitar_interacao()
        self.salvar_em_arquivo()

    def limpar_memoria(self):
        for i in range(8):
            for j in range(40):
                if self.grade[i][j]['bg'] != "white":
                    self.grade[i][j]['bg'] = "white"
                    self.grade[i][j]['text'] = ''
        self.processos = {}
        self.grupos = {}
        self.selecionado = []

    def desabilitar_interacao(self):
        self.botao_alocar.config(state="disabled")
        self.botao_desalocar.config(state="disabled")
        self.botao_realocar.config(state="disabled")
        self.botao_limpar.config(state="disabled")
        for i in range(8):
            for j in range(40):
                self.grade[i][j].unbind("<Button-1>")

    def habilitar_interacao(self):
        self.botao_alocar.config(state="normal")
        self.botao_desalocar.config(state="normal")
        self.botao_realocar.config(state="normal")
        self.botao_limpar.config(state="normal")
        for i in range(8):
            for j in range(40):
                self.grade[i][j].bind("<Button-1>", self.selecionar)

    def salvar_em_arquivo(self):
        data_str = datetime.now().strftime('%d-%m-%Y')
        with open(f'{data_str}.txt', 'w') as f:
            for id_grupo, info in self.processos.items():
                tempo_alocacao_str = info['tempo_alocacao'].strftime('%H:%M:%S')
                if info['tempo_desalocacao'] is not None:
                    tempo_desalocacao_str = info['tempo_desalocacao'].strftime('%H:%M:%S')
                    duracao_str = str(info['tempo_desalocacao'] - info['tempo_alocacao'])
                else:
                    tempo_desalocacao_str = 'N/A'
                    duracao_str = 'N/A'
                f.write(
                    f'Nome: {id_grupo}, Tamanho: {info["tamanho"]}, Hora de alocação: {tempo_alocacao_str}, Hora de desalocação: {tempo_desalocacao_str}, Duração: {duracao_str}\n')


root = tk.Tk()
root.geometry("800x300")
root.resizable(0, 0)

titulo = tk.Label(root, text="Gerenciador de Memória", font=("Arial", 20))
titulo.pack(pady=10)

mm = GerenciadorDeMemoria(root)

quadro_botoes = tk.Frame(root)
quadro_botoes.pack(side="top", fill="x", pady=20)

mm.botao_alocar = tk.Button(quadro_botoes, text="Alocar", command=mm.alocar, height=2, width=10)
mm.botao_alocar.pack(side="left", padx=10)

mm.botao_desalocar = tk.Button(quadro_botoes, text="Desalocar", command=mm.desalocar, height=2, width=10)
mm.botao_desalocar.pack(side="left", padx=10)

mm.botao_realocar = tk.Button(quadro_botoes, text="Realocar", command=mm.realocar, height=2, width=10)
mm.botao_realocar.pack(side="left", padx=10)

mm.botao_limpar = tk.Button(quadro_botoes, text="Limpar Memória", command=mm.limpar_memoria, height=2, width=15)
mm.botao_limpar.pack(side="left", padx=10)

root.mainloop()
