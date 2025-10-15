def ocorrencias(lista, valor):
    contador = 0
    
    for elemento in lista:
        if elemento == valor:
            contador +=1
        
    return contador

lista = ["a", "b", "a", "c", "d", "a", "b"]
valor = "a"
resultado = ocorrencias(lista, valor)
print(f"Resultado 2: {resultado}")