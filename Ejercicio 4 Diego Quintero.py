#aca vereis en que grupo tocas
nombre = input("Introduce tu nombre: ")#se guarda en la variable nombre
sexo = input("Introduce tu sexe (M para cromosoma xx, H para cromosoma xy): ") #lo mas inclusive posible, aca se guarda en la variable sexo

nombre = nombre.lower() #poner todo el nombre en minuscula para evitar errores si coloca el nombre con la inicial mayuscula


if (sexo == "M" and nombre < "m") or (sexo == "H" and nombre > "n"): #si eres xy y tu inicial esta adelante de la n, grupo A or si eres xx y tu inicial es atras que M
    print ("Tu grupo es el A") 
else:
    print ("Tu grupo es el B") #si no se cumple lo antes visto, toca pal B


