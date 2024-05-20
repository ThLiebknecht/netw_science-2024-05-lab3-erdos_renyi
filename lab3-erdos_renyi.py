
import networkx as nx

# Заданное количество вершин
n_predef = 12   # predefined
# Заданная вероятность появления связи
p_predef = 0.3  # predefined


# 1. Генерация случайного графа согласно модели Эрдёша-Реньи
G = nx.erdos_renyi_graph(n_predef, p_predef)

# 2. Calculating Average-degree-in-graph-Actual / Вычисление Средняя-степень-вершин-графа-Фактическая:
#        (n-1)*p
a = 0
for n in G.nodes():
    a = a + G.degree(n)  # по Degree/Степень-вершины-графа
d_avr = float(a) / len(G.nodes())

# 3. Calculating Average-degree-in-graph-Analitic / Вычисление Средняя-степень-вершин-графа-Аналитическая:
d_analitic = float(n_predef-1) * float(p_predef)

# 4. Difference between Average-degree-in-graph-Actual and *-Analitic
#    Разница между Средняя-степень-вершин-графа-Фактическая и *-Аналитическая
d_diff = round(d_analitic - d_avr, 4)

# 4. Вывод результатов
print("     Средняя-степень-вершин-графа-Фактическая: ", round(d_avr,4) )
print("   Средняя-степень-вершин-графа-Аналитическая: ", d_analitic )
print("Разница между *-Аналитическая и *-Фактическая: ", d_diff )

