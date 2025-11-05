# grafico de barras
import matplotlib.pyplot as plt
produtos = ['Biscoito', 'Refrigerante', 'Sal', 'Acúcar', 'Farinha', 'Café', 'Óleo']
quantidades = [130, 150, 100, 250, 300, 170, 220]
plt.bar(produtos, quantidades, color=['yellow', 'red', 'green', 'lightpink', 'gray', 'lightblue', 'orange'])
plt.title("Estoque de Produtos", fontweight='bold')
plt.xlabel("Produtos", fontweight='bold')
plt.ylabel("Quantidades", fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show() 