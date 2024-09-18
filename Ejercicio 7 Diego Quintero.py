#bienvenidos al himalaya, helao?
tecla = "x" #sé que esto no era necesario pero me inspiré, asi queda mas profesional
print ("Bienvenide al nuevo portal del colegio la Salle Grita para conocer tu calificación en un formato actualizado, ingresa ´x´ para continuar.") #ahora sabrá que raspará pero en letrica

teclaIngresada = input()

if tecla == teclaIngresada: #sé que esto no era necesario pero me inspiré, asi queda mas profesional x2
    
    print ("ingresa tu calificación (0-100).") #aca si empieza lo que es, ingresar numero del 0 al 100, solo numeros en ese parametro!!!!
    nota = int(input())
    if nota <= 100: #esto es para que de un error cuando ingrese un numero que no sea del parametro ya antes aplicado (0-100)
        if nota >= 90:
            print ("Tu calificación es A, cerebrito.") # esto aja
        
        elif nota >= 80 and nota < 90:
            print ("Tu calificación es B, bien hecho") #nada q  explicar
        elif nota >= 70 and nota < 80:
            print ("Tu calificacioón es C, puedes mejorar") #lo mismo
        elif nota >= 60 and nota < 70:
            print ("Tu calificación es D, a un paso de la muerte") #casi morido
        else: 
            print ("Tu calificación es F, *morido*") #pana raspao
    else:
        print ("las notas van desde el 0 hasta el 100, la nota ingresada es invalida, reinicia el programa para volver a intentarlo") #DIJE DEL 0 AL 100!!!, error por no ingresar numeros en el parametro de 0-100
else:
    print("no has presionado la tecla correcta, ni la F es calificacion para ti. reinicia el programa para volver a intentarlo") #esto para que de un error si no presionan la tecla correcta al inicio


#profe yo considero esto una preciosidad de codigo, estoy orgulloso del esfuerzo que puse aca!!!!, no es sarcasmo!, le eche bola
