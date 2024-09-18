precioPorZapato = 80 #variable a usar

print ("Ingrese la cantidad de zapatos a comprar") #cuantos zapatos panita?
cantidadZapatos = int (input()) #añadirlo a variable



if cantidadZapatos > 30:
        descuento = 0.40 #si compras mas de 30 tienes 40 de descuento
        
elif 20 < cantidadZapatos <= 30:
        descuento = 0.20 #mas de 20 pero igual o menos de 30 tienes 20 de descuento
        
elif cantidadZapatos > 10:
        descuento = 0.10 #si compras mas de 10, tienes esto
        
else: 
        descuento = 0.0 #solo se tomará en cuenta la variable descuento que concuerde con la cantidad de zapatos que seran comprados

totalSinDescuento = cantidadZapatos * precioPorZapato #pin pan pun
totalConDescuento = totalSinDescuento * (1 - descuento) #calculitos para sacar precio con descuento
    

print(f"El total con descuento es: ${totalConDescuento:.2f}") #admito que aca si necesité ayuda

#guapisimos aca vegetta777
