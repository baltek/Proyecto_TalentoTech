import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,0.1)
y=np.sin(x)
"""
for datos in x:
    y.append(datos**2)
    print(y)
"""



plt.plot(x, y,color='black', label='gráfica 1')
plt.grid()
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráficas")
plt.legend()
plt.show()    
