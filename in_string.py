def check_vowels():
    nombre=(input("ingresar nombre: "))
    A= ("a" in nombre.lower())
    E= ("e" in nombre.lower())
    I= ("i" in nombre.lower())
    O= ("o" in nombre.lower())
    U= ("u" in nombre.lower())
    print(f"Contiene a: {A}")
    print(f"Contiene e: {E}")
    print(f"Contiene i: {I}")
    print(f"Contiene o: {O}")
    print(f"Contiene u: {U}")

