# gráfico de linhas
import matplotlib.pyplot as plt
dias = [1, 2, 3, 4, 5, 6, 7]
estoque = [100, 70, 110, 90, 75, 60, 95]
plt.plot(dias, estoque)
plt.title("Movimentação do Estoque de Biscoito de Chocolate")
plt.xlabel("Dias")
plt.ylabel("Estoque")
plt.show()