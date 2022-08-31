"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""

from operator import itemgetter
import datetime
import itertools


def file_clean():
    tup_lst=[]
    with open('data.csv') as file:
        for line in file:
            line=line.replace(chr(32),'')
            line=line.replace('\n','')
            tupla = tuple(list(line.split('\t')))
            tup_lst.append(tupla)
            
    return tup_lst


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    tup_lst=file_clean()
    counter=0
    for i in range(0,len(tup_lst)):
        counter+=int(tup_lst[i][1])
    
    return counter  


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    tup_lst=file_clean()
    freq={}
    lista=[]
    for t in range(0,len(tup_lst)):
        e=tup_lst[t][0]
        lista.append(e)
    for i in lista:
        freq[i]=freq.setdefault(i, 0) + 1
    rta=sorted(list(freq.items()),key=itemgetter(0))
    return rta


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    tup_lst=file_clean()
    lista=[]
    counter = {}
    for t in range(0,len(tup_lst)):
        tupla_temp=(tup_lst[t][0],int(tup_lst[t][1]))
        lista.append(tupla_temp)
        
    for key, value in lista:
        if key in counter:
            counter[key] += value
        else:
            counter[key] = value
    rta=sorted([(key, counter[key]) for key in counter],key=itemgetter(0))
    return rta  


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    tup_lst=file_clean()
    lista=[]
    for i in range(0,len(tup_lst)):
        e=tup_lst[i][2]
        try:
            e=datetime.datetime.strptime(e,'%Y-%m-%d')
            e=str(datetime.datetime.strftime(e,'%m'))
            lista.append(e)
        except:
            # Error en fecha. Febrero de 1999 no era bisiesto, solo tenía 28 días
            e=str(e[5:7])
            lista.append(e)
    
    freq={}
    for i in lista:
        freq[i]=freq.setdefault(i, 0) + 1
    rta=sorted(list(freq.items()),key=itemgetter(0))
            
    return rta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    tup_lst=file_clean()
    lista=[]
    lista_rta=[]
    for t in range(0,len(tup_lst)):
        e1=tup_lst[t][0]
        e2=int(tup_lst[t][1])
        t=(e1,e2)
        lista.append(t)
    lista=sorted(lista,key=itemgetter(0))
    
    key_func=lambda x: x[0]
    for key,group in itertools.groupby(lista,key_func):
        min=100
        max=0
        group=list(group)
        for k in group:
            if min>k[1]:
                min=k[1]
            if max<k[1]:
                max=k[1]
        h=(key,max,min)
        lista_rta.append(h)
    return lista_rta


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    tup_lst=file_clean()
    lista=[]
    lista2=[]
    lista_rta=[]
    
    for t in range(0,len(tup_lst)):
        e1=list(str((tup_lst[t][4])).split(','))
        e1=tuple(e1)
        lista.append(e1)
    
    for r in lista:
        f=None
        for g in r:
            z1=g[:3]
            z2=int(g[4:])
            f=(z1,z2)
            lista2.append(f)
        
    lista2=sorted(lista2,key=itemgetter(0))
    key_func=lambda x: x[0]
    
    for key,group in itertools.groupby(lista2,key_func):
        min=100
        max=-100
        group=list(group)
        for k in group:
            if min>k[1]:
                min=k[1]
            if max<k[1]:
                max=k[1]
        h=(key,min,max)
        lista_rta.append(h)
    return lista_rta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    tup_lst=file_clean()
    lista=[]
    ind=[]
    lista_rta=[]
    
    for t in range(0,len(tup_lst)):
        e1=int(tup_lst[t][1])
        e2=tup_lst[t][0]
        ind.append(e1)    
        u=(e1,e2)
        lista.append(u)
    
    ind=set(ind)

    for j in ind:
        letters=None
        letters=[]
        rta=None 
        for k in lista:
            if k[0]==j:
                letters.append(k[1])
        rta=(j,letters)        
        lista_rta.append(rta)       
    return lista_rta     


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    tup_lst=file_clean()
    lista=[]
    ind=[]
    lista_rta=[]
    
    for t in range(0,len(tup_lst)):
        e1=int(tup_lst[t][1])
        e2=tup_lst[t][0]
        ind.append(e1)    
        u=(e1,e2)
        lista.append(u)
    
    ind=set(ind)

    for j in ind:
        letters=None
        letters=[]
        rta=None 
        for k in lista:
            if k[0]==j:
                letters.append(k[1])
        letters=sorted(list(set(letters)),reverse=False)
        rta=(j,letters)        
        lista_rta.append(rta)       
    return lista_rta  


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    tup_lst=file_clean()
    lista=[]
    letters=[]    
    for t in range(0,len(tup_lst)):
        e1=list(str((tup_lst[t][4])).split(','))
        e1=tuple(e1)
        lista.append(e1)
    
    for r in lista:
        for g in r:
            z1=g[:3]
            letters.append(z1)
    
    ind=set(letters)
    rta=[]
    for j in ind:
        cnt=0
        for k in letters:
            if k==j:
                cnt+=1
        e=(j,cnt)        
        rta.append(e)
    rta=sorted(rta,key=itemgetter(0))          
    
    counter = {}
    for y in rta:
        counter[y[0]]=y[1]
    
    return counter


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    tup_lst=file_clean()
    lista=[]
    for t in range(0,len(tup_lst)):
        e1=tup_lst[t][0]
        e2=len(list(str((tup_lst[t][3])).split(',')))
        e3=tup_lst[t][4]
        e3=e3.count(',')+1
        f=(e1,e2,e3)
        lista.append(f)

    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    voll_liste=[]
    tup_lst=file_clean()
    letters=[]
    buchst=[]
    lista_rta=[]
    dicc_rta={}

    for t in range(0,len(tup_lst)):
        e=list(str((tup_lst[t][3])).split(','))
        l=tuple(e)
        letters.append(l)
        e.append(tup_lst[t][1])

        def mixs(num):
            try:
                ele = int(num)
                return (0, ele, '')
            except ValueError:
                return (1, num, '')

        e.sort(key = mixs)
        e[0]=int(e[0])
        e=tuple(e)
        voll_liste.append(e)

    for p in letters:
        for r in p: buchst.append(r)

    letters=None
    letters=sorted(list(set(buchst)),reverse=False)

    for k in letters:
        suma=0
        for i in voll_liste:
            for j in i:
                if k==j:
                    suma+=i[0]   
        h=(k,suma)
        lista_rta.append(h)
        
    for elemento in lista_rta:
        dicc_rta[elemento[0]]=elemento[1]
        
    return dicc_rta


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    tup_lst=file_clean()
    voll_liste=[]
    letters=[]
    buchst=[]
    lista_rta=[]
    dicc_rta={}

    for x in range(0,len(tup_lst)):
        a=str((tup_lst[x][4])).split(',')
        d=tup_lst[x][0]
        letters.append(d)
        suma=0
        for w in a:
            #print(w)
            q=int(w[4:])
            suma+=q
        h=(d,suma)
        voll_liste.append(h)

    for p in letters:
        for r in p: buchst.append(r)

    letters=None
    letters=sorted(list(set(buchst)),reverse=False)

    for k in letters:
        cont=0
        for i in voll_liste:
            for j in i:
                if k==j:
                    cont+=i[1]   
        f=(k,cont)
        lista_rta.append(f)

    for elemento in lista_rta:
        dicc_rta[elemento[0]]=elemento[1]
    
    return dicc_rta

