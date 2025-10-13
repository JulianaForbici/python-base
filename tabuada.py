#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

Tabuada do 1
1
2
3
...
------------
Tabuada do 2
2
4
---
------------
"""
__version__ = "0.1.0"
__author__ = "Juliana"

template = """

---Tabuada do 2---

##################
"""


numeros = list(range(1, 11))
for n1 in numeros:
    print(f"{'-'*10} Tabuada do {n1} {'-'*10}")
    for n2 in numeros:
        resultado = n1 * n2
        print(f"{n1} x {n2} = {resultado}")
    print() 
