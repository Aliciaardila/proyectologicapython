#condicionales ejemplo estaciones
mesaño=input("Digita un mes del año:")
print(f"el mes digitado fue:{mesaño}")
#caminos para clasificar le mes
if(mesaño == "Diciembre" or mesaño == "Enero" or mesaño =="Febrero" or mesaño=="Marzo"):
    print("Esta en invierno")
elif(mesaño == "Junio" or mesaño == "Julio" or mesaño =="Agosto"):
    print("Esta en verano")
elif(mesaño == "Abril" or mesaño == "Mayo"):
    print("Esta en Primavera")
elif (mesaño == "Septiembre" or mesaño == "Octubre" or mesaño =="Noviembre"):
    print("Esta en Otoño")
else: 
    print("Mes no existe")