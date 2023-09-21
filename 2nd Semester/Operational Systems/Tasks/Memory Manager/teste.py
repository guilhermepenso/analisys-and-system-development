from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
        
    def tela(self):
        self.root.title("Gerenciador de Memória")
        self.root.configure(background= 'lightgray')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.wm_maxsize(1280, 1080)
        self.root.wm_minsize(720, 480)


Application()