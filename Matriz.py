
matriz = [
    [10, 20, 30],
    [5, 15, 25],
    [35, 45, 55]
]
max_valor=max(max(fila) for fila in matriz)
min_valor=min(min(fila) for fila in matriz)
print("Valor maximo: ", max_valor)
print("valor minimo: ", min_valor)
