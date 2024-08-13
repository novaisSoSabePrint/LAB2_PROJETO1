def cumprimento(texto):
    return f"Olá, {texto}"

print(cumprimento("Gabriel Novais"))


import random

def sorteia_e_calcula_media():
    numeros = [random.randint(1, 100) for _ in range(3)]
    media = sum(numeros) / len(numeros)
    return media

media_numeros = sorteia_e_calcula_media()
print(f"A média dos três números sorteados é: {media_numeros}")