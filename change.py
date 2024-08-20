def change():
    spent= input("Ingresar gasto:\n")
    received= input("Dinero recibido\n")
    change= float(received) - float(spent)
    intchange= int((change - int(change)) * 100)
    print("\nVuelto\n")
    print(f"Pesos:\n{int(change)}")
    print(f"Centavos:\n{intchange}")
