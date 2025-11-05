#grafico de pizza
import matplotlib.pyplot as plt
categorias = ['Eletrônicos', 'Casa e Jardim', 'Alimentos', 'Limpeza', 'Higiene Pessoal']
quantidades = [500, 2000, 2500, 1500, 800] 
precos = [150.00, 15.00, 80.00, 50.00, 50.00]
valores_totais = [qtd * preco for qtd, preco in zip(quantidades, precos)]
cores = ['#4CAF50', '#FFC107', '#FF5722', '#2196F3', '#9C27B0']

plt.figure(figsize=(9, 9)) 

plt.pie(
    valores_totais,        # Os valores que definem o tamanho de cada fatia
    labels=categorias,     # Os rótulos (nomes das categorias)
    autopct='%1.1f%%',     # Formata para mostrar a porcentagem
    colors=cores,          # Aplica as cores definidas
    startangle=90,         
    wedgeprops={'edgecolor': 'black'} 
)
plt.title('Proporção do Valor Total de Estoque por Categoria', fontsize=16, fontweight='bold')
plt.axis('equal') 

plt.show()