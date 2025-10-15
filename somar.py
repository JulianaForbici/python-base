def somar(lista): 
    somarpares = 0
    
    for numero in lista:
        if numero % 2 == 0:
            somarpares += numero
    return somarpares

entrada = [1, 5, 8, 10, 3, 4]
resultado = somar(entrada)
print(f"Resultado 1: {resultado}")