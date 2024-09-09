def verificar_letra_a(string):
    contador = string.lower().count('a')
    return contador

texto = "A rápida raposa marrom salta sobre o cachorro preguiçoso."
quantidade = verificar_letra_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
