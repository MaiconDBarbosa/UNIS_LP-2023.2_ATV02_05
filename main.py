def inverter_letras_palavras(frase):
    # Divide a frase em uma lista de palavras
    palavras = frase.split()

    # Inverte as letras de cada palavra
    palavras_invertidas = [palavra[::-1] for palavra in palavras]

    # Junta as palavras de volta em uma frase
    nova_frase = ' '.join(palavras_invertidas)

    return nova_frase

# Solicitar ao usuário que digite uma frase
frase_usuario = input("Digite uma frase: ")

# Chamar a função para inverter as letras das palavras na frase
frase_resultante = inverter_letras_palavras(frase_usuario)

# Exibir a frase original e a frase resultante
print("Frase original:", frase_usuario)
print("Frase com letras invertidas:", frase_resultante)
