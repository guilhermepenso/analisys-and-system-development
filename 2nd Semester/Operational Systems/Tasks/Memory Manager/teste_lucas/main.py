# Gerador de poemas sobre programas em Python
import random

# Lista de adjetivos
adjetivos = ["simples", "eficiente", "elegante", "criativo", "dinâmico", "interativo"]

# Lista de substantivos
substantivos = ["programa", "código", "algoritmo", "função", "módulo", "projeto"]

# Lista de verbos
verbos = ["criar", "resolver", "calcular", "executar", "salvar", "apresentar"]

# Escolher palavras aleatórias das listas
adj1 = random.choice(adjetivos)
adj2 = random.choice(adjetivos)
sub1 = random.choice(substantivos)
sub2 = random.choice(substantivos)
ver1 = random.choice(verbos)
ver2 = random.choice(verbos)

# Montar o poema
poema = f"Eu fiz um {sub1} em Python\n"
poema += f"Que é muito {adj1} e {adj2}\n"
poema += f"Ele pode {ver1} um problema\n"
poema += f"E {ver2} as informações\n"
poema += f"Eu usei várias {sub2}s\n"
poema += f"Para organizar meu código\n"
poema += f"Agora vou mostrar para vocês\n"
poema += f"O resultado do meu trabalho"

# Imprimir o poema
print(poema)
