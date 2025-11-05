import matplotlib.pyplot as plt
import numpy as np

precos = np.array([50, 120, 300, 80, 20])
estoque = np.array([80, 25, 10, 70, 150])

plt.figure(figsize=(8, 6)) # Define o tamanho da figura
plt.scatter(
    precos,          # Eixo X
    estoque,         # Eixo Y
    color='#2196F3', # Cor dos pontos (azul claro)
    alpha=0.8,       # Transparência
    edgecolors='k',  # Borda dos pontos (preto)
    linewidths=0.5   # Espessura da borda
)

plt.title(
    'Relação entre Preço Unitário e Quantidade em Estoque', 
    fontsize=14, 
    fontweight='bold'
)
plt.xlabel(
    "Preço Unitário (R$)", 
    fontweight='bold', 
    labelpad=15 #espaçamento
)
plt.ylabel(
    "Quantidade em Estoque", 
    fontweight='bold', 
    labelpad=15
)

#adicionar uma grade
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()