import matplotlib.pyplot as plt
import numpy as np

# vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
# meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

vendas_meses = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)


plt.plot(meses, vendas_meses, marker='o', linestyle='-', color='b')
plt.title('Vendas Mensais')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.grid(True)
plt.savefig('vendas_mensais.jpg')
plt.show()
plt.close()

plt.bar(meses, vendas_meses, color='g')
plt.title('Vendas Mensais - Gráfico de Barras')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.grid(axis='y')
plt.savefig('vendas_mensais_barra.jpg')
plt.show()

