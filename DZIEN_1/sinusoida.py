import numpy as np
import matplotlib.pyplot as plt

#przygotowanie danych
t = np.arange(0.0,2.0,0.01)
s = 1+np.sin(2*np.pi*t)

fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas [s]', ylabel='napięcie prądu [mV]',title="Zmiany napięcia prądu w czasie")
ax.grid()
fig.savefig("test.png")
plt.show()
