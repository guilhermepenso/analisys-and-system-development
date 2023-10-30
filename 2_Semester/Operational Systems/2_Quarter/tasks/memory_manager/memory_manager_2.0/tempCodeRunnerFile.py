def reallocate(self):
        block_groups = []
        memory_blocks = []
        actual_group = ""
        previous_memory_block = 0

        # Procura dentro da grid dos processos
        for i in range(10):
            for j in range(10):
                
                # Verificação de processos que estão ocupados
                if self.status[(i,j)] != 0 and previous_memory_block == 0:
                    actual_group = self.grid[i][j]["text"]
                while actual_group == self.grid[i][j]["text"]:
                    block_groups.append((i, j, self.grid[i][j]["text"], self.grid[i][j]["background"], self.status[(i,j)]))           
                        
                    # Salva os processos ocupadas no memory_blocks 
                    memory_blocks.append((block_groups))
                    
                    # Altera os dados atuais para não ocupados visualmente
                    self.grid[i][j]['background'] = "white"
                    self.grid[i][j]['text'] = ""
                    self.status[(i,j)] = 0
                block_groups = []
            previous_memory_block = self.status[(i,j)]
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
                    self.grid[x][y]['text'] = memory_blocks[index][0][2]
                    self.grid[x][y]['background'] = memory_blocks[index][0][3]
                    self.status[(i,j)] = memory_blocks[index][0][4]
                    # Aumenta o index para verificar o if 
                    index += 1
                    
                # Root atualiza a tela
                root.update()
                
                # Timer visual para realocação lenta
                time.sleep(0.05)
                y += 1