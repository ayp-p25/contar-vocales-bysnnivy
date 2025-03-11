
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    total_vocales = 0
    a = 0
    
    while a < len(texto):
        if texto[a] in vocales:
            total_vocales += 1
        a += 1
    
    print(f"La frase tiene {total_vocales} vocales")

texto_usuario = input("Ingresa un texto: ")
contar_vocales(texto_usuario)