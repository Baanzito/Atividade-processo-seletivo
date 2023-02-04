#!/usr/bin/env python3

# Tarefa Troféu
# r. anido


corrente = int(input())  # valor de pontos corrente
primeiro = corrente    # primeiro é igual ao primeiro valor da lista
segundo = 0            # inicialmente segundo é zero

trofeus = 1            # número de troféus, inicia com 1 (sempre dá ao menos um troféu)
placas = 0             # número de placas, inicia com -1, um valor menor e diferente dos que serão lidos

# vamos ler outros quatro números
for i in range(4):  
    pontos = int(input())
    if pontos == corrente:         # empate com o último lido
        if pontos == primeiro:
            trofeus += 1           # empate em primeiro, mais um troféu
        elif pontos == segundo:
            placas += 1        # mais uma placa
    elif pontos > segundo:
        segundo = pontos   # primeira vez que o segundo lugar aparece
        placas += 1        # mais uma placa
    corrente = pontos              # novo valor corrente
    
# imprime resultado
print(trofeus,placas)
