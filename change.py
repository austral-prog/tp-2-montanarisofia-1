def change():
    spent= input("Ingresar gasto:\n")
    received= input("Dinero recibido:\n")
 #Calculating change from now change= received - spent
    change= received-spent
    intchange= int((change - int(change))*100)
    print("\nVuelto")
    print (f"\nPesos:\n{int(change)}\nCentavos:\n{intchange}")
