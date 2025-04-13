import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Определяем наше дифференциальное уравнение

# Задаем начальные условия и временной диапазон
y0 = 0.1  # Начальное значение y
t = np.linspace(0, 5, 100)  # Временной массив от 0 до 5 с 100 шагами

# Решаем модель
y = odeint(model, y0, t)

# Визуализируем результаты
plt.plot(t, y)
plt.title("Решение уравнения y' = y^2 - yt")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.show()