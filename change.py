def change():
    expense = 23.75
    money = 100
    spent= float(input("Ingresar gasto:\n"))
    received= float(input("Dinero recibido\n"))
    change= received - spent
    intchange= int((change - int(change)) * 100)
    print() 
    print("Vuelto")
    print()
    print(f"Pesos:\n{int(change)}")
    print(f"Centavos:\n{intchange}")
