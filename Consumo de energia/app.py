#Calculadora de consumo de energia

aparelho=input("digite o nome do seu aparelho: \n")
potencia=float(input("digite a potência (em watts):\n"))
horas_dia=float(input("quantas horas por dia ele é utilizado no dia?:\n"))

#calculo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

#Custo estimado (R$ 0,75 por kWh)
custo=consumo_mensal*0.75

print("\n--- Resultado ---")

print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")



