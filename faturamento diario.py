from statistics import mean
faturamento = [1000 , 2500 , 500 , 1500 , 5000]
maior = 0
menor = 9999
for c in range(len(faturamento)):
    if faturamento[c] > maior:
        maior = faturamento[c]
    if faturamento[c] < menor:
        menor = faturamento[c]

print("O maior faturamento do mês foi {}".format(maior))
print("O menor faturamento do mês foi {}".format(menor))
print("A media de faturamento foi {}".format(mean(faturamento)))

