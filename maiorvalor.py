def maiorvalor(lista):
    if not lista:
        return None
    
    maiorvalor = lista[0]
    
    for numero in lista:
        if numero > maiorvalor:
            maiorvalor = numero
    return maiorvalor
        
entrada = [14, 7, 92, 1, 55]
resultado = maiorvalor(entrada)
print(f"Resultado 3: {resultado}")