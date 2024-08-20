def change():
    spent= float(input("Ingresar gasto:\n"))
    received= float(input("Dinero recibido\n"))
    change= received-spent
    intchange= int((change - int(change))*100)
    print("\nVuelto")
    print (f"\nPesos:\n{int(change)}\nCentavos:\n{intchange}")
