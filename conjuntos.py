#O conjunto não aceita elementos repetidos, sua declaração é igual do dict porém não tem precisa de chave, somente os valores
cores = {"azul", "vermelho", "amarelo"}

cores.add("preto")

print(cores)

cores.remove("amarelo")

print(cores)