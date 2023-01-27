#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 07:22:04 2021

@author: julianeduardogomezchavarro
"""

cadena="leomessi"
cadena2=""

nueva=cadena
i=0
a=True
while i<len(cadena) and a==True:
    minimo=min(nueva)
    todo=cadena.count(minimo)
    cadena2+=(minimo*todo)
    nueva=nueva.replace(minimo,"")
    if len(nueva)==0:
        a=False
        
    i+=1
    
print(cadena2)



dic=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
a="0xa4e8bba10d8a3e774b99ce4019726e6a61966c1a01a67f3427326d2091e11ba3"
b="0x8f5fc1b505d77a04bd2608fff9884ac3ebd87f20"
h="0x169332ae7d143e4b5c6baedb2fef77bfbddb4011"
v="0.0"
r="transaccion"
e="5317"
s="25160"
c=a+b+h+v+r+e+s
f=""
g="1446156278"
for i in c:
    if i in dic:
        f+=str(ord(i))
    else:
        f+=i

d=int(f)%int(g)
print(d)