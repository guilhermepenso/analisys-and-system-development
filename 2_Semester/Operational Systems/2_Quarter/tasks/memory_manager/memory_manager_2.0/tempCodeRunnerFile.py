
            if self.status[pos] == 0 and tamanho_memoria > 0:
                self.grade[pos]["text"] = texto_memoria
                self.grade[pos]["background"] = self.grupos[texto_memoria]
                self.status[pos] = 1
                tamanho_memoria -= 1
        return self.grade