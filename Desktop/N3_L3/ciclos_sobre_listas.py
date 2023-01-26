#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 06:47:09 2021

@author: julianeduardogomezchavarro
"""

def unir_listas(lista1: list, lista2: list, lista3:list)->str:

    nueva_cadena=""

    for i in range(0,len(lista1)):
          nueva_cadena+= (lista1[i]+" "+ lista2[i]+" "+lista3[i]+" ")
          cadena=nueva_cadena.rstrip()
          
    return cadena
print(unir_listas(["a","d"], ["b","e"], ["c","f"]))
def palabras_intercaladas(cadena1: str, cadena2: str, cadena3:str)->str:
    
    nueva=""
    p=0
    e=0
    i=0
    while i<len(cadena1):
        if e>=len(cadena3):
           break
        elif cadena1[i]==cadena3[e]:
             e+=1
             p=i
             nueva+=cadena2[p]
             i=0
        elif cadena3[e] not in cadena1:
             nueva+=cadena3[e]
             e+=1
             i=0
        else:
             i+=1
    return nueva

print(palabras_intercaladas("abcde", "fghij", "ceda"))
    
        
        