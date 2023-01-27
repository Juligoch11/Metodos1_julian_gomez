#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:42:02 2021

@author: julianeduardogomezchavarro
"""
def crear_hash (sumaASCII: int, timestamp: int) -> int:
    total= sumaASCII % timestamp
    return total

def cargar_blockchain_cupicoin(nombre_archivo:str)->list:
    transaccion=[]
    d=[]
    suma=0
    hash_anterior=None
    i=0
    c=0
    f=0
    abierto=False
    archivo=open(nombre_archivo,"r")
    titulos=archivo.readline()
    print(titulos)
    linea=archivo.readline()
    while len(linea)>0:
        datos = linea.split(",")
        total=""
        numero=datos[1]
        if datos[1] not in d:
           tra={}
           tra["numero bloque"]=datos[1]
           tra["timestamp"]=datos[5]
           tra["hash_anterior"]=hash_anterior
           suma=0
           f=0
           
        else:
            transaccion.remove(transaccion[i])
            suma+=1


        d.append(datos[1])
        n=int(datos[1])
        if n != c:
            i+=1
            c=int(datos[1])
        can=d.count(datos[1])
        tra["cantidad_transacciones"]=can
        tra["abierto"]=abierto
        time=int(tra["timestamp"])
        codigo1= suma
        trans={}
        trans["codigo"] =  datos[0]
        trans["remitente"] =  datos[2]
        trans["destinatario"] =  datos[3]
        trans["valor"] =  datos[4]
        if trans["destinatario"]=="":
            tipo="contrato"
        else: 
            tipo="transferencia"
        trans["operación"] = tipo
        tra[codigo1]=trans
        transaccion.append(tra)
        if can==1 and tra["hash_anterior"]!=None:
           total+=trans["codigo"]+trans["remitente"]+trans["destinatario"]+trans["valor"]+trans["operación"]+tra["numero bloque"]+str(tra["hash_anterior"])
        elif can==1 and tra["hash_anterior"]==None:
             total+=trans["codigo"]+trans["remitente"]+trans["destinatario"]+trans["valor"]+trans["operación"]+tra["numero bloque"]
        else: 
            total+=trans["codigo"]+trans["remitente"]+trans["destinatario"]+trans["valor"]+trans["operación"]

        for z in total:
            f+=ord(z)
        resultado= crear_hash(f,time)
        tra["hash"]=str(resultado)
        hash_anterior=tra["hash"]
        
        linea =  archivo.readline()
        
    tras={}
    tras["numero bloque"]=int(numero)+1
    tras["timestamp"]=None
    tras["hash_anterior"]=hash_anterior
    tras["hash"]=None
    abierto=True
    tras["abierto"]=abierto
    tras["cantidad_transacciones"]=0
    transaccion.append(tras)
    archivo.close()
    return transaccion


def agregar_transaccion(transaccion:list, trans:dict)->None:
    ultima=len(transaccion)-1
    nuevo=transaccion[ultima]
    total=nuevo["cantidad_transacciones"]
    nuevo[total]=trans
    total+=1
    nuevo["cantidad_transacciones"]=total

def agregar_nuevo_bloque(transaccion:list,timestamp:str)->None:
    for nuevo in transaccion:
        num=nuevo["numero bloque"]
        ha_ant=nuevo["hash_anterior"]
        ha=nuevo["hash"]
        can=nuevo["cantidad_transacciones"]
        ab=nuevo["abierto"]
        for i in nuevo:
           b=type(i)
           if b == int:
              dict2=nuevo[i]
              if ha!=None and timestamp!=None:
                tra={}
                tra["numero bloque"]=num
                tra["timestamp"]=timestamp
                tra["hash_anterior"]=ha_ant
                tra["hash"]=ha
                tra["cantidad_transacciones"]=can
                tra["abierto"]=ab
                tra[i]=dict2
                transaccion.append(tra)
              else:
                tras={}
                tras["numero bloque"]=num+1
                tras["timestamp"]=None
                tras["hash_anterior"]=ha_ant
                tras["hash"]=None
                abierto=True
                tras["abierto"]=abierto
                tras["cantidad_transacciones"]=0
                transaccion.append(tra)
        
def contar_veces_aparece_cuenta(transaccion:list,direccion_cuenta:str )->dict:
    c=0
    d=0
    dic={}
    for nuevo in transaccion:
        for i in nuevo:
            b=type(i)
            if b == int:
               dict2=nuevo[i]
               remi=dict2["remitente"]
               desti=dict2["destinatario"]
               if remi==direccion_cuenta:
                     d+=1
               elif desti==direccion_cuenta:
                     c+=1
    dic["remitente"]=d
    dic["destinatario"]=c
    total=dic
    return total

                
def buscar_transaccion (transaccion:list,codigo_transaccion:str)->dict:
    todo=None
    for nuevo in transaccion:
       for i in nuevo:
           b=type(i)
           if b == int:
              dict2=nuevo[i]
              cod=dict2["codigo"]
              if cod==codigo_transaccion:
                  todo=nuevo[i]
    return todo

def dar_transacciones_entre (transaccion:list, remitente:str,destinatario:str)->list: 
    nueva=[]
    for nuevo in transaccion:
       for i in nuevo:
           b=type(i)
           if b == int:
              dict2=nuevo[i]
              remi=dict2["remitente"]
              desti=dict2["destinatario"]
              if remi==remitente and desti==destinatario:
                  nueva.append(nuevo[i])
    return nueva
             
 
                
def dar_transferencia_mayor_valor(transaccion:list)->dict:
    suma=0
    dic={}
    for nuevo in transaccion:
       for i in nuevo:
           b=type(i)
           if b == int:
              dict2=nuevo[i]
              va=float(dict2["valor"])
              if va>suma:
                  suma=va
                  dic=dict2
    return dic

       
def calcular_saldo_cuenta (transaccion:list,direccion_cuenta:str)->int:
    saldo=0
    for nuevo in transaccion:
       for i in nuevo:
           b=type(i)
           if b == int:
              dict2=nuevo[i]
              remi=dict2["remitente"]
              desti=dict2["destinatario"]  
              va=float(dict2["valor"])
              if remi==direccion_cuenta:
                  saldo=saldo-va
              if desti==direccion_cuenta:
                  saldo=saldo+va
                
    return saldo         

def validar_bloque(transaccion:list)->bool:
    final=False
    mas=False
    ultimo=len(transaccion)-1
    todo=transaccion[ultimo]
    contador=0
    nada=0
    d=[]
    suma=0
    if todo["abierto"]==True:
        mas=True
    for nuevo in transaccion:
        a=nuevo["abierto"]
        if a== True:
           contador+=1
    for nuevo in range(1,len(transaccion)):
        b1=transaccion[nuevo]
        b2=transaccion[nuevo-1]
        b3=b1["hash_anterior"]
        b4=b2["hash"]
        if b3==b4:
            nada+=1

    for nuevo in transaccion:

        num=nuevo["numero bloque"]
        if num not in d:
            f=0
        ha_ant=nuevo["hash_anterior"]
        time=nuevo["timestamp"]
        ha=nuevo["hash"]
        if time!=None:
           time2=int(time)
        else:
            resul=None
            if resul==ha:
                 suma+=1
        for i in nuevo:
           b=type(i)
           if b == int:
              total=""
              d.append(num)
              can=d.count(num)
              dict2=nuevo[i]
              cod=dict2["codigo"]
              remi=dict2["remitente"]
              desti=dict2["destinatario"]  
              va=dict2["valor"]
              ope=dict2["operación"]
              if can==1 and ha_ant!=None:
                 total+=cod+remi+desti+va+ope+num+str(ha_ant)
              elif can==1 and ha_ant==None:
                 total+=cod+remi+desti+va+ope+num
              else: 
                 total+=cod+remi+desti+va+ope
              for z in total:
                 f+=ord(z)
              resultado= crear_hash(f,time2)
              resul=str(resultado)
              if resul==ha:
                 suma+=1
    if mas==True and contador==1 and nada==len(transaccion)-1 and suma==len(transaccion):
          final=True
    return final



