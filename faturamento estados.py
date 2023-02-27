faturamento_estados = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

faturamento_total = sum(faturamento_estados.values())

for estado in faturamento_estados:
    percentual = (faturamento_estados[estado] / faturamento_total) * 100
    print("{}: {:.2f}%".format(estado,percentual))