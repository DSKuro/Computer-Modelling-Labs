import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14,
     15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29]
y = [21.572, 21.710, 21.715, 21.598, 21.808, 21.890, 21.677,
     21.306, 20.810, 20.875, 20.670, 20.961, 20.959, 20.766,
     21.238, 21.277, 20.984, 20.054, 20.005, 20.025, 20.375,
     20.715, 21.793, 21.929, 22.073]

numpy_x = np.array(x)
numpy_y = np.array(y)

def set_trend(trend, label, arg):
     plt.plot(arg, trend, linestyle='dashed', color="orange", label = label)

def create_subplot(nrows, ncol, index, arg, trend, label):
     plt.subplot(nrows, ncol, index)
     plt.scatter(numpy_x, numpy_y, label = 'data')
     set_trend(trend, label, arg)
     plt.grid(color="gainsboro")
     plt.legend(loc='upper right', fontsize=8)

def create_graphics():
     set_line_by_data = np.polyfit(numpy_x, numpy_y, 1)
     linear_trend = np.poly1d(set_line_by_data)
     print("{0}x + {1}".format(*set_line_by_data))

     set_polinom_by_data2 = np.polyfit(numpy_x, numpy_y, 2)
     polinom_trend2 = np.poly1d(set_polinom_by_data2)
     linspace_x2 = np.linspace(numpy_x.min(), numpy_x.max())
     print("${0}x^2 + {1}x + {2}$".format(*set_polinom_by_data2))

     set_polinom_by_data4 = np.polyfit(numpy_x, numpy_y, 4)
     polinom_trend4 = np.poly1d(set_polinom_by_data4)
     linspace_x4 = np.linspace(numpy_x.min(), numpy_x.max())
     print("${0}x^4 + {1}x^3 + {2}x^2 + {3}x + {4}$".format(*set_polinom_by_data4))

     set_polinom_by_data = np.polyfit(numpy_x, numpy_y, 6)
     polinom_trend = np.poly1d(set_polinom_by_data)
     linspace_x = np.linspace(numpy_x.min(), numpy_x.max())
     print("${0}x^6 + {1}x^5 + {2}x^4 + {3}x^3 + {4}x^2 + {5}x + {6}$".format(*set_polinom_by_data))

     # логарифмический
     set_log_by_data = np.polyfit(np.log(numpy_x), numpy_y, 1)  # работа с полиномом 1 степени + логарифмирование x
     log_trend = [set_log_by_data[0] * np.log(x) + set_log_by_data[1] for x in
                  numpy_x]  # создание одномерного массива для логарифмического тренда
     print("${0}ln(x) + {1}$".format(*set_log_by_data))  # формула

     set_exp_by_data = np.polyfit(numpy_x, np.log(numpy_y), 1)
     exp_trend = [np.exp(set_exp_by_data[1]) * np.exp(set_exp_by_data[0] * x) for x in numpy_x]
     print("${1}e^{0}x$".format(*set_exp_by_data))

     linear_r2 = r2_score(numpy_y, linear_trend(numpy_x))
     polinom_r2 = r2_score(numpy_y, polinom_trend(numpy_x))
     polinom4_r2 = r2_score(numpy_y, polinom_trend4(numpy_x))
     polinom2_r2 = r2_score(numpy_y, polinom_trend2(numpy_x))
     log_r2 = r2_score(numpy_y, log_trend)
     exp_r2 = r2_score(numpy_y, exp_trend)

     plt.figure(figsize=(15, 15))

     plt.subplot(3, 2, 1)

     create_subplot(3, 2, 1, numpy_x, linear_trend(numpy_x), 'linear trend')
     plt.title("Линейный \n$R^2=$" + str(linear_r2) + "\n{0}x + {1}".format(*set_line_by_data))

     create_subplot(3, 2, 2, linspace_x, polinom_trend2(linspace_x2), "")
     plt.title("Полиномиальный 2 \n$R^2=$" + str(polinom2_r2) + "${0}x^2 + {1}x$ + \n${2}$".format(*set_polinom_by_data2))

     create_subplot(3, 2, 3, linspace_x, polinom_trend4(linspace_x4), "")
     plt.title("Полиномиальный 4 \n$R^2=$" + str(polinom4_r2) + "${0}x^4 + {1}x^3$ + \n${2}x^2 + {3}x$ + \n${4}$".format(
          *set_polinom_by_data4))

     create_subplot(3, 2, 4, linspace_x, polinom_trend(linspace_x), "")
     plt.title("Полиномиальный \n$R^2=$" + str(
          polinom_r2) + "\n${0}x^6 + {1}x^5$ + \n${2}x^4 + {3}x^3$ + \n${4}x^2 + {5}x$ + \n${6}$".format(
          *set_polinom_by_data))

     create_subplot(3, 2, 5, numpy_x, log_trend, 'log_trend')
     plt.title("Логарифмический \n$R^2=$" + str(log_r2) + "\n${0}ln(x) + {1}$".format(*set_log_by_data))

     create_subplot(3, 2, 6, numpy_x, exp_trend, "")
     plt.title("Экспоненциальный \n$R^2=$" + str(exp_r2) + "\n$12,677e^{-106x}$")

     fig = plt.gcf()
     fig.set_size_inches(15, 15)
     fig.tight_layout(pad=10.0)

     plt.show()