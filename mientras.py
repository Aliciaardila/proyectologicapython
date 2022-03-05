# importar libreria (recetas/codigo, prefabricados)
import math
#variable controladora

#declaro el bucle/ciclo
#menu
print("Empanadas el machetico")
print("********************")
print("0. para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un #")
print("2. Digita 2 para calcular la potencia de un #")
print("********************")
opcion=1
while(opcion!=0):
    #variable controladora
    opcion=int(input("Digita una opcion:"))
    # pregunte por la opcion
    if(opcion==0):
        break
    elif(opcion==1):
        numero=int(input("Digita un nuemro:"))
        raiz=math.sqrt(numero)
        print(f"La raiz de {numero} es{raiz}")
    elif(opcion==2):
        numero=int(input("Digita un nuemro:"))  
        potencia= math.pow(numero,2)
        print(f"La potencia es{potencia}")
    else:
        print(f"Digite una opcion valida")
        
    