#Sets e a teoria dos conjuntos! 

# Os sets podem ser criados a partir de qualquer objeto iterável
iteravel = [1, 2, 3]  # list
iteravel = 1, 2, 3  # tuple
iteravel = "Banana"  # str

# usando a classe
set(iteravel)

# usando literais com { e }
{1, 2, 3, 4}

# desempacotando tuplas, listas ou textos
{*iteravel}

>>> conjunto_a = [1, 2, 3, 4, 5]
>>> conjunto_b = [4, 5, 6, 7, 8]

# | para união
>>> set(conjunto_a) | set(conjunto_b)
{1, 2, 3, 4, 5, 6, 7, 8}

# & para intersecção
>>> set(conjunto_a) & set(conjunto_b)
{4, 5}

# – para diferença
>>>  set(conjunto_a) - set(conjunto_b)
{1, 2, 3}

# para ^ diferença simétrica
>>> set(conjunto_a) ^ set(conjunto_b)
{1, 2, 3, 6, 7, 8}
