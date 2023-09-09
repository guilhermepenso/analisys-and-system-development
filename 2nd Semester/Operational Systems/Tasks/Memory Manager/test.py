import tkinter as tk

class MemoryManager:
    def __init__(self, master):
        self.master = master
        self.grid = []
        self.selected = []
        self.create_grid()

    def create_grid(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True)
        for i in range(5):
            row = []
            for j in range(30):
                label = tk.Label(frame, bg="white", width=2, height=1, relief="solid", borderwidth=1)
                label.grid(row=i, column=j)
                label.bind("<Button-1>", self.select)
                row.append(label)
            self.grid.append(row)

    def allocate(self, n):
        for i in range(5):
            for j in range(30):
                if self.grid[i][j]['bg'] == "white":
                    for k in range(n):
                        if j+k < 30:
                            self.grid[i][j+k]['bg'] = "blue"
                    return

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
        for i in range(5):
            for j in range(30):
                if self.grid[i][j]['bg'] == "blue":
                    memory_blocks.append((i,j))
                    self.grid[i][j]['bg'] = "white"

        index = 0
        x, y = 0, 0
        for i in range(5):
            for j in range(30):
                if index < len(memory_blocks):
                    if y == 30:
                        x += 1
                        y = 0
                    self.grid[x][y].grid(row=i, column=j)
                    self.grid[x][y]['bg'] = "blue"
                    index += 1
                    y += 1

root = tk.Tk()
mm = MemoryManager(root)

allocate_button = tk.Button(root, text="Alocar", command=lambda: mm.allocate(int(entry.get())))
allocate_button.pack(side="left")

entry = tk.Entry(root)
entry.pack(side="left")

deallocate_button = tk.Button(root, text="Desalocar", command=mm.deallocate)
deallocate_button.pack(side="left")

organize_button = tk.Button(root, text="Organizar", command=mm.organize)
organize_button.pack(side="left")

root.mainloop()