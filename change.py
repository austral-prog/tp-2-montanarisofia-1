def change():
    spent= float(input("Ingresar gasto:\n"))
    received= float(input("Dinero recibido:\n"))
 #Calculating change from now change= received - spent
    change= received-spent
    intchange= int((change - int(change))*100)
    print("\nVuelto")
    print (f"\nPesos:\n{int(change)}\nCentavos:\n{intchange}")
change()