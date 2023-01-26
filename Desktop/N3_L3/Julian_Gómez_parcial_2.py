#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 06:47:04 2021

@author: julianeduardogomezchavarro
"""

def crear_sector( nombre: str, carriles: int, pendiente: float, 
                   ancho_calzada: float, ancho_berma: float, separador: bool,
                   peatones: bool, control_accesos: str, 
                   zona_recreacional: bool,cuello_de_botella: bool, 
                   zona_escolar: bool ) -> dict:
    
    dic_sector={"nombre_sector":nombre, 
                "carriles":carriles,
                "pendiente":pendiente,
                "ancho_calzada":ancho_calzada,
                "ancho_berma":ancho_berma,
                "separador":separador,
                "concentracion_peatones":peatones,
                "control_accesos":control_accesos,
                "zona_recreacional":zona_recreacional,
                "cuello_de_botella":cuello_de_botella,
                "zona_escolar":zona_escolar}
    return dic_sector

sector1 = crear_sector("Melquíades", 4, 0.03, 7.3, 2.5,True, False,
                               "Total",False, False, False)
sector2 = crear_sector("Remedios", 4, 0.05, 7.3, 1.5, True, False,
                               "Parcial", False, True, True)
sector3 = crear_sector("Crespi", 3, 0.045, 7.3, 1.5, False, False,
                               "Nulo", True, True, False)
sector4 = crear_sector("Buendía", 2, 0.06, 7.3, 1.8, False, True,
                               "Nulo", True, True, False)
def clasificar_sector( sector: dict ) -> str:
    
    carac= ""
    if sector["pendiente"]<=0.05 and sector["ancho_calzada"]==7.30 and sector["ancho_berma"]==2.50 and sector["carriles"]>2:
        carac="A1"
    elif sector["pendiente"]<=0.06 and sector["ancho_calzada"]==7.30 and sector["ancho_berma"]==1.50 and sector["carriles"]>2:
        carac="B1"
    elif sector["pendiente"]<=0.08 and sector["ancho_calzada"]==7.00 and sector["ancho_berma"]==1.30 and sector["carriles"]>2:
        carac="C1"
    elif sector["pendiente"]<=0.06 and sector["ancho_calzada"]==7.30 and sector["ancho_berma"]==1.80 and sector["carriles"]==2:
        carac="A2"
    elif sector["pendiente"]<=0.08 and sector["ancho_calzada"]==7.30 and sector["ancho_berma"]==1.00 and sector["carriles"]==2:
        carac="B2"
    elif sector["pendiente"]<=0.09 and sector["ancho_calzada"]==7.00 and sector["ancho_berma"]==0.50 and sector["carriles"]==2:
        carac="C2"
    elif sector["pendiente"]<=0.09 and sector["ancho_calzada"]==7.00 and sector["ancho_berma"]==0.40 and sector["carriles"]==2:
        carac="D2"
        
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return carac

def determinar_velocidad_generica( sector: dict ) -> int:
   
    clasificar=clasificar_sector(sector)
    vel=0
    if sector["carriles"]>2 and clasificar=="A1" and sector["control_accesos"]=="Total" and sector["concentracion_peatones"]==False and sector["separador"]==True:
        vel= 120
    if sector["carriles"]>2 and clasificar=="B1" and sector["control_accesos"]=="Parcial" and sector["concentracion_peatones"]==False and sector["separador"]==True:
        vel= 100
    elif sector["carriles"]>2 and clasificar=="B1" and sector["control_accesos"]=="Parcial" and sector["concentracion_peatones"]==False and sector["separador"]==False:
        vel= 90
    if sector["carriles"]>2 and clasificar=="B1" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==False and sector["separador"]==True:
        vel= 90
    elif sector["carriles"]>2 and clasificar=="B1" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==False and sector["separador"]==False:
        vel= 80
    if sector["carriles"]>2 and clasificar=="C1" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==False and sector["separador"]==True:
        vel= 80
    elif sector["carriles"]>2 and clasificar=="C1" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==False and sector["separador"]==False:
        vel= 70
    if sector["carriles"]>2 and clasificar=="C1" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==True and sector["separador"]==True:
        vel= 70
    elif sector["carriles"]>2 and clasificar=="C1" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==True and sector["separador"]==False:
        vel= 60
    if sector["carriles"]==2 and clasificar=="A2" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==False:
        vel= 80
    elif sector["carriles"]==2 and clasificar=="A2" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==True:
        vel=70
    if sector["carriles"]==2 and clasificar=="B2" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==False:
        vel= 70
    elif sector["carriles"]==2 and clasificar=="B2" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==True:
        vel= 60
    if sector["carriles"]==2 and clasificar=="C2" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==True:
        vel= 50
    if sector["carriles"]==2 and clasificar=="D2" and sector["control_accesos"]=="Nulo" and sector["concentracion_peatones"]==True:
        vel= 40
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return vel

def sectores_pacificos(s1:dict, s2:dict, s3:dict, s4:dict)->dict:
    dic_pas=None
    dic_tar={}
    if s1["zona_escolar"]==False and s1["zona_recreacional"]==True:
        dic_tar[s1["nombre_sector"]]=s1["pendiente"]
        dic_pas=dic_tar
    if s2["zona_escolar"]==False and s2["zona_recreacional"]==True:
        dic_tar[s2["nombre_sector"]]=s2["pendiente"]
        dic_pas=dic_tar
    if s3["zona_escolar"]==False and s3["zona_recreacional"]==True:
        dic_tar[s3["nombre_sector"]]=s3["pendiente"]
        dic_pas=dic_tar
    if s4["zona_escolar"]==False and s4["zona_recreacional"]==True:
        dic_tar[s4["nombre_sector"]]=s4["pendiente"]
        dic_pas=dic_tar
        
    return dic_pas


def ingresar_lecturas(s1:dict, s2:dict, s3:dict, s4:dict, nombre:str)->str:
    num=0
    nom=False
    velocidad= determinar_velocidad_generica(s1)
    velocidad_2= determinar_velocidad_generica(s2)
    velocidad_3= determinar_velocidad_generica(s3)
    velocidad_4= determinar_velocidad_generica(s4)
    if s1["nombre_sector"]==nombre and velocidad>=0 and velocidad<=50:
        num=40
        s1["numero_lecturas"]=num
        nom=True
    elif s1["nombre_sector"]==nombre and velocidad>=51 and velocidad<=80:
        num=60
        s1["numero_lecturas"]=num
        nom=True
    elif s1["nombre_sector"]==nombre and velocidad>=81:
        num=80
        s1["numero_lecturas"]=num
        nom=True
    if s2["nombre_sector"]==nombre and velocidad_2>=0 and velocidad_2<=50:
        num=40
        s2["numero_lecturas"]=num
        nom=True
    elif s2["nombre_sector"]==nombre and velocidad_2>=51 and velocidad_2<=80:
        num=60
        s2["numero_lecturas"]=num
        nom=True
    elif s2["nombre_sector"]==nombre and velocidad_2>=81:
        num=80
        s2["numero_lecturas"]=num
        nom=True
    if s3["nombre_sector"]==nombre and velocidad_3>=0 and velocidad_3<=50:
        num=40
        s3["numero_lecturas"]=num
        nom=True
    elif s3["nombre_sector"]==nombre and velocidad_3>=51 and velocidad_3<=80:
        num=60
        s3["numero_lecturas"]=num
        nom=True
    elif s3["nombre_sector"]==nombre and velocidad_3>=81:
        num=80
        s3["numero_lecturas"]=num
        nom=True
    if s4["nombre_sector"]==nombre and velocidad_4>=0 and velocidad_4<=50:
        num=40
        s4["numero_lecturas"]=num
        nom=True
    elif s4["nombre_sector"]==nombre and velocidad_4>=51 and velocidad_4<=80:
        num=60
        s4["numero_lecturas"]=num
        nom=True
    elif s4["nombre_sector"]==nombre and velocidad_4>=81:
        num=80
        s4["numero_lecturas"]=num
        nom=True
    if nom==True:
        total="El sector "+nombre+" fue actualizado con el radio "+str(num)
    elif nom==False:
        total="El sector no esxiste"
    return total



   
        
        












