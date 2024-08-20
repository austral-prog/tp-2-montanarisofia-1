def change():
    spent= float(input("Ingresar gasto:\n"))
    received= float(input("Dinero recibido\n"))
    change= received - spent
    intchange= int((change - int(change)) * 100)
    print("\nVuelto\n")
    print(f"Pesos:\n{int(change)})
    print(f"Centavos:\n{intchange}")
